---
name: phi-prompt-guard
description: Runtime, prompt-time guardrail that prevents Protected Health Information (PHI) from entering the LLM context. Use when the user is about to paste, query, or read clinical/patient data, or when an action (DB query, file read, tool output) may pull PHI into the conversation. Honors a [PHI-OK] attestation for synthetic / test data.
license: MIT
author: AIPOCH
---
> **Source**: [https://github.com/aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)
> **Contributed by**: [@ndu-bioinfo](https://github.com/ndu-bioinfo)

# PHI Prompt Guard

A behavioral skill that instructs the agent to refuse, redact, or redirect when the live prompt — or an action the agent is about to take — would push Protected Health Information (PHI) into the LLM context window. Operates under the assumption that no Business Associate Agreement exists with the LLM provider: any data placed in the prompt is sent to a third-party API outside the organization's control and may be cached or logged depending on vendor terms.

## When to Use

- The user pastes (or is about to paste) clinical, patient, or specimen data into the conversation.
- The agent is about to run a database client (`psql`, `mysql`, `mongo`, `duckdb`, `sqlite3`, `bq`, `snowsql`, `redis-cli`, `clickhouse-client`, `cqlsh`) or a dump tool (`pg_dump`, `mysqldump`, `mongodump`) against an environment that may contain PHI.
- The agent is about to read a file whose contents may contain identifiers (lab reports, EHR exports, accession-keyed CSVs).
- Discussion involves keywords such as: `patient`, `clinical`, `accession`, `phi`, `hipaa`, `mrn`, `medical record`, `health plan`, `social security`.
- The environment is unknown — assume production with PHI by default.

## Key Features

- Runtime PHI detection in the live prompt — catches obfuscated dates, names spelled across turns, foreign formats, indirect identifiers, and prose-form PHI that regex scanners miss.
- Action-level guardrails for database clients, dump tools, and file reads that could stream PHI into context; instructs the agent to generate the command for the user to run locally rather than executing it.
- Full HIPAA Safe Harbor 18-identifier taxonomy plus the 90+ age aggregation rule.
- `[PHI-OK]` attestation protocol that lets users work freely with synthetic/test data without false refusals or lecturing.
- Concrete decision rules: "schema is safe, data is not"; "error messages are usually safe"; "unknown environment ⇒ assume production with PHI"; "generate, don't execute".
- Pure in-context behavioral skill — no scripts, no external services, portable across agent frameworks.

## Dependencies

- None (documentation-only behavioral skill).

## Example Usage

### Scenario 1 — User pastes a clinical row

> *"Why won't this row parse? `Jane Doe, MRN 0044812, DOB 1985-03-15, dx SMA`"*
> *(synthetic — illustrative only)*

Correct agent behavior:
1. Detect category: name + MRN + DOB.
2. Do not echo the PHI.
3. Reply: "That row contains three HIPAA identifiers (name, MRN, DOB). Re-submit with the identifier columns redacted, or append `[PHI-OK]` if these are synthetic fixtures."

### Scenario 2 — User asks for a SQL query against a clinical DB

> *"Pull the last 10 lab results from `clinical.results` so I can debug the parser."*

Correct agent behavior:
1. Recognize `psql`/`bq`/etc. would stream PHI into context.
2. Generate the SQL but **do not execute**: `SELECT * FROM clinical.results ORDER BY collected_at DESC LIMIT 10;`
3. Instruct: "Run this in your own terminal and paste only de-identified columns or the parser error message back here."

### Scenario 3 — Synthetic test fixture with `[PHI-OK]`

> *"Compute age-at-diagnosis: DOB 03/15/1985, dx 2020-06-01 [PHI-OK]"*

Correct agent behavior: answer directly — `Age at diagnosis = 35`. No refusal, no redaction, no lecture.

### Scenario 4 — `[PHI-OK]` misused on an EHR-shaped paste (override)

> *"Patient Jonathan A. Smith, DOB 1962-08-22, MRN 88440213, admitted 2024-11-04 to Memorial Hospital, NYC, for stage IV pancreatic adenocarcinoma. Current meds: gemcitabine + nab-paclitaxel. ECOG 2. Help me write the discharge summary. [PHI-OK]"*

Correct agent behavior: override the attestation. The paste matches ≥3 of the override heuristics (real-looking full name, named hospital, exact admission date, current regimen, plausible MRN format). Reply: "This reads as a real chart despite `[PHI-OK]`. Confirm it is synthetic and I'll proceed, or re-submit with name / MRN / hospital / exact dates removed and I'll draft a discharge-summary template you can fill in locally."

## Implementation Details

- Pure in-context behavioral skill — no scripts, no external services, no persisted state.
- Inputs: the live prompt plus any tool output the agent is considering.
- Outputs: (a) a refusal-with-redirect when PHI is detected, (b) a generated-but-unexecuted command when an action would pull PHI in, or (c) a normal task response when `[PHI-OK]` is present or no PHI is present.
- Each prompt is evaluated independently, **but** when the current prompt completes an identifier started in an earlier turn (e.g., last name now + first name two turns ago, or MRN tail now + MRN head earlier), the assembled identifier still counts as PHI and the current prompt must be treated as a PHI prompt.

## Instructions

### Your Responsibilities (the agent)

1. **Detect PHI the prompt scanner missed.** Obfuscated dates, names spelled across turns, foreign formats, indirect identifiers, prose like *"the patient born in March 1985 with SMA…"*. Do not process, repeat, summarize, or store the PHI. Warn the user and offer two paths: redact, or re-submit with `[PHI-OK]` if it is synthetic.
2. **Prevent PHI from entering via actions.** Before running a database client, dump tool, or file read whose output may contain PHI, **stop and generate the command for the user to run in their own terminal** rather than executing it yourself.
3. **Honor the `[PHI-OK]` attestation.** When present in the prompt, treat identifier-looking values as synthetic / test data. Do not refuse, redact, or lecture. Override only if the data is unmistakably real and operational despite the token.

### The 18 HIPAA Identifiers (never let into LLM context)

1. Names
2. Geographic data smaller than state (street, city, county, ZIP — ZIP3 only for large areas)
3. Dates (except year) tied to an individual — DOB, admission, discharge, death
4. Phone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers (MRN)
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate / license numbers
12. Vehicle identifiers and serial numbers (including license plates)
13. Device identifiers and serial numbers
14. Web URLs
15. IP addresses
16. Biometric identifiers (fingerprints, voiceprints)
17. Full-face photographs and comparable images
18. Any other unique identifying number, characteristic, or code (accession numbers, specimen IDs, rare-disease combinations that re-identify)

Also PHI under Safe Harbor: **ages above 89** (must be aggregated as `90+`).

### Actions That Can Pull PHI Into Context

| Action | Risk | Safe alternative |
|---|---|---|
| `psql`, `mysql`, `mongo`, `duckdb`, `sqlite3`, `bq`, `snowsql`, `redis-cli`, `clickhouse-client`, `cqlsh` | Query results enter LLM context | Generate the SQL; user runs it in their own terminal |
| `pg_dump`, `mysqldump`, `mongodump` | Full table contents stream into context | Generate the command; user runs it and keeps output local |
| `Read` on clinical files, CSVs, lab reports | File contents enter context | Ask the user to confirm the file is de-identified, or redact first. Safe inspection patterns: `head -1` (header row only), `df.dtypes` / `\d <table>` (types only), or `wc -l` (row count only) — none of these reveal row data |
| Schema-only queries (`\dt`, `SHOW TABLES`, `DESCRIBE`) | None | Safe — structure is not PHI |

**Operating rules:**
- **Schema is safe; data is not.** Structure, column names, and types are fine. Row data may contain PHI.
- **Error messages are usually safe** to paste — they rarely contain PHI. **Exception:** errors that quote a row value embed whatever that value was (e.g., `ValueError: cannot parse 'John Smith' as date`). Treat such errors as PHI if the quoted value is an identifier.
- **Unknown environment ⇒ assume production with PHI.**
- **Generate, don't execute.** For any data source that may contain PHI, hand the user the command rather than running it yourself. Do not echo the user's original PHI-pulling command back to them either — substitute a safer projection (drop identifier columns), a schema-only query, or an aggregate query directly.

### The `[PHI-OK]` Attestation — treat as synthetic, proceed normally

When the user includes the literal token `[PHI-OK]` anywhere in a prompt, they are attesting that any identifier-looking content is **synthetic / test / non-PHI data** (fake DOBs in fixtures, redacted examples, regex development input, mock patient records for unit tests).

**Required behavior when `[PHI-OK]` is present:**

- **Proceed with the task.** Treat the values as synthetic and answer the user's actual question.
- **Use the values directly** in computation, code, examples, and output — including echoing them back when needed (filling in a template, building a fixture, computing an age from a DOB).
- **Do not refuse, redact, mask, or substitute placeholders.**
- **Do not lecture, even on HIPAA-adjacent tasks.** Do not warn the user that the values "look like PHI" or remind them about HIPAA. They already asserted it. This applies even when the task itself is HIPAA-related (training material, compliance examples, redaction tutorials) — produce the requested artifact and stop; do not append unsolicited identifier-categorization commentary or Safe Harbor reminders.
- **Do not re-invoke this skill's protections** against the attested data. The attestation covers the whole prompt.

Example — answer this directly, echoing the DOB as needed:

> `DOB: 03/15/1985 [PHI-OK] — compute age if dx was 2020-06-01`

Correct response: *"Age at diagnosis = 35 (birthday had passed by June 1)."*
Not: *"I can't process that DOB…"*

**Override the attestation only when** the prompt contains unmistakable evidence of real, operational PHI despite the token. Concrete override heuristic — override if **three or more** of the following are present together:

- Real-looking full name (first + last, plausible spelling)
- Named hospital, clinic, payer, or other identifiable institution
- Exact admission, discharge, encounter, or procedure date (not just a year)
- Current medication regimen, dose, or clinical-grade detail (ECOG, stage, lab values with units)
- Identifier-format-matching MRN, accession number, or payer ID (right digit count, recognizable institution prefix)
- Live-EHR-shaped layout (chart sections, structured field labels, signed-by lines)

Two or fewer signals → honor the token. Three or more → override and ask the user to confirm the data is synthetic, or to redact and re-submit. Default to honoring the token; only override when the evidence is overwhelming. The token is an attestation, not a magic word; misuse is a policy violation on the user's side, not a technical failure on the model's side.

### When PHI Is Detected (no `[PHI-OK]`)

1. Do **not** echo, quote, or summarize the PHI. This includes the offending value itself when explaining the detection — say *"the age you provided exceeds 89"* rather than restating *"94"*, and *"the embedded name in the error string"* rather than quoting it back.
2. Tell the user which category was detected (e.g., "labeled DOB + name").
3. Offer two paths:
   - Redact and re-submit, or
   - Re-submit with `[PHI-OK]` if the data is synthetic / test.
4. If a clinical question underlies the prompt, answer it generically using only non-identifying information (e.g., birth year + dx year for age-at-diagnosis).
