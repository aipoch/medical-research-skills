---
name: radiology-image-quiz
description: Use when creating radiology educational quizzes, preparing board exam questions, or studying medical imaging cases. Generates interactive quizzes with X-ray, CT, MRI, and ultrasound images for medical education.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Radiology Image Quiz Generator

Create educational quizzes using radiology images (X-ray, CT, MRI, ultrasound) for medical students, residents, and board exam preparation.

## Quick Start

```python
from scripts.radiology_quiz import RadiologyQuiz

quiz = RadiologyQuiz()

# Generate quiz
questions = quiz.generate(
    modality="chest_xray",
    difficulty="intermediate",
    topic="pulmonary_pathology",
    num_questions=10
)
```

## Core Capabilities

### 1. Quiz Generation

```python
quiz = quiz.create(
    images=["case1.png", "case2.png"],
    question_type="multiple_choice",
    include_findings=True,
    include_differential=True
)
```

**Question Types:**
- Multiple choice (single best answer)
- Select all that apply
- Fill in the blank
- Open-ended interpretation

### 2. Case Creation

```python
case = quiz.create_case(
    image_path="ct_scan.png",
    diagnosis="Pulmonary embolism",
    findings=["Filling defect in pulmonary artery", "Right heart strain"],
    clinical_history="Sudden onset dyspnea"
)
```

### 3. Difficulty Calibration

```python
quiz = quiz.set_difficulty(
    level="resident",  # medical_student, resident, fellow, attending
    include_rare_findings=False
)
```

## CLI Usage

```bash
python scripts/radiology_quiz.py \
  --modality ct \
  --topic emergency \
  --num 20 \
  --output quiz.pdf
```

---

**Skill ID**: 212 | **Version**: 1.0 | **License**: MIT
