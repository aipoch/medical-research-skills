# Milestones and Deliverables
# tcm-biomedical-research-strategist — Section 7 Reference

---

## Execution Timeline

| Period | Tasks | Deliverable |
|---|---|---|
| **Week 1–2** | Compound collection, ADME screening, target prediction, disease gene retrieval, target intersection | Compound table (ADME), target mapping table, intersection list, Venn figure |
| **Week 3–4** | PPI construction, GEO dataset download + QC, DEG analysis, WGCNA | PPI network figure, DEG table, WGCNA module–trait heatmap |
| **Month 2** | ML hub gene ranking, GO/KEGG enrichment, immune infiltration analysis, molecular docking | Hub gene ranked list, enrichment dot plots, immune correlation matrix, docking score table |
| **Month 3** | Cross-dataset validation, experimental follow-up design, manuscript preparation | Cross-cohort validation table, experimental design proposal, full manuscript draft |

---

## Intermediate Deliverables Checklist

Use this as a gate-check before moving to the next phase.

**Phase 1 — Data Collection**
- [ ] Screened active compound table (with OB, DL, MW, LogP values)
- [ ] Compound–target mapping table (with prediction source + score)
- [ ] Disease target list (with database source + evidence level)
- [ ] Venn / UpSet intersection figure
- [ ] Candidate target list (intersection output)

**Phase 2 — Transcriptomics**
- [ ] GEO dataset QC report (PCA, outlier removal log)
- [ ] Normalized expression matrix
- [ ] DEG table (gene, log2FC, p-value, FDR, direction)
- [ ] Volcano plot
- [ ] WGCNA soft-threshold power plot
- [ ] WGCNA module–trait correlation heatmap
- [ ] Trait-associated module gene list

**Phase 3 — Network & Enrichment**
- [ ] PPI network (Cytoscape .cys file or high-res figure)
- [ ] Hub gene candidate list (ranked by centrality / CytoHubba MCC)
- [ ] Candidate target ranked list (multi-evidence layer)
- [ ] GO enrichment table + dot plot
- [ ] KEGG enrichment table + dot plot

**Phase 4 — ML & Immune**
- [ ] ML feature importance ranking (≥ 2 methods)
- [ ] Cross-validation AUC curves
- [ ] Final hub gene list (consensus across ML methods)
- [ ] Immune infiltration fraction heatmap
- [ ] Hub gene × immune cell Spearman correlation matrix

**Phase 5 — Docking & Validation**
- [ ] Molecular docking table (compound, target, ΔG, key residues)
- [ ] Top docking pose figures (PyMOL)
- [ ] Cross-dataset validation table (hub genes in ≥ 1 independent GEO cohort)
- [ ] Final prioritized compound–target pair summary table
