---
name: personal-statement
description: Use when writing medical school personal statements, residency application essays, fellowship statements, or graduate school admissions essays. Crafts compelling narratives highlighting clinical experiences, research achievements, and career motivations for healthcare education applications.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Personal Statement Writer for Medical Education

Craft compelling personal statements for medical school, residency, fellowship, and graduate school applications in healthcare fields.

## Quick Start

```python
from scripts.personal_statement_writer import PersonalStatementWriter

writer = PersonalStatementWriter()

# Generate personal statement
statement = writer.write(
    program_type="medical_school",
    key_experiences=["Shadowing Dr. Smith", "Volunteer at free clinic", "Research on diabetes"],
    motivation="Helping underserved communities",
    character_limit=5300
)
```

## Core Capabilities

### 1. Structure Generation

```python
outline = writer.create_outline(
    program="residency_surgery",
    themes=["Leadership", "Technical skill", "Patient advocacy"]
)
```

**Standard Structure:**
1. **Opening Hook** (10-15%) - Captivating patient story or defining moment
2. **Clinical Experiences** (30-40%) - Specific patient encounters with reflection
3. **Research/Academic** (20-25%) - Scholarly contributions and intellectual curiosity
4. **Service/Leadership** (15-20%) - Community impact and teamwork
5. **Career Goals** (10-15%) - Clear vision for future practice

### 2. Experience Framing

```python
framed = writer.frame_experience(
    experience="Volunteered at homeless shelter",
    angle="patient_advocacy",
    program_type="family_medicine"
)
```

**STAR Method for Experiences:**
- **S**ituation: Brief context
- **T**ask: Your responsibility
- **A**ction: Specific steps you took
- **R**esult: Measurable outcome + personal reflection

### 3. Character Optimization

```python
optimized = writer.optimize_length(
    draft_statement,
    target_chars=5300,  # AMCAS limit
    min_chars=4500
)
```

**Character Limits by Program:**
| Program | Character Limit | Word Approx |
|---------|----------------|-------------|
| AMCAS (Medical School) | 5,300 | ~750 words |
| ERAS (Residency) | Varies by specialty | ~800 words |
| Fellowship | Usually 1-2 pages | ~1000 words |
| Graduate School | Varies | ~500-1000 words |

### 4. Tone Adjustment

```python
adjusted = writer.adjust_tone(
    statement,
    tone="confident_but_humble",
    avoid_cliches=True
)
```

## Common Patterns

See `references/personal-statement-examples.md` for:
- Medical School (MD/DO) Examples
- Residency Personal Statements by Specialty
- Fellowship Application Essays
- Re-applicant Strategies
- Career Changer Narratives

## Quality Checklist

**Before Writing:**
- [ ] List 3 defining patient experiences
- [ ] Identify unique aspects of your journey
- [ ] Research specific program values

**After Writing:**
- [ ] No clichés ("I want to help people", "Since I was young...")
- [ ] Specific examples throughout
- [ ] Personal reflection on every experience
- [ ] Clear connection to chosen specialty
- [ ] Within character limits
- [ ] Proofread for errors

## Common Pitfalls

❌ **Avoid**: "I have always wanted to be a doctor since childhood"
✅ **Instead**: "My decision to pursue medicine crystallized when..."

❌ **Avoid**: Listing achievements without reflection
✅ **Instead**: "This experience taught me..." + specific insight

---

**Skill ID**: 203 | **Version**: 1.0 | **License**: MIT
