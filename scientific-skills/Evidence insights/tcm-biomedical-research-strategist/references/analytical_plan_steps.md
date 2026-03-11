# Analytical Plan — Step Reference
# tcm-biomedical-research-strategist

## 9-Field Template (apply to every step)

| Field | What to provide |
|---|---|
| **Step Name** | Short label |
| **Purpose** | What this step accomplishes in the pipeline |
| **Required Input** | Exact data / files / outputs from prior steps |
| **Proposed Method** | Tool / algorithm + *why this instead of alternatives* |
| **Key Parameters** | Thresholds, cutoffs, decision rules — be specific |
| **Expected Output** | File format + content description |
| **Connects To** | How this output feeds the next step |
| **Failure Points** | What could go wrong; how to detect it |
| **Alternative Method** | Backup tool/approach if primary fails |

---

## 14 Mandatory Steps

### Step 1 — Active Compound Collection & ADME Screening
- Primary source: TCMSP (OB ≥ 30%, DL ≥ 0.18); fallback: HERB, SymMap
- ⚠ **Multi-herb formulas**: deduplicate by InChIKey across all herbs; record herb-of-origin; prioritize compounds in ≥ 2 herbs as core candidates; document threshold conflicts
- ⚠ **Sparse data (<5 compounds)**: escalate to ChEMBL / UNPD / literature mining; relax OB to ≥ 20% with justification; flag downstream uncertainty

### Step 2 — Target Prediction for Screened Compounds
- Primary: Swiss Target Prediction (batch query); Secondary: SEA, SuperPred
- Filter by probability score (≥ 0.1 recommended); record source for each prediction

### Step 3 — Disease Target Collection
- Primary: GeneCards + DisGeNET (`disgenet2r` R package, CURATED evidence)
- Secondary: OMIM, TTD
- Use the disease name exactly as it appears in the database; retain evidence-level annotation

### Step 4 — Compound–Disease Target Intersection
- Tool: R `VennDiagram` or `UpSetR`; or manual `intersect()` on gene symbol lists
- Normalize all gene identifiers to HGNC official symbols before intersection
- Output: candidate target list + Venn/UpSet figure

### Step 5 — PPI Network Construction & Topology Analysis
- Tool: STRINGdb R package (`score_threshold = 400`); Cytoscape for visualization
- Topology metrics: degree, betweenness centrality, closeness centrality via igraph
- Hub definition: degree ≥ median + 1 SD or CytoHubba top-10 by MCC score
- Output: network .cys file + hub gene ranked table

### Step 6 — Transcriptomic Dataset Selection & QC/Preprocessing
- Source: GEO (≥ 30 samples/group preferred); TCGA-COAD/READ (CRC), TCGA-LIHC (HCC), TCGA-LUAD (NSCLC)
- Platform: Illumina RNA-seq (counts) or Affymetrix microarray (RMA-normalized)
- QC: PCA for batch effects; `arrayQualityMetrics` or `FastQC`; remove outlier samples
- Output: normalized expression matrix + QC report

### Step 7 — Differential Expression Analysis (DEG Identification)
- RNA-seq: DESeq2 (`|log2FC| > 1`, `padj < 0.05`)
- Microarray: limma (`|log2FC| > 0.5`, `adj.P.Val < 0.05`)
- Output: DEG table with log2FC, p-value, FDR; volcano plot

### Step 8 — WGCNA Co-expression Network & Module Extraction
- Package: `WGCNA` R
- Soft threshold: choose β where R² ≥ 0.85 (scale-free fit)
- Minimum module size: 30 genes; merge threshold: 0.25
- Trait correlation: Pearson/Spearman between module eigengenes and disease trait
- Output: module–trait heatmap; gene lists per module

### Step 9 — Candidate Target Prioritization
- Intersect: PPI hub genes ∩ DEGs ∩ WGCNA trait-correlated module genes
- Rank by: number of evidence layers hit (1 layer → 3 layers)
- Output: prioritized candidate target list with evidence annotations

### Step 10 — GO / KEGG Enrichment
- Package: `clusterProfiler` R; background: all expressed genes in dataset
- GO thresholds: p.adjust < 0.05, q-value < 0.2
- KEGG thresholds: p.adjust < 0.05
- Visualization: dot plot (top 20 terms per category)
- Output: enrichment tables + dot plots

### Step 11 — ML-Based Hub Gene Ranking
- Methods (run ≥ 2 and take consensus): LASSO (`glmnet`), Random Forest (`randomForest` importance), SVM-RFE (`e1071`)
- Validation: 5-fold cross-validation; AUC on held-out set
- Output: ML feature importance ranking + AUC curves

### Step 12 — Immune Infiltration Analysis
- Primary: CIBERSORT via TIMER2.0 web (LM22 signature)
- Alternative: ssGSEA via `GSVA` package
- Analysis: Spearman correlation between hub gene expression and immune cell fraction
- ⚠ **Single-cell extension**: if scRNA-seq available via TISCH2, validate deconvolution at cell-type resolution using AUCell module scores
- Output: immune fraction heatmap + correlation matrix

### Step 13 — Molecular Docking
- Target preparation: retrieve PDB or AlphaFold structure; remove water/ligands; add hydrogens
- Ligand preparation: PubChem SDF → Open Babel → .pdbqt
- Docking: AutoDock Vina; define grid box on known binding domain or blind-dock
- Acceptance threshold: ΔG < −5 kcal/mol; inspect top pose in PyMOL
- Output: docking score table (compound, target, ΔG, key interacting residues)

### Step 14 — External Validation + Experimental Follow-up Design
- Cross-dataset: validate hub gene expression direction in ≥ 1 independent GEO cohort
- Experimental suggestions: cell viability (MTT/CCK8), Western blot for hub protein, siRNA knockdown + rescue
- Output: cross-cohort validation table + experimental design proposal
