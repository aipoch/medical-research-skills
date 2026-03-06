---
name: clinical-data-cleaner
description: Use when cleaning clinical trial data, preparing data for FDA/EMA submission, standardizing SDTM datasets, handling missing values in clinical studies, detecting outliers in lab results, or converting raw CRF data to CDISC format. Cleans and standardizes clinical trial data for regulatory compliance with audit trails.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "2.0"
---

# Clinical Data Cleaner

Clean, validate, and standardize clinical trial data to meet CDISC SDTM standards for regulatory submissions to FDA or EMA.

## Quick Start

```python
from scripts.main import ClinicalDataCleaner

# Initialize for Demographics domain
cleaner = ClinicalDataCleaner(domain='DM')

# Clean data with default settings
cleaned = cleaner.clean(raw_data)

# Save with audit trail
cleaner.save_report('output.csv')
```

## Core Capabilities

### 1. SDTM Domain Validation

```python
cleaner = ClinicalDataCleaner(domain='DM')  # or 'LB', 'VS'
is_valid, missing = cleaner.validate_domain(data)
```

**Required Fields:**
- **DM**: STUDYID, USUBJID, SUBJID, RFSTDTC, RFENDTC, SITEID, AGE, SEX, RACE
- **LB**: STUDYID, USUBJID, LBTESTCD, LBCAT, LBORRES, LBORRESU, LBSTRESC, LBDTC
- **VS**: STUDYID, USUBJID, VSTESTCD, VSORRES, VSORRESU, VSSTRESC, VSDTC

### 2. Missing Value Handling

```python
cleaner = ClinicalDataCleaner(
    domain='DM',
    missing_strategy='median'  # mean, median, mode, forward, drop
)
cleaned = cleaner.handle_missing_values(data)
```

### 3. Outlier Detection

```python
cleaner = ClinicalDataCleaner(
    domain='LB',
    outlier_method='domain',  # iqr, zscore, domain
    outlier_action='flag'     # flag, remove, cap
)
flagged = cleaner.detect_outliers(data)
```

**Clinical Thresholds:**
| Parameter | Range | Unit |
|-----------|-------|------|
| Glucose | 50-500 | mg/dL |
| Hemoglobin | 5-20 | g/dL |
| Systolic BP | 70-220 | mmHg |

### 4. Date Standardization

```python
standardized = cleaner.standardize_dates(data)
# Converts to ISO 8601: 2023-01-15T09:30:00
```

### 5. Complete Pipeline

```python
cleaner = ClinicalDataCleaner(
    domain='DM',
    missing_strategy='median',
    outlier_method='iqr',
    outlier_action='flag'
)
cleaned_data = cleaner.clean(data)
cleaner.save_report('output.csv')
```

**Output Files:**
- `output.csv` - Cleaned SDTM data
- `output.report.json` - Audit trail for regulatory submission

## CLI Usage

```bash
# Clean demographics
python scripts/main.py \
  --input dm_raw.csv \
  --domain DM \
  --output dm_clean.csv \
  --missing-strategy median \
  --outlier-method iqr \
  --outlier-action flag

# Clean lab data with clinical thresholds
python scripts/main.py \
  --input lb_raw.csv \
  --domain LB \
  --output lb_clean.csv \
  --outlier-method domain
```

## Common Patterns

See [references/common-patterns.md](references/common-patterns.md) for detailed examples:
- Regulatory Submission Preparation
- Interim Analysis Data Preparation
- Database Migration Cleanup
- External Lab Data Integration

## Troubleshooting

See [references/troubleshooting.md](references/troubleshooting.md) for solutions to:
- Validation failures
- Date parsing errors
- Memory errors with large datasets
- Outlier detection issues

## Quality Checklist

**Pre-Cleaning:**
- [ ] IACUC approval obtained (animal studies)
- [ ] Sample size adequately powered
- [ ] Randomization method documented

**Post-Cleaning:**
- [ ] Validate against CDISC SDTM IG
- [ ] Review all cleaning actions in audit trail
- [ ] Test import to analysis software

## References

- `references/sdtm_ig_guide.md` - CDISC SDTM Implementation Guide
- `references/domain_specs.json` - Domain-specific field requirements
- `references/outlier_thresholds.json` - Clinical outlier thresholds
- `references/common-patterns.md` - Detailed usage patterns
- `references/troubleshooting.md` - Problem-solving guide

---

**Skill ID**: 189 | **Version**: 2.0 | **License**: MIT
