---
name: dual-disease-transcriptomic-ml-planner
description: Generates complete dual-disease transcriptomic + machine learning research designs from a user-provided disease pair. Use when users want to identify shared DEGs, common hub genes, cross-disease biomarkers, or shared molecular mechanisms between two diseases using public GEO data. Triggers: "shared biomarker study for two diseases", "dual-disease transcriptomic ML paper", "identify common DEGs between disease A and B", "cross-disease hub gene discovery", "shared DEG + PPI + ROC design", "immune infiltration shared biomarker", or "I want to study disease X and Y together". Always outputs four workload configurations (Lite / Standard / Advanced / Publication+) with a recommended primary plan, step-by-step workflow, figure plan, validation strategy, minimal executable version, and publication upgrade path.
license: MIT
skill-author: AIPOCH
---

# Dual-Disease Transcriptomic Machine Learning Research Planner

Generates a complete dual-disease transcriptomic + ML study design from a user-provided disease pair. Always outputs four workload configurations and a recommended primary plan.

## Supported Study Styles

| Style | Description | Example |
|-------|-------------|---------|
| **A. Shared DEG → Hub Gene Core** | DEG overlap → PPI → hub consensus | Intracranial aneurysm + AAA; diabetic + hypertensive nephropathy |
| **B. Dual-Disease Shared Mechanism** | Pathway-level convergence | ECM, inflammation, fibrosis linking two diseases |
| **C. PPI + Multi-Algorithm Hub Prioritization** | STRING + MCODE + CytoHubba consensus | Any pair with sufficient shared DEGs |
| **D. Dual-Disease Biomarker Validation** | ROC in discovery + validation cohorts | Any pair with ≥2 GEO datasets per disease |
| **E. Immune Infiltration + Shared Biomarker** | CIBERSORT/alternative + gene–immune correlation | Immunologically active disease pairs |
| **F. Single-Gene Cross-Disease Deepening** | Hub-gene GSEA in both diseases | Single top hub with strong AUC |
| **G. Publication-Oriented Integrated Design** | Full pipeline: DEG → PPI → ROC → immune → GSEA | High-impact submission target |

## Minimum User Input

- Two diseases or phenotypes
- If limited detail is provided, infer a reasonable default design and state all assumptions explicitly (Hard Rule 9)

## Step-by-Step Execution

### Step 1: Infer Study Type

Identify:
- Disease pair and biological theme (vascular, autoimmune, fibrotic, metabolic, neurodegenerative, infectious-oncologic, comorbidity)
- User goal: shared biomarkers, shared mechanisms, immune relevance, or publication strength
- Whether ML is central (hub consensus, ROC) or supportive (biological interpretation)
- Whether immune analysis is appropriate — consult Hard Rule 5 and tissue/tool decision guide below
- Resource constraints: public data only, dataset count per disease, time limit, single-gene focus

### Step 2: Output Four Configurations

Always generate all four. For each describe: goal, required data, major modules, expected workload, figure set, strengths, weaknesses.

| Config | Goal | Timeframe | Best For |
|--------|------|-----------|----------|
| **Lite** | Shared DEG + basic hub, 1 dataset per disease | 2–4 weeks | Pilot, skeleton manuscript, single-dataset constraint |
| **Standard** | Full pipeline + validation + ROC + one deepening layer | 5–9 weeks | Core publishable paper |
| **Advanced** | Standard + immune + GSEA + multi-cohort robustness | 9–14 weeks | Competitive journal target |
| **Publication+** | Full multi-layer + experimental suggestions + reviewer defense | 12–20 weeks | High-impact submission |

### Step 3: Recommend One Primary Plan

Select the best-fit configuration and explain why, given disease pair biology, GEO data availability, time constraints, and publication ambition.

### Step 4: Full Step-by-Step Workflow

For each step include: step name, purpose, input, method, key parameters/thresholds, expected output, failure points, alternative approaches.

**Dataset & Preprocessing**
- GEO dataset search: one discovery + one validation per disease when feasible (see [references/geo_search_and_tools.md](references/geo_search_and_tools.md))
- Tissue-only filtering: exclude blood/CSF unless disease-appropriate; match tissue type across both diseases
- **Tissue selection rule**: use the tissue most proximal to disease pathology; for metabolic diseases refer to the tissue/tool decision guide
- Platform compatibility check: verify GPL IDs match or are cross-compatible before merging
- Normalization; batch-awareness without forced merging
- Disease vs control group assignment

**Fault tolerance — dataset level:**
- If no GEO dataset exists for one disease: state infeasibility, suggest the closest available proxy phenotype, downgrade to Lite with discovery-only design
- If only one dataset is available per disease: downgrade to Lite; clearly state validation ROC is not feasible; provide GEO search strategy for a second cohort

**DEG & Shared Signature**
- limma-based DEG analysis (logFC > 1–2, adj.p < 0.05)
- Volcano plots, heatmaps
- Shared up/downregulated DEG intersection (Venn diagram)
- Shared-gene summary table

**Fault tolerance — DEG intersection:**
- If shared DEG count = 0: do not proceed with PPI/hub analysis; apply the following recovery sequence in order:
  1. Relax logFC threshold to 0.5 (report alongside original results)
  2. Extend to top 500 DEGs per disease regardless of threshold
  3. Switch to WGCNA co-expression module overlap instead of direct DEG intersection
  4. Re-evaluate whether the disease pair shares a common tissue or biological mechanism; recommend alternative pairing if not

**Enrichment & Shared Mechanism**
- GO enrichment (BP, MF, CC) + KEGG enrichment (clusterProfiler / DAVID)
- Pathway visualization; shared biological module summarization

**PPI & Hub Prioritization**
- STRING PPI construction (confidence score > 0.4)
- Cytoscape visualization; MCODE dense-cluster identification
- CytoHubba multi-algorithm ranking (≥5 algorithms required: Degree, MCC, Betweenness, Closeness, EPC)
- Hub-gene consensus logic → top 1 / top 3 / top 10 candidates

**Biomarker Performance**
- ROC / AUC analysis (pROC); AUC > 0.70 as minimum threshold
- Discovery-cohort ROC + validation-cohort ROC (Standard and above)
- Expression validation across cohorts

**Fault tolerance — ROC:**
- If AUC ≈ 0.5 in discovery cohort: do not interpret as biomarker; flag as non-informative; consider mini-signature (3–5 genes) instead of single hub gene
- If n < 30 per group: explicitly flag AUC inflation risk; interpret AUC with bootstrap CI; do not generalize

**Immune Infiltration** (when disease-appropriate per Hard Rule 5)
- Deconvolution tool selection — consult [references/tissue_and_tool_decisions.md](references/tissue_and_tool_decisions.md) for the correct tool by tissue type
- Immune-cell proportion comparison (disease vs control); gene–immune cell correlation (Spearman)
- Violin plots, lollipop / heatmap correlation

**Single-Gene Deepening** (Standard and above)
- Stratify samples by hub gene expression (high vs low quartile)
- Single-gene GSEA in both diseases; cross-disease pathway convergence interpretation

### Step 5: Figure Plan

→ Full figure list and table templates: [references/figure_plan_template.md](references/figure_plan_template.md)

Core figures: workflow schematic (Fig 1), DEG volcanos + Venn (Fig 2), shared DEG heatmap (Fig 3), GO/KEGG enrichment (Fig 4), PPI + MCODE + hub ranking (Fig 5), ROC curves (Fig 6), immune infiltration + correlation (Fig 7), single-gene GSEA (Fig 8). Tables: dataset summary, shared DEG list, hub rankings, ROC/AUC summary.

### Step 6: Validation and Robustness Plan

State what each layer proves and what it does not prove:
- **Shared-expression evidence** — DEG overlap + threshold reproducibility
- **Hub-prioritization evidence** — PPI topology + multi-algorithm consensus (association, not causation)
- **Biomarker performance evidence** — ROC/AUC in discovery + validation cohorts (diagnostic signal, not mechanistic proof)
- **Immune support** — immune landscape differences + gene–immune correlation (associative only; Hard Rule 8)
- **Single-gene mechanistic support** — GSEA pathway themes (hypothesis-generating only; Hard Rule 7)

### Step 7: Risk Review

Always include a self-critical section addressing:
- Strongest part of the design
- Most assumption-dependent part (typically: small cohort ROC inflation; platform differences across datasets)
- Most likely false-positive source (hub ranking with few shared DEGs; AUC > 0.9 in n < 50)
- Easiest part to overinterpret (immune deconvolution as causal; one hub gene as mechanistic proof)
- Most likely reviewer criticisms: small cohorts, no experimental validation, platform heterogeneity, overinterpretation of single biomarker, immune deconvolution limitations, CRC/infectious disease subtype heterogeneity
- Revision strategy if first-pass findings fail (broaden DEG threshold, alternate validation cohort, switch to mini-signature)

### Step 8: Minimal Executable Version

Public data only, one discovery dataset per disease, DEG + Venn + GO/KEGG, STRING + MCODE + CytoHubba top gene, ROC in discovery cohort, one-page interpretation. 2–4 week timeline. Confirm feasibility against any stated time or dataset constraints before recommending.

### Step 9: Publication Upgrade Path

→ Full upgrade impact table: [references/upgrade_path.md](references/upgrade_path.md)

Key upgrades by impact: validation cohort per disease (High / Low–Medium), multi-algorithm hub consensus (High / Low), cross-platform reproducibility logic (High / Medium), immune infiltration (Medium / Medium), single-gene GSEA (Medium / Low), mini-signature 3–5 genes (Medium / Medium).

## R Code Framework Guidelines

When providing R code examples or pipeline frameworks:

1. **EXAMPLE ID convention**: All GEO accession numbers in code must carry an inline comment: `# EXAMPLE ID — replace with your actual GSE accession before running`
2. **Zero-intersection guard**: All pipelines must include a feasibility check immediately after DEG intersection:
   ```r
   if (length(shared_genes) == 0) {
     stop("No shared DEGs found. Recovery options: (1) relax logFC to 0.5, (2) use top-500 DEGs per disease, (3) switch to WGCNA co-expression module overlap.")
   }
   ```
3. **Standard package list**: GEOquery, limma, clusterProfiler, org.Hs.eg.db, pROC, igraph, STRINGdb, WGCNA. Provide `BiocManager::install()` calls where needed.
4. **GEO search pattern**: To find valid accession IDs, use `GEOquery::getGEO("GSEsearch", ...)` or direct search at https://www.ncbi.nlm.nih.gov/geo/

**Standard R pipeline template:**

```r
library(GEOquery); library(limma); library(clusterProfiler); library(pROC)

# Load datasets — EXAMPLE IDs: replace before running
gse_disease1 <- getGEO("GSEXXXXX", GSEMatrix = TRUE)[[1]]  # EXAMPLE ID
gse_disease2 <- getGEO("GSEXXXXX", GSEMatrix = TRUE)[[1]]  # EXAMPLE ID

# DEG analysis (repeat for disease2)
design <- model.matrix(~ group, data = pData(gse_disease1))
fit    <- eBayes(lmFit(exprs(gse_disease1), design))
deg_d1 <- subset(topTable(fit, coef = 2, adjust = "BH", number = Inf),
                 abs(logFC) > 1 & adj.P.Val < 0.05)

# Shared DEG intersection with zero-guard
shared_genes <- intersect(rownames(deg_d1), rownames(deg_d2))
if (length(shared_genes) == 0) {
  stop("No shared DEGs found. Recovery: relax logFC to 0.5 or use top-500 DEGs per disease.")
}

# ROC for top hub gene — EXAMPLE: replace 'HUB_GENE' and labels/scores with real data
roc_obj <- roc(response = labels, predictor = expr_scores)
cat("AUC:", auc(roc_obj), "\n")
if (auc(roc_obj) < 0.70) warning("AUC below 0.70 threshold. Consider mini-signature approach.")
```

## Hard Rules

1. Never output only one generic plan — always output all four configurations.
2. Always recommend one primary plan with justification.
3. Always separate necessary modules from optional modules.
4. Distinguish shared-expression evidence, biomarker performance evidence, immune support, and mechanistic support — see Step 6.
5. Do not proceed with immune analysis if the disease pair is not immunologically suited or if deconvolution would be unreliable for the tissue type. Consult [references/tissue_and_tool_decisions.md](references/tissue_and_tool_decisions.md) to select the correct tool.
6. Do not overclaim diagnostic value from ROC in small (n < 30 per group) or unmatched cohorts. Always report bootstrap confidence intervals.
7. Do not overstate one hub gene as mechanistic proof — label consistently as "biomarker candidate."
8. Do not treat immune-correlation evidence as causal immune regulation.
9. If user provides limited detail, infer a reasonable default design and state all assumptions clearly.
10. Do not produce only a flat methods list or literature summary.
11. **Out-of-scope redirect**: If the request involves a single disease only, wet-lab experimental design, clinical trial planning, or non-GEO data types, do not proceed — activate the Input Validation refusal template below.

## Input Validation

This skill accepts: a pair of diseases or phenotypes for which the user wants to identify shared transcriptomic signatures, hub genes, or cross-disease biomarkers using publicly available GEO transcriptomic data.

If the request does not involve two diseases for GEO-based transcriptomic comparison — for example, asking to design a study for a single disease only, plan a wet-lab experiment, design a clinical trial, analyze non-transcriptomic omics data (e.g., proteomics, metabolomics), or conduct a systematic literature review — do not proceed with the planning workflow. Instead respond:
> "Dual-Disease Transcriptomic ML Planner is designed to generate GEO-based transcriptomic + machine learning study designs for pairs of diseases. Your request appears to be outside this scope. Please provide two diseases to compare, or use a more appropriate skill (e.g., a single-disease transcriptomic skill, an MR planner, or a systematic review skill)."

## Reference Files

| File | Content | Used In |
|------|---------|---------|
| [references/tissue_and_tool_decisions.md](references/tissue_and_tool_decisions.md) | Tissue prioritization rules by disease class; immune deconvolution tool selection by tissue type | Step 4 (immune module), Step 1 |
| [references/geo_search_and_tools.md](references/geo_search_and_tools.md) | GEO dataset search strategy by disease class; bioinformatics tool list with alternatives | Step 4 (dataset module) |
| [references/figure_plan_template.md](references/figure_plan_template.md) | Full figure list (Fig 1–8) and table templates (Table 1–4) | Step 5 |
| [references/upgrade_path.md](references/upgrade_path.md) | Publication upgrade impact vs complexity table | Step 9 |
