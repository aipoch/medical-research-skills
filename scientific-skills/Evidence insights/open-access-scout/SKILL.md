---
name: open-access-scout
description: Use when finding open access journals, checking journal policies, or identifying predatory publishers. Helps researchers locate legitimate open access venues and avoid publication scams.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Open Access Journal Scout

Find legitimate open access journals, verify publisher credibility, and avoid predatory publication traps.

## Quick Start

```python
from scripts.oa_scout import OpenAccessScout

scout = OpenAccessScout()

# Find journals
journals = scout.find_journals(
    subject="oncology",
    impact_range=(2, 5),
    max_apc=2000
)
```

## Core Capabilities

### 1. Journal Search

```python
results = scout.search(
    keywords=["immunotherapy", "cancer"],
    filters={
        "indexed_in": ["PubMed", "Scopus"],
        "peer_review": "double_blind",
        "apc_max": 2500
    }
)
```

### 2. Predatory Check

```python
assessment = scout.assess_journal("Journal of Medical Advances")
print(f"Trust score: {assessment.score}/100")
print(f"Red flags: {assessment.red_flags}")
```

**Warning Signs:**
- No clear editorial board
- Rapid review promises (<2 weeks)
- Excessive APCs (>$3000)
- Not indexed in major databases
- Spam email invitations

### 3. APC Comparison

```python
comparison = scout.compare_apc(
    journals=["Journal A", "Journal B"],
    currency="USD"
)
```

## CLI Usage

```bash
python scripts/oa_scout.py --search "oncology immunotherapy" --max-apc 2000
```

---

**Skill ID**: 210 | **Version**: 1.0 | **License**: MIT
