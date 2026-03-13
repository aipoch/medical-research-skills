# IV Count Benchmarks and Weak-Instrument Risk by Exposure Class

> Use this table during Step 4 (instrument extraction) to set expectations, flag weak-instrument risk, and communicate feasibility to the user.

## How to Use This Reference

1. Identify the exposure class from Step 1.
2. Look up the expected IV count range for that class.
3. Compare against the actual IV count obtained after clumping (p < 5×10⁻⁸, r² < 0.001 / 10,000 kb).
4. Apply the risk flag and adjust the recommended configuration and methods accordingly.

---

## IV Count Benchmarks

| Exposure Class | Typical IV Count (post-clumping) | Weak-Instrument Risk | Recommended Action |
|---|---|---|---|
| **Anthropometric** (BMI, height, waist-hip ratio) | 50–500+ | Very Low | Standard IVW appropriate |
| **Blood lipids** (LDL, HDL, TG, TC) | 50–300+ | Very Low | Standard IVW appropriate |
| **Biomarker — well-powered** (uric acid, CRP, insulin) | 10–100 | Low | Standard IVW appropriate |
| **Biomarker — moderately powered** (most single biomarkers) | 5–30 | Low-Moderate | Check mean F-statistic; note if < 20 |
| **Protein (cis-pQTL)** | 1–10 | Moderate | Use cis-only; check colocalization (PP.H4 > 0.8) |
| **Protein (trans-pQTL)** | Variable | High (pleiotropy) | Use only as supplementary; flag horizontal pleiotropy risk |
| **Metabolite (NMR panel)** | 2–20 per metabolite | Moderate | May need weighted median as primary if < 5 IVs |
| **Gene expression (eQTL)** | 1–5 per gene | Moderate | cis-eQTL preferred; trans-eQTL high pleiotropy risk |
| **Dietary trait** | 2–15 | High | Flag if < 10; state weak-instrument limitation explicitly |
| **Behavioral / Lifestyle** | 3–50 | Moderate-High | Self-report noise amplifies weak IV problem |
| **Sleep phenotypes** | 5–30 (insomnia), 2–10 (duration) | Moderate | Objective actigraphy GWAS preferred |
| **Gut microbiome (taxon-level)** | 1–5 | Very High | Many taxa: 0 genome-wide significant SNPs; flag as exploratory |
| **Psychiatric phenotype** | 10–200 (varies by disorder) | Low-Moderate | PGC GWAS sample sizes growing rapidly; check latest release |
| **Binary disease outcome as exposure** | 5–50 | Moderate | Case-control GWAS; liability-scale effect sizes needed |

---

## F-Statistic Interpretation

The F-statistic for each instrument is: **F = (β/SE)²**

The mean F-statistic across all IVs indicates overall instrument strength:

| Mean F | Interpretation | Action |
|---|---|---|
| > 50 | Strong instruments | Standard analysis |
| 20–50 | Acceptable instruments | Proceed; note in limitations |
| 10–20 | Borderline weak | Add weighted median as primary fallback; report mean F |
| < 10 | Weak instruments | Do not use IVW as primary; use weak-IV-robust methods (LIML, TSLS with robust SE); frame as exploratory |
| < 5 | Severely weak | Do not conduct MR; recommend waiting for larger GWAS |

---

## Weak-Instrument Mitigation Strategies

When IV count is low or F-statistic is borderline:

1. **Lower the p-value threshold** to p < 5×10⁻⁶ (use with caution; increases pleiotropy risk; always report alongside genome-wide threshold results)
2. **Use GSMR** (Genome-wide Summary-data-based MR) which is more efficient with lower IV counts
3. **Report the Weighted Median estimator** as the primary result when N_IVs < 10 (it tolerates up to 50% invalid instruments)
4. **Conduct a power calculation** using mRnd or the TwoSampleMR power function to estimate detectable effect sizes
5. **Frame the study as exploratory** and recommend replication when a better-powered GWAS becomes available

---

## Special Cases

### Bidirectional MR IV Requirements
Both directions require sufficient instruments independently. If exposure A → outcome B has 30 IVs but outcome B → exposure A has only 2 IVs, the reverse direction is not feasible. Report this asymmetry explicitly.

### Multi-Exposure Screening (Panel MR)
- Apply FDR correction (Benjamini-Hochberg) when screening ≥ 5 exposures
- Apply Bonferroni correction if ≥ 10 exposures
- Report both corrected and uncorrected p-values
- For dietary panels: expect most exposures to have < 10 IVs; prioritize exposures with the strongest biological prior

### Protein MR (Proteome-Wide MR)
- Use cis-pQTLs only as primary IVs (within ±1 Mb of the gene)
- Colocalization (PP.H4 > 0.8 using coloc or HyPrColoc) is required before drawing causal conclusions for high-impact publications
- SOMAscan and Olink platforms measure overlapping but non-identical protein sets; specify the platform used
