"""MedGamma microservice — FastAPI app wrapping the RunPod MedGamma endpoint.

Sampling parameters (max_tokens, temperature) are owned here and injected
into the upstream RunPod payload server-side. The public contract accepts
{prompt | messages, caller} only; sampling fields are rejected (422).
"""

from __future__ import annotations

import logging
import time

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, ConfigDict, Field, field_validator

from .settings import settings
from .upstream import MedGammaUpstream, UpstreamError

logger = logging.getLogger("medgamma_microservice")

app = FastAPI(title="MedGamma Microservice", version="1.0.0")

_upstream = MedGammaUpstream(
    api_key=settings.runpod_api_key,
    endpoint_id=settings.medgamma_endpoint_id,
    model=settings.medgamma_model,
    max_tokens=settings.medgamma_max_tokens,
    timeout_seconds=settings.medgamma_timeout_seconds,
)


class _NoSamplingFields(BaseModel):
    """Reject client-side sampling overrides — they live in code/settings."""

    model_config = ConfigDict(extra="forbid")


class CompletionRequest(_NoSamplingFields):
    prompt: str | None = None
    messages: list[dict] | None = None
    caller: str = Field(default="microservice", max_length=128)

    @field_validator("caller")
    @classmethod
    def _alphanumeric_caller(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("caller must not be blank")
        return cleaned


class AEExtractRequest(_NoSamplingFields):
    prompt: str

    @field_validator("prompt")
    @classmethod
    def _nonempty_prompt(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("prompt must not be blank")
        return value


def _require_api_key(authorization: str | None = Header(default=None)) -> None:
    """Optional bearer gate for this service (MICROSERVICE_API_KEY)."""
    if not settings.microservice_api_key:
        return
    if authorization != f"Bearer {settings.microservice_api_key}":
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/health")
def health() -> dict:
    upstream_ready = _upstream.health()
    return {
        "status": "ok" if upstream_ready else "degraded",
        "upstream_ready": upstream_ready,
        "model": settings.medgamma_model,
        "endpoint_id": settings.medgamma_endpoint_id or None,
        "enabled": bool(settings.runpod_api_key and settings.medgamma_endpoint_id),
    }


def _resolve_messages(payload: CompletionRequest) -> list[dict]:
    if payload.prompt and payload.messages:
        raise HTTPException(status_code=422, detail="Provide either 'prompt' or 'messages', not both")
    if payload.prompt:
        return [{"role": "user", "content": payload.prompt}]
    if payload.messages:
        if not isinstance(payload.messages, list) or not payload.messages:
            raise HTTPException(status_code=422, detail="messages must be a non-empty array")
        return payload.messages
    raise HTTPException(status_code=422, detail="Provide 'prompt' or 'messages'")


def _complete(messages: list[dict], caller: str) -> dict:
    started = time.perf_counter()
    try:
        result = _upstream.chat_completion(messages, caller=caller)
    except UpstreamError as exc:
        logger.warning("Upstream error caller=%s: %s", caller, exc)
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    latency_ms = (time.perf_counter() - started) * 1000
    logger.info(
        "caller=%s latency_ms=%.0f prompt_tokens=%s completion_tokens=%s finish=%s",
        caller,
        latency_ms,
        result.usage.get("prompt_tokens"),
        result.usage.get("completion_tokens"),
        result.finish_reason,
    )
    return {
        "content": result.content,
        "finish_reason": result.finish_reason,
        "usage": result.usage,
        "model": settings.medgamma_model,
        "caller": caller,
        "latency_ms": round(latency_ms),
    }


@app.post("/v1/completions")
def completions(payload: CompletionRequest, _: None = Depends(_require_api_key)) -> dict:
    return _complete(_resolve_messages(payload), payload.caller)


@app.post("/v1/chat/completions")
def chat_completions(payload: CompletionRequest, _: None = Depends(_require_api_key)) -> dict:
    return _complete(_resolve_messages(payload), payload.caller)


@app.post("/v1/extract-ae")
def extract_ae(payload: AEExtractRequest, _: None = Depends(_require_api_key)) -> dict:
    """AE extraction helper: run the prompt and JSON-parse the reply."""
    import json

    response = _complete([{"role": "user", "content": payload.prompt}], caller="extract_ae")
    text = (response["content"] or "").strip()
    if text.startswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as decode_error:
        raise HTTPException(
            status_code=502,
            detail={"error": "Upstream returned non-JSON content", "raw_prefix": text[:200], "detail": str(decode_error)},
        ) from decode_error
    return {**response, "parsed": parsed}