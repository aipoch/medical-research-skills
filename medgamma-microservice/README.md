# MedGamma Microservice

Standalone FastAPI microservice wrapping the **MedGamma** LLM (MedGemma 27B,
`google/medgemma-27b-text-it`) served on RunPod Serverless behind its
OpenAI-compatible vLLM route.

The service owns **all** sampling parameters in code — callers never send
`max_tokens` / `temperature`. The wire body to this microservice is
`{prompt | messages, caller}` only.

Forked from [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)
(`randomization-gen` skill lineage; MIT).

## Endpoints

| Method | Path | Body | Response |
|--------|------|------|----------|
| `GET` | `/health` | — | `{status, upstream_ready, workers, model, enabled}` |
| `POST` | `/v1/completions` | `{"prompt": "...", "caller": "..."}` | `{"content": "...", "finish_reason": "...", "usage": {...}, "model": "..."}` |
| `POST` | `/v1/chat/completions` | `{"messages": [{role, content}], "caller": "..."}` | same |
| `POST` | `/v1/extract-ae` | `{"prompt": "..."}` (AE extraction JSON prompt) | JSON-parsed AE array or `{"error"}` |

### Request contract

```json
{"prompt": "<clinical prompt text>", "caller": "ae_extraction"}
```

- `prompt` **or** `messages` — one required.
- `caller` — optional audit label (default `"microservice"`).
- **No sampling fields accepted.** `max_tokens` and `temperature` are set
  server-side from env (`MEDGAMMA_MAX_TOKENS`, default 4096) and pinned
  (`temperature=0.0`, clinical determinism). Extra sampling fields in the
  request body are rejected with 422.

### Response

```json
{
  "content": "MEDGAMMA OK\n",
  "finish_reason": "stop",
  "usage": {"prompt_tokens": 16, "completion_tokens": 5, "total_tokens": 21},
  "model": "google/medgemma-27b-text-it",
  "caller": "microservice",
  "latency_ms": 412
}
```

Errors mirror the upstream RunPod contract: `404 endpoint not found`,
`400 invalid request body`, `500` wrong model id, `524`/timeout cold start
(fallback: `POST /run` + `GET /status/{id}` polling, implemented in
`upstream.py`).

## Configuration (env)

| Var | Default | Purpose |
|-----|---------|---------|
| `RUNPOD_API_KEY` | — | RunPod Bearer key (server-side only) |
| `MEDGAMMA_ENDPOINT_ID` | — | RunPod serverless endpoint (e.g. `te0qpuvto18vuj`) |
| `MEDGAMMA_MODEL` | `google/medgemma-27b-text-it` | vLLM-served model id |
| `MEDGAMMA_MAX_TOKENS` | `4096` | Completion cap (code-controlled) |
| `MEDGAMMA_TIMEOUT_SECONDS` | `600` | Upstream HTTP timeout |
| `MICROSERVICE_API_KEY` | — | Optional bearer gate for *this* service |
| `MICROSERVICE_PORT` | `8100` | Listen port |

## Run

```bash
pip install -r medgamma-microservice/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8100   # from medgamma-microservice/
```

Docker: `docker build -t medgamma-microservice medgamma-microservice/ && docker run --rm -p 8100:8100 --env-file .env medgamma-microservice`

## Layout

```
medgamma-microservice/
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI app, routes, auth gate
│   ├── upstream.py    # RunPod OpenAI-route client (sampling params injected here)
│   └── settings.py    # env config
├── tests/
│   └── test_api.py    # contract tests (sampling fields rejected, happy path)
├── requirements.txt
└── Dockerfile
```

## Relationship to HC_AI

`HC_AI/api/services/medgamma_client.py` is the in-process variant of the same
contract (sampling params in code). This microservice decouples it so HC_AI
(or any other consumer) talks HTTP to a single governed LLM gateway; swap
`medgamma_client.chat_completion` to `POST {MICROSERVICE}/v1/completions`
later without touching prompt pipelines.