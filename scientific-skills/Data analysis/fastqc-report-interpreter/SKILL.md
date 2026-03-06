---
name: fastqc-report-interpreter
description: Use when analyzing FASTQC quality reports from sequencing data, identifying quality issues in NGS datasets, or troubleshooting sequencing problems. Interprets quality metrics and provides actionable recommendations for RNA-seq, DNA-seq, and ChIP-seq data.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# FASTQC Report Interpreter

Analyze FASTQC quality control reports for Next-Generation Sequencing (NGS) data to assess data quality and identify issues.

## Quick Start

```python
from scripts.fastqc_interpreter import FASTQCInterpreter

interpreter = FASTQCInterpreter()

# Analyze report
analysis = interpreter.analyze("sample_fastqc.html")
print(f"Overall Quality: {analysis.quality_status}")
print(f"Issues Found: {analysis.issues}")
```

## Core Capabilities

### 1. Quality Metrics Analysis

```python
metrics = interpreter.parse_metrics("fastqc_data.txt")
```

**Key Metrics:**
| Metric | Good | Warning | Fail |
|--------|------|---------|------|
| Per base sequence quality | Q > 28 | Q 20-28 | Q < 20 |
| Per sequence quality scores | Peak at Q30 | Peak Q20-30 | Peak < Q20 |
| Per base N content | < 5% | 5-20% | > 20% |
| Sequence duplication | < 20% | 20-50% | > 50% |
| Adapter content | < 5% | 5-10% | > 10% |

### 2. Issue Diagnosis

```python
issues = interpreter.diagnose_issues(metrics)
for issue in issues:
    print(f"{issue.severity}: {issue.description}")
    print(f"Recommendation: {issue.recommendation}")
```

**Common Issues:**

**Low Quality at Read Ends**
- **Cause**: Phasing effects, reagent depletion
- **Solution**: Trim last 10-20 bases

**Adapter Contamination**
- **Cause**: Incomplete adapter removal
- **Solution**: Re-run cutadapt/Trimmomatic with stricter parameters

**High Duplication**
- **Cause**: PCR over-amplification, low input
- **Solution**: Use deduplication; consider library prep optimization

**Per Base Sequence Content Bias**
- **Cause**: Adapter dimers, non-random priming
- **Solution**: Check for adapter contamination; randomize primers

### 3. Batch Analysis

```python
batch_results = interpreter.analyze_batch(
    fastqc_files=["sample1_fastqc.html", "sample2_fastqc.html", ...],
    output_summary="batch_summary.csv"
)
```

### 4. Recommendation Generation

```python
recommendations = interpreter.get_recommendations(
    analysis,
    application="rna_seq",  # or "dna_seq", "chip_seq"
    quality_threshold="high"
)
```

**Application-Specific Thresholds:**
- **RNA-seq**: Acceptable duplication up to 40% (transcript abundance)
- **DNA-seq**: Strict quality requirements (variant calling)
- **ChIP-seq**: Moderate quality, focus on enrichment metrics

## CLI Usage

```bash
# Analyze single report
python scripts/fastqc_interpreter.py --input sample_fastqc.html

# Batch analysis
python scripts/fastqc_interpreter.py --batch "*fastqc.html" --output report.pdf

# With custom thresholds
python scripts/fastqc_interpreter.py --input fastqc.html --application rna_seq
```

## Output Interpretation

**PASS (Green)**: Proceed with analysis
**WARNING (Yellow)**: Review but likely acceptable
**FAIL (Red)**: Requires action before downstream analysis

## Troubleshooting Guide

See `references/troubleshooting.md` for:
- Platform-specific issues (Illumina, PacBio, Oxford Nanopore)
- Library prep problem diagnosis
- Downstream analysis impact assessment

---

**Skill ID**: 205 | **Version**: 1.0 | **License**: MIT
