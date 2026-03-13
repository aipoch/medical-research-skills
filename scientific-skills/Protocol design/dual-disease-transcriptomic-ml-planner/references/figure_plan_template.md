# Figure Plan Template — Dual-Disease Transcriptomic ML Study

> Use during Step 5 to communicate the complete figure and table deliverable set to the user.
> Adapt by configuration: Lite = Figs 1–5 + Tables 1–3; Standard adds Fig 6; Advanced adds Figs 7–8; Publication+ adds supplementary figures.

---

## Core Figures

| Figure | Title | Content | Config |
|--------|-------|---------|--------|
| **Fig 1** | Overall Workflow Schematic | Study design flowchart: data source → DEG → PPI → ROC → immune → GSEA | All |
| **Fig 2** | DEG Landscape | Volcano plots for Disease 1 and Disease 2 (side by side); Venn diagram of shared DEGs | All |
| **Fig 3** | Shared DEG Heatmap | Expression heatmap of shared DEGs across disease and control samples (both diseases) | All |
| **Fig 4** | Enrichment Analysis | GO bubble plots (BP, MF, CC) + KEGG bar charts; shared pathway summary | All |
| **Fig 5** | PPI Network and Hub Gene Identification | STRING PPI network; MCODE module highlight; CytoHubba ranking heatmap (algorithms × genes) | All |
| **Fig 6** | Biomarker Performance (ROC) | ROC curves for top hub gene in discovery cohort (Disease 1 + Disease 2); validation cohort ROC | Standard+ |
| **Fig 7** | Immune Infiltration and Gene–Immune Correlation | Immune cell proportion violin plots (disease vs control); Spearman correlation lollipop or heatmap | Advanced+ |
| **Fig 8** | Single-Gene GSEA | GSEA enrichment plots for top hub gene in Disease 1 and Disease 2 (high vs low expression strata) | Advanced+ |

---

## Supplementary Figures (Publication+)

| Supplement | Content |
|---|---|
| **Suppl. Fig 1** | Validation dataset DEG volcano plots |
| **Suppl. Fig 2** | Cross-platform reproducibility (if multiple array platforms used) |
| **Suppl. Fig 3** | Mini-signature ROC (if 3–5 gene panel used instead of single gene) |
| **Suppl. Fig 4** | Immune deconvolution algorithm comparison (if multiple tools run) |

---

## Tables

| Table | Title | Content |
|-------|-------|---------|
| **Table 1** | Dataset Summary | GEO accession, disease, tissue, platform (GPL), sample count (disease/control), normalization method |
| **Table 2** | Shared DEG List | Gene symbol, logFC in Disease 1, logFC in Disease 2, adj.p in both, direction (up/down) |
| **Table 3** | Hub Gene Rankings | Gene, Degree, MCC, Betweenness, Closeness, EPC scores, consensus rank |
| **Table 4** | ROC / AUC Summary | Gene, cohort (discovery/validation), disease, AUC, 95% CI, sensitivity, specificity at optimal cutoff |

---

## Figure Production Notes

- All figures should use a consistent color palette (e.g., red = upregulated / disease-high; blue = downregulated / disease-low)
- DEG volcano plots: label top 10 upregulated and top 10 downregulated genes by |logFC|
- Venn diagram: use ggVennDiagram or VennDiagram R package
- ROC curves: include 95% confidence bands (bootstrap, n=1000); annotate AUC with CI
- Immune violin plots: overlay individual data points; include Wilcoxon p-values
- GSEA plots: show NES, p-value, and FDR q-value in plot annotation
- All figures should be exported at ≥ 300 DPI for journal submission
