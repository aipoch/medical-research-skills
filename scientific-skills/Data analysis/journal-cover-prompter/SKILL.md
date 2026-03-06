---
name: journal-cover-prompter
description: Use when creating journal cover images, generating scientific artwork prompts, or designing graphical abstracts. Creates detailed prompts for AI image generators to produce publication-quality scientific visuals.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Journal Cover Image Prompter

Generate detailed prompts for creating scientific journal cover images and graphical abstracts using AI image generators.

## Quick Start

```python
from scripts.cover_prompter import CoverPrompter

prompter = CoverPrompter()

# Generate prompt
prompt = prompter.create_prompt(
    research_topic="CRISPR gene editing",
    visual_style="photorealistic",
    mood="hopeful",
    key_elements=["DNA strands", "molecular scissors", "cells"]
)
```

## Core Capabilities

### 1. Prompt Generation

```python
prompt = prompter.generate(
    subject="cancer immunotherapy",
    style="scientific illustration",
    color_scheme="blue_gradient",
    complexity="high"
)
```

**Prompt Structure:**
- Subject description
- Artistic style
- Color palette
- Lighting and mood
- Technical specifications

### 2. Style Selection

```python
style_guide = prompter.select_style(
    journal_type="nature",
    subject_matter="molecular_biology"
)
```

**Journal Styles:**
- Nature: Dramatic, artistic
- Cell: Clean, molecular focus
- Science: Conceptual, broad appeal
- Medical journals: Clinical, professional

### 3. Technical Specs

```python
specs = prompter.get_specs(
    journal="Nature",
    cover_type="front"
)
# Returns dimensions, resolution, color mode
```

## CLI Usage

```bash
python scripts/cover_prompter.py \
  --topic "neuroscience synaptic transmission" \
  --style artistic \
  --output prompt.txt
```

---

**Skill ID**: 211 | **Version**: 1.0 | **License**: MIT
