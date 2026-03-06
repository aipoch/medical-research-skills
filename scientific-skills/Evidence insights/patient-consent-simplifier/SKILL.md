---
name: patient-consent-simplifier
description: Use when simplifying informed consent documents, translating medical procedures for patients, creating patient-friendly research summaries, or adapting clinical trial information for lay audiences. Maintains regulatory compliance while improving readability.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Patient Consent Simplifier

Transform complex informed consent documents into patient-friendly language while maintaining regulatory compliance and ethical standards.

## Quick Start

```python
from scripts.consent_simplifier import ConsentSimplifier

simplifier = ConsentSimplifier()

# Simplify consent form
simplified = simplifier.simplify(
    document="clinical_trial_consent.pdf",
    reading_level="8th_grade",
    preserve_legal=True
)
```

## Core Capabilities

### 1. Document Simplification

```python
result = simplifier.simplify_section(
    section="procedure_description",
    text="Lumbar puncture will be performed under sterile conditions...",
    max_sentences=3
)
```

**Simplification Rules:**
- Break long sentences (>20 words)
- Replace medical jargon with common terms
- Use active voice
- Add visual aids placeholders
- Maintain key legal elements

### 2. Risk/Benefit Clarification

```python
risks = simplifier.clarify_risks(
    original_text="Potential adverse events include...",
    format="table",
    severity_scale="emoji"  # or "color", "text"
)
```

**Risk Presentation:**
| Risk | Likelihood | Severity |
|------|-----------|----------|
| Headache | Common (1 in 10) | Mild 😊 |
| Infection | Rare (1 in 1000) | Serious ⚠️ |

### 3. Reading Level Assessment

```python
metrics = simplifier.assess_readability(document)
print(f"Current grade level: {metrics.grade_level}")
print(f"Suggested improvements: {metrics.suggestions}")
```

**Target Levels:**
- **General population**: 8th grade
- **Vulnerable populations**: 6th grade
- **Health literacy challenges**: 4th-5th grade

### 4. Regulatory Compliance Check

```python
compliance = simplifier.check_compliance(
    simplified_document,
    regulations=["FDA_21CFR50", "ICH-GCP", "HIPAA"]
)
```

**Required Elements:**
- [ ] Purpose of research
- [ ] Procedures involved
- [ ] Risks and discomforts
- [ ] Benefits
- [ ] Alternatives
- [ ] Confidentiality
- [ ] Compensation
- [ ] Contact information
- [ ] Voluntary participation

## CLI Usage

```bash
# Simplify PDF
python scripts/consent_simplifier.py \
  --input consent_form.pdf \
  --output simplified_consent.pdf \
  --grade-level 8

# Check compliance only
python scripts/consent_simplifier.py \
  --check compliance \
  --input document.pdf
```

## Best Practices

**Do:**
- Use "you" and "your"
- Define terms on first use
- Use bullet points for lists
- Include visual aids
- Test with patient advocates

**Don't:**
- Remove required legal elements
- Downplay significant risks
- Use coercive language
- Exceed recommended length

---

**Skill ID**: 208 | **Version**: 1.0 | **License**: MIT
