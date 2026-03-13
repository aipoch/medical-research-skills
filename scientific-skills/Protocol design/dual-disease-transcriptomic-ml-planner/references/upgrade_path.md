# Publication Upgrade Path — Dual-Disease Transcriptomic ML Study

> Use during Step 9 to guide users from Standard toward Advanced or Publication+ configurations.
> Impact ratings: High / Medium / Low. Complexity ratings: Low / Medium / High.

---

## Upgrade Impact Table

| Addition | Publication Impact | Complexity | Notes |
|----------|-------------------|------------|-------|
| Add validation cohort per disease (→ Standard) | **High** | Low–Medium | Most important upgrade; required by most journals; dramatically reduces AUC inflation concern |
| Multi-algorithm hub consensus (≥5 CytoHubba algorithms) | **High** | Low | Easy to implement; directly addresses reviewer concern about arbitrary hub selection |
| Cross-platform reproducibility logic (different GPL validation) | **High** | Medium | Adds credibility when discovery and validation cohorts use different array generations |
| Add immune infiltration analysis (→ Advanced) | **Medium** | Medium | Disease-appropriate only (Hard Rule 5); adds biological depth; requires correct deconvolution tool |
| Single-gene GSEA (→ Advanced) | **Medium** | Low | Low effort; adds mechanistic narrative; clearly frame as hypothesis-generating |
| Mini-signature (3–5 genes) vs single hub gene | **Medium** | Medium | Improves AUC and robustness; required if single gene AUC < 0.80 in validation |
| Experimental validation suggestion section | **Medium** | Low | Cost-free to write; shows publication awareness; can include in silico alternatives (drug targets, scRNA-seq) |
| scRNA-seq re-analysis or single-cell deconvolution | **High** | High | Strongest upgrade for Publication+; rarely feasible with public data alone |
| Drug target / repurposing analysis for hub genes | **Medium** | Low–Medium | Adds translational value; use DGIdb, DrugBank, or CMap for in silico analysis |

---

## Upgrade Decision Rules

### When to upgrade from Lite → Standard
- Target journal requires external validation (most PubMed-indexed journals)
- Second GEO dataset is available for at least one disease
- AUC in discovery cohort > 0.70 (worth validating)

### When to upgrade from Standard → Advanced
- Disease pair has established immune relevance (autoimmune, inflammatory, oncologic, neurodegenerative with neuroinflammation)
- Second GEO dataset is large enough for immune deconvolution (n ≥ 20 per group)
- Single hub gene shows strong AUC (> 0.80) in validation — GSEA deepening worthwhile

### When to target Publication+
- High-impact journal target (Q1, IF > 5)
- Multiple validation cohorts available (≥ 2 per disease)
- Cross-platform or cross-ancestry reproducibility is achievable
- Drug-target or clinical-translation angle is available

---

## Common Reviewer Demands and Corresponding Upgrades

| Reviewer Concern | Upgrade That Addresses It |
|---|---|
| "AUC was only tested in the discovery cohort" | Add validation cohort ROC (Lite → Standard) |
| "Hub gene selection seems arbitrary" | Multi-algorithm CytoHubba consensus (already in Standard) |
| "Single gene is insufficient as a biomarker" | Mini-signature 3–5 genes |
| "No mechanistic insight provided" | Single-gene GSEA (Standard → Advanced) |
| "Immune analysis uses inappropriate reference matrix" | Correct deconvolution tool per tissue_and_tool_decisions.md |
| "Results may not replicate across platforms" | Cross-platform reproducibility analysis |
| "No experimental validation" | Suggest in silico alternatives: drug target analysis, scRNA-seq re-analysis, existing protein databases |
| "Small sample size limits interpretation" | Acknowledge in limitations; provide bootstrap CI for AUC; recommend future larger cohort validation |
