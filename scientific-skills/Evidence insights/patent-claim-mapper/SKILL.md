---
name: patent-claim-mapper
description: Use when mapping patent claims to products, analyzing patent infringement, or preparing freedom-to-operate analyses. Compares patent claims against product features for biotech and pharmaceutical IP assessment.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Patent Claim Mapper

Map patent claims to product features for infringement analysis, freedom-to-operate assessments, and competitive intelligence in biotech/pharma.

## Quick Start

```python
from scripts.claim_mapper import ClaimMapper

mapper = ClaimMapper()

# Map claims to product
mapping = mapper.analyze(
    patent_claims="patent_claims.txt",
    product_description="product_spec.txt"
)
```

## Core Capabilities

### 1. Claim Parsing

```python
claims = mapper.parse_claims(
    patent_file="US10123456B2.pdf",
    independent_only=False
)
```

### 2. Feature Mapping

```python
mapping = mapper.map_to_product(
    claim="A monoclonal antibody that binds to PD-1...",
    product_features=product_specs
)
```

**Mapping Results:**
- **Fully covered**: Product implements claim
- **Partially covered**: Some elements present
- **Not covered**: Claim element missing
- **Questionable**: Requires legal review

### 3. Gap Analysis

```python
gaps = mapper.identify_gaps(
    mapping_results,
    strategy="design_around"
)
```

## CLI Usage

```bash
python scripts/claim_mapper.py \
  --patent US10123456B2 \
  --product product_spec.txt \
  --output mapping_report.pdf
```

---

**Skill ID**: 213 | **Version**: 1.0 | **License**: MIT
