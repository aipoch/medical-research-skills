---
name: tone-adjuster
description: Use when converting medical text between academic and patient-friendly tones, translating medical jargon for patients, adapting research papers for public audiences, or rewriting clinical notes for patient handouts. Maintains medical accuracy while adjusting readability level.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Medical Tone Adjuster

Convert medical text between academic rigor and patient-friendly language while preserving clinical accuracy.

## Quick Start

```python
from scripts.tone_adjuster import ToneAdjuster

adjuster = ToneAdjuster()

# Academic → Patient-friendly
patient_text = adjuster.convert(
    text="The patient presents with acute myocardial infarction...",
    target_tone="patient-friendly"
)

# Patient-friendly → Academic
academic_text = adjuster.convert(
    text="I had a heart attack...",
    target_tone="academic"
)
```

## Core Capabilities

### 1. Academic to Patient-Friendly

```python
adjuster = ToneAdjuster()
result = adjuster.to_patient_friendly(
    "The patient exhibits tachycardia with irregular rhythm
     consistent with atrial fibrillation",
    reading_level="8th_grade"
)
```

**Conversion Rules:**
- Replace medical terms with common equivalents
- Shorten sentence length (aim for <15 words)
- Use active voice
- Remove unnecessary qualifiers

**Examples:**

| Academic | Patient-Friendly |
|----------|------------------|
| Myocardial infarction | Heart attack |
| Tachycardia | Fast heartbeat |
| Hypertension | High blood pressure |
| Benign prostatic hyperplasia | Enlarged prostate (non-cancerous) |
| Idiopathic | Unknown cause |

### 2. Patient-Friendly to Academic

```python
result = adjuster.to_academic(
    "My stomach hurts after eating spicy food",
    add_citations=True
)
# Output: "The patient reports postprandial abdominal pain
#          exacerbated by capsaicin-containing foods"
```

### 3. Reading Level Assessment

```python
metrics = adjuster.assess_reading_level(text)
print(f"Grade level: {metrics.grade_level}")
print(f"Medical terms: {metrics.jargon_count}")
print(f"Recommendations: {metrics.suggestions}")
```

**Reading Levels:**
- **5th-6th Grade**: Young patients, general public
- **8th Grade**: Most adult patients
- **12th Grade**: Educated lay audiences
- **College**: Healthcare professionals

### 4. Jargon Translation

```python
translations = adjuster.translate_jargon(
    text="Patient presents with dyspnea and orthopnea...",
    show_alternatives=True
)
```

**Common Medical Terms Dictionary:**

```json
{
  "dyspnea": {
    "patient_friendly": "shortness of breath",
    "explanation": "feeling like you can't get enough air"
  },
  "orthopnea": {
    "patient_friendly": "trouble breathing when lying down",
    "explanation": "need to prop up with pillows to breathe"
  }
}
```

## CLI Usage

```bash
# Convert file
python scripts/tone_adjuster.py \
  --input clinical_note.txt \
  --direction academic-to-patient \
  --output patient_handout.txt

# Assess reading level
python scripts/tone_adjuster.py \
  --assess readme.txt \
  --target-grade 8
```

## Best Practices

**When Converting to Patient-Friendly:**
- ✅ Use "you" and "your" when appropriate
- ✅ Define terms in parentheses on first use
- ✅ Use analogies for complex concepts
- ✅ Keep paragraphs to 2-3 sentences

**When Converting to Academic:**
- ✅ Use precise medical terminology
- ✅ Include anatomical locations
- ✅ Specify temporal relationships
- ✅ Add objective measurements

## Common Pitfalls

❌ **Don't**: "Your heart has a problem"
✅ **Do**: "Your heart muscle shows signs of reduced blood flow"

❌ **Don't**: "The medicine might make you feel bad"
✅ **Do**: "This medication may cause nausea, dizziness, or fatigue"

## Quality Checklist

- [ ] Medical accuracy preserved
- [ ] No critical information lost
- [ ] Appropriate reading level achieved
- [ ] Tone matches intended audience
- [ ] All medical terms explained or translated

---

**Skill ID**: 202 | **Version**: 1.0 | **License**: MIT
