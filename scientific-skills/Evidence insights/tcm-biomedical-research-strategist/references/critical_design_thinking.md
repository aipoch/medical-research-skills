# Critical Design Thinking
# tcm-biomedical-research-strategist — Section 9 Reference

---

## 9a. Standard Risk Review

Answer all 6 questions. Be specific to the study at hand — no generic answers.

1. **Strongest part** of the proposed design — and why it provides the most reliable evidence.
2. **Weakest / most assumption-dependent part** — name the assumption and what happens if it fails.
3. **Step most likely to generate false positives** — and what mitigation is built in.
4. **Result most easily overinterpreted** — and the exact language guardrail to prevent it.
5. **Top 3 reasons this specific study could fail** — not generic bioinformatics caveats, but reasons specific to this herb, disease, and dataset combination.
6. **Redesign plan if first-pass results are negative or inconsistent** — what would you change and why?

---

## 9b. Challenge the Conventional Workflow

> *Do not assume the standard network pharmacology pipeline is optimal. If a better design exists, propose it.*

Answer all 3:
1. **Why your version is stronger** than the standard intersection-based NP workflow.
2. **What bias or weakness** in the conventional workflow you are specifically trying to avoid.
3. **What additional evidence** your design generates that the standard approach would miss.

---

## Common Weaknesses to Challenge

Use these as a checklist — address each one that applies to the current study:

| Weakness | Standard Approach Problem | Potential Improvement |
|---|---|---|
| OB/DL thresholds | Empirical cutoffs not validated for all plant families | Report sensitivity at ±10% threshold; consider structure-activity filters |
| Intersection target selection | Ignores target confidence weighting; treats all sources equally | Weight by evidence score (STRINGdb combined score, DisGeNET score) |
| PPI hub centrality | Degree centrality ≠ therapeutic relevance; housekeeping genes score high | Supplement with functional enrichment; require DEG overlap as second criterion |
| Bulk RNA immune deconvolution | Known cell-type resolution limits; noisy for low-infiltrate tumors | Validate with scRNA-seq (TISCH2) or TIDE immune exclusion scores |
| Static molecular docking | ΔG is binding affinity estimate only; no dynamic stability | Note limitation explicitly; propose MD simulation as future validation step |
| Single-dataset transcriptomics | Cohort-specific artifacts inflate significance | Require ≥ 2 independent GEO cohorts for hub gene validation |
| Correlation framed as mechanism | Most common overinterpretation error in NP papers | Explicitly label all computational findings as "association" not "causality" |
