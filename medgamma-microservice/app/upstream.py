"""RunPod OpenAI-route client — the ONLY place sampling parameters are set.

The upstream contract (verified live, 2026-09-22):

    POST https://api.runpod.ai/v2/{ENDPOINT_ID}/openai/v1/chat/completions
    Authorization: Bearer {RUNPOD_API_KEY}

    {"model": "google/medgemma-27b-text-it", "messages": [...]}   ← caller body

    max_tokens (default 4096) and temperature (0.0) are injected here,
    never accepted from microservice callers.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

import requests


@dataclass
class CompletionResult:
    content: str
    finish_reason: str | None
    usage: dict = field(default_factory=dict)
    raw: dict | None = None


class UpstreamError(RuntimeError):
    """Raised for any non-200 upstream response or transport failure."""


class MedGammaUpstream:
    def __init__(
        self,
        *,
        api_key: str,
        endpoint_id: str,
        model: str,
        max_tokens: int,
        timeout_seconds: int,
    ) -> None:
        self._api_key = api_key
        self._endpoint_id = endpoint_id
        self._model = model
        self._max_tokens = max_tokens
        self._timeout_seconds = timeout_seconds
        self._temperature = 0.0  # pinned — clinical determinism
        self._http = None

    def _client(self):
        if self._http is None:
            self._http = requests.Session()
        return self._http

    @property
    def base_url(self) -> str:
        return f"https://api.runpod.ai/v2/{self._endpoint_id}"

    def chat_completion(self, messages: list[dict], *, caller: str = "microservice") -> CompletionResult:
        if not self._api_key:
            raise UpstreamError("RUNPOD_API_KEY is not set on the microservice")
        if not self._endpoint_id:
            raise UpstreamError("MEDGAMMA_ENDPOINT_ID is not set on the microservice")

        payload = {
            "model": self._model,
            "messages": messages,
            # Sampling params owned by the service (never by callers):
            "max_tokens": self._max_tokens,
            "temperature": self._temperature,
        }

        started = time.perf_counter()
        try:
            response = self._client().post(
                f"{self.base_url}/openai/v1/chat/completions",
                json=payload,
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                    "Content-Type": "application/json",
                },
                timeout=self._timeout_seconds,
            )
        except Exception as transport_error:  # requests.RequestException
            raise UpstreamError(f"MedGamma request failed: {transport_error}") from transport_error

        if response.status_code != 200:
            raise UpstreamError(f"MedGamma returned HTTP {response.status_code}: {(response.text or '')[:400]}")

        data = response.json()
        try:
            choice = data["choices"][0]
            content = choice["message"]["content"] or ""
            finish_reason = choice.get("finish_reason")
        except (KeyError, IndexError, TypeError) as shape_error:
            raise UpstreamError(f"MedGamma returned an unexpected shape: {shape_error}") from shape_error

        latency_ms = (time.perf_counter() - started) * 1000
        usage = data.get("usage") or {}
        print(
            f"[medgamma] caller={caller} latency_ms={latency_ms:.0f} "
            f"prompt_tokens={usage.get('prompt_tokens')} completion_tokens={usage.get('completion_tokens')}",
            flush=True,
        )
        return CompletionResult(content=content, finish_reason=finish_reason, usage=usage, raw=data)

    def health(self) -> bool:
        if not self._api_key or not self._endpoint_id:
            return False
        try:
            response = self._client().get(
                f"{self.base_url}/health",
                headers={"Authorization": f"Bearer {self._api_key}"},
                timeout=15,
            )
            return response.status_code == 200
        except Exception:
            return False