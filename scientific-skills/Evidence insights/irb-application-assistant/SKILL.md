---
name: irb-application-assistant
description: Assists researchers with Institutional Review Board (IRB) application tasks, including drafting informed consent documents, reviewing research protocols for compliance, generating application forms, and preparing submission checklists. Use when the user mentions IRB, Institutional Review Board, research ethics, human subjects research, protocol review, informed consent, or needs help preparing or reviewing an IRB application or submission.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# IRB Application Assistant

Helps researchers prepare, review, and submit Institutional Review Board (IRB) applications. Supports drafting informed consent templates, checking protocol compliance, generating application documents, and guiding researchers through the submission workflow.

## Quick Start

```bash
# Generate an informed consent template
python scripts/main.py --task consent --protocol protocol.json --output consent_form.docx

# Run a compliance check on a research protocol
python scripts/main.py --task compliance-check --protocol protocol.json --verbose

# Generate a full IRB application package
python scripts/main.py --task generate-application --config study_config.json --output irb_package/
```

## Core Capabilities

### 1. Generate Informed Consent Documents

Produces compliant informed consent forms based on study parameters such as participant population, risk level, and study type.

```bash
python scripts/main.py --task consent \
  --protocol protocol.json \
  --population "adults 18+" \
  --risk-level minimal \
  --output consent_form.docx
```

### 2. Protocol Compliance Review

Checks a research protocol against IRB requirements and flags missing or non-compliant sections.

```bash
python scripts/main.py --task compliance-check \
  --protocol protocol.json \
  --ruleset federal-common-rule \
  --output compliance_report.txt
```

### 3. Application Form Generation

Generates completed IRB application forms (e.g., initial review, continuing review, amendment) from structured study data.

```bash
python scripts/main.py --task generate-application \
  --form-type initial-review \
  --config study_config.json \
  --output irb_application.docx
```

### 4. Submission Checklist Validation

Validates that all required documents and fields are present before submission.

```bash
python scripts/main.py --task validate-submission \
  --package irb_package/ \
  --output validation_report.txt
```

## Recommended Workflow

Follow these steps for a complete IRB submission:

1. **Prepare study configuration** — Populate `study_config.json` with study title, PI details, participant population, risk level, and procedures.
2. **Run compliance check** — Use `--task compliance-check` to identify gaps in the protocol before drafting documents.
   - ⛔ **Checkpoint**: If the compliance report flags ANY errors, resolve ALL flagged items and re-run `--task compliance-check` before proceeding. Do not advance to step 3 with unresolved compliance errors.
3. **Generate consent document** — Use `--task consent` to produce a compliant informed consent form tailored to the study.
4. **Generate application forms** — Use `--task generate-application` to produce the required IRB submission forms.
5. **Validate submission package** — Use `--task validate-submission` to confirm all required documents are present and fields are complete.
   - ⛔ **Checkpoint**: If validation fails, follow this loop: review errors in `validation_report.txt` → fix each issue → re-run `--task validate-submission` → only proceed when the report shows zero blocking errors.
6. **Review and submit** — Manually review any remaining warnings in the compliance and validation reports before submitting to the IRB.

## Quality Checklist

- [ ] Protocol includes all required sections (purpose, procedures, risks, benefits, confidentiality)
- [ ] Informed consent language is at appropriate reading level for participant population
- [ ] Risk level classification is justified and documented
- [ ] All required attachments (recruitment materials, surveys, data management plan) are included
- [ ] Compliance report reviewed and all flagged items resolved
- [ ] Submission package validated with zero blocking errors

## References

- `references/guide.md` — Detailed documentation and field descriptions
- `references/examples/` — Sample protocols, consent forms, and completed applications

---

**Skill ID**: 952 | **Version**: 1.0 | **License**: MIT
