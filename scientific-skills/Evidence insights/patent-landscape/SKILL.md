---
name: patent-landscape
description: Use when analyzing biotech patent landscapes, identifying white spaces in pharmaceutical IP, tracking competitor patents, or assessing freedom to operate for drug development. Provides comprehensive patent analysis and strategic insights for life sciences innovation.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Biotech Patent Landscape Analyzer

Analyze biotech and pharmaceutical patent landscapes to identify opportunities, assess competition, and guide R&D strategy.

## Quick Start

```python
from scripts.patent_landscape import PatentLandscapeAnalyzer

analyzer = PatentLandscapeAnalyzer()

# Analyze therapeutic area
landscape = analyzer.analyze(
    therapeutic_area="CAR-T cell therapy",
    date_range="2020-2024",
    assignees=["Novartis", "Kite Pharma", "Juno Therapeutics"]
)
```

## Core Capabilities

### 1. Patent Search & Analysis

```python
results = analyzer.search_patents(
    keywords=["CRISPR", "gene editing", "therapeutic"],
    classification="C12N15/113",  # IPC class
    jurisdictions=["US", "EP", "WO"]
)
```

**Search Strategies:**
- **Keyword-based**: Technical terms + synonyms
- **Classification-based**: IPC/CPC codes
- **Citation-based**: Forward/backward citations
- **Assignee-based**: Company portfolios

### 2. White Space Analysis

```python
opportunities = analyzer.identify_white_spaces(
    technology="Antibody-drug conjugates",
    target_diseases=["breast cancer", "lung cancer"],
    existing_claims=landscape
)
```

**White Space Opportunities:**
- Underserved disease indications
- Novel combination therapies
- Alternative delivery mechanisms
- Geographical gaps (emerging markets)

### 3. Competitor Intelligence

```python
competitors = analyzer.analyze_competitors(
    companies=["Pfizer", "Moderna", "BioNTech"],
    focus_area="mRNA vaccines"
)
```

**Competitor Metrics:**
| Metric | Description |
|--------|-------------|
| Portfolio size | Total active patents |
| Filing velocity | Recent filing trends |
| Geographic coverage | Jurisdiction strategy |
| Technology focus | Core vs. peripheral areas |
| Partnership patterns | Collaboration trends |

### 4. Freedom to Operate (FTO) Assessment

```python
fto = analyzer.assess_fto(
    product_concept="Bispecific antibody targeting PD-1 and CTLA-4",
    jurisdictions=["US", "EU", "Japan"]
)
```

**FTO Analysis Steps:**
1. Identify relevant patent claims
2. Map claims to product features
3. Assess validity of blocking patents
4. Design around options
5. Licensing recommendations

## CLI Usage

```bash
# Generate patent landscape report
python scripts/patent_landscape.py \
  --query "immuno-oncology checkpoint inhibitors" \
  --output landscape_report.pdf \
  --format comprehensive

# Quick FTO check
python scripts/patent_landscape.py \
  --fto "product_description.txt" \
  --jurisdictions US EP JP
```

## Data Sources

- USPTO (United States)
- EPO (Europe)
- WIPO (Global)
- JPO (Japan)
- CNIPA (China)

## References

- `references/ipc-classifications.md` - IPC/CPC codes for biotech
- `references/patent-search-strategies.md` - Advanced search techniques
- `examples/landscape-reports/` - Sample reports

---

**Skill ID**: 204 | **Version**: 1.0 | **License**: MIT
