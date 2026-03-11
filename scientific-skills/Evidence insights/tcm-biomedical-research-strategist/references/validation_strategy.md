# Validation Strategy Template
# tcm-biomedical-research-strategist

Design multi-level validation. For each level state: *what is validated*, *why it matters*, *how success is judged*.

| Level | What | Why | Success Criterion |
|---|---|---|---|
| Internal validation | Reproducibility within pipeline | Catch pipeline artifacts | Consistent results across parameter ranges |
| Cross-dataset validation | Hub genes in independent GEO cohort | Avoid dataset-specific bias | Same direction, p < 0.05 in ≥ 2 cohorts |
| Biological plausibility | Pathway coherence | Confirm mechanistic logic | Enriched pathways match known disease biology |
| Immune relevance | Correlation of hub genes with immune infiltrates | Link targets to TME | Significant correlation in TIMER2 / TCGA |
| Molecular interaction | Docking binding energy, pose analysis | Support compound–target claims | ΔG < −5 kcal/mol, stable binding pose |
| Experimental validation | Cell viability, Western blot, knockdown | Causal evidence | Dose-dependent effect, rescue experiment |
| Robustness checks | Sensitivity analysis on thresholds | Assess stability of findings | Key findings stable across ±20% cutoff variation |

## Causality Separation Rule

Computational evidence (Steps 1–12) establishes **association and hypothesis**. It does not establish causality.

Causality requires:
- siRNA/shRNA knockdown demonstrating functional dependence
- Rescue experiments restoring the phenotype
- In vivo models confirming the pathway in an animal or organoid context

**Never state that a computational finding "proves" mechanism. Use language: "suggests", "associates", "is consistent with", "warrants experimental validation".**
