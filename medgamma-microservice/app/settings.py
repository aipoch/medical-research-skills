"""Environment-driven settings for the MedGamma microservice."""

from __future__ import annotations

import os
from dataclasses import dataclass


def _int_env(name: str, default: int) -> int:
    try:
        return int(os.getenv(name) or default)
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    runpod_api_key: str = (os.getenv("RUNPOD_API_KEY") or "").strip()
    medgamma_endpoint_id: str = (os.getenv("MEDGAMMA_ENDPOINT_ID") or "").strip()
    medgamma_model: str = (os.getenv("MEDGAMMA_MODEL") or "google/medgemma-27b-text-it").strip()
    # Sampling parameters are code/server-owned — callers cannot override.
    medgamma_max_tokens: int = _int_env("MEDGAMMA_MAX_TOKENS", 4096)
    medgamma_timeout_seconds: int = _int_env("MEDGAMMA_TIMEOUT_SECONDS", 600)
    microservice_api_key: str = (os.getenv("MICROSERVICE_API_KEY") or "").strip()


settings = Settings()