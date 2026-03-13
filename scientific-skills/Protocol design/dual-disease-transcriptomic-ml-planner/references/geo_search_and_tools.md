# GEO Dataset Search Strategy and Bioinformatics Tool Reference

> Last verified: March 2026
> Use during Step 4 (Dataset & Preprocessing module) to identify suitable GEO datasets and verify tool availability.

---

## Part 1: GEO Dataset Search Strategy by Disease Class

### General Search Approach

1. Go to https://www.ncbi.nlm.nih.gov/geo/
2. Search: `"[disease name]" AND "Homo sapiens" AND "[tissue type]"`
3. Filter: DataSet Type = Expression profiling by array OR Expression profiling by high throughput sequencing
4. Sort by: Relevance or Sample Count (prefer n ≥ 20 per group)
5. Check GPL platform: prefer GPL570 (Affymetrix HG-U133 Plus 2.0) or GPL96 (HG-U133A) for microarray; prefer Illumina HiSeq for RNA-seq

### Minimum Dataset Requirements

| Configuration | Datasets per Disease | Minimum n per Group |
|---|---|---|
| Lite | 1 (discovery only) | ≥ 10 |
| Standard | 2 (discovery + validation) | ≥ 15 discovery, ≥ 10 validation |
| Advanced | 2–3 | ≥ 20 per group preferred |
| Publication+ | 3+ or cross-platform | ≥ 25 preferred; external replication encouraged |

### Platform Compatibility Rules

| Scenario | Action |
|---|---|
| Both datasets on same GPL | Direct merge after normalization |
| GPL570 + GPL96 | Subset to common probes; note probe coverage loss |
| Microarray + RNA-seq | Do NOT merge; analyze separately and compare DEG lists |
| Different species | Do NOT merge; use ortholog mapping only for supplementary analysis |

---

## Part 2: Recommended GEO Datasets by Disease Class (Examples)

> These are illustrative examples only. Always verify dataset suitability (tissue type, disease definition, control group) before use. Accession numbers may be superseded by newer datasets.

| Disease | Example GEO Accessions | Tissue | Platform |
|---|---|---|---|
| Intracranial aneurysm | GSE75436, GSE57691, GSE26979 | Arterial wall | GPL570, GPL96 |
| Abdominal aortic aneurysm | GSE57492, GSE47472, GSE98278 | Aortic tissue | GPL570, GPL6244 |
| Atherosclerosis / CAD | GSE20129, GSE34822, GSE43292 | Arterial plaque | GPL570 |
| Type 2 diabetes | GSE23343, GSE25724, GSE41762 | Adipose / islet | GPL570, GPL96 |
| NAFLD / NASH | GSE48452, GSE89632, GSE126848 | Liver biopsy | GPL570, GPL6244 |
| SLE | GSE72326, GSE49454, GSE81622 | PBMC / blood | GPL570, GPL6244 |
| Rheumatoid arthritis | GSE55235, GSE77298, GSE45291 | Synovial tissue | GPL570, GPL96 |
| Alzheimer's disease | GSE5281, GSE48350, GSE122063 | Brain (hippocampus/cortex) | GPL570, GPL96 |
| Parkinson's disease | GSE7621, GSE20163, GSE49036 | Substantia nigra / brain | GPL570, GPL96 |
| Colorectal cancer | GSE44076, GSE21510, GSE39582 | Colon tissue | GPL570, GPL6244 |
| C. difficile infection | GSE45301, GSE50190 | Colonic mucosa | GPL570 |
| IPF | GSE24206, GSE32537, GSE47460 | Lung tissue | GPL570 |
| CKD / diabetic nephropathy | GSE30528, GSE96804 | Kidney biopsy | GPL570 |
| Heart failure | GSE57338, GSE76701 | Cardiac tissue | GPL570 |

---

## Part 3: Bioinformatics Tool Reference

### Core Pipeline Tools

| Stage | Primary Tool | R Package / Access | Alternative |
|---|---|---|---|
| Data retrieval | GEOquery | `BiocManager::install("GEOquery")` | GEO2R (web interface) |
| Normalization (microarray) | limma / affy | `BiocManager::install("limma")` | RMA (affy package) |
| DEG analysis | limma | `BiocManager::install("limma")` | DESeq2 (RNA-seq) |
| GO/KEGG enrichment | clusterProfiler | `BiocManager::install("clusterProfiler")` | DAVID (web), enrichR |
| Pathway visualization | ggplot2 + clusterProfiler | CRAN | pathview |
| PPI construction | STRINGdb | `install.packages("STRINGdb")` | STRING web interface |
| Network visualization | Cytoscape | Desktop app (cytoscape.org) | igraph (R) |
| Hub module detection | MCODE | Cytoscape plugin | CluePedia |
| Hub gene ranking | CytoHubba | Cytoscape plugin (≥5 algorithms) | NetworkAnalyzer |
| ROC / AUC | pROC | `install.packages("pROC")` | ROCR |
| GSEA | clusterProfiler (GSEA function) | `BiocManager::install("clusterProfiler")` | fgsea |
| Co-expression | WGCNA | `install.packages("WGCNA")` | CEMiTool |
| Batch correction | ComBat (sva) | `BiocManager::install("sva")` | limma::removeBatchEffect |

### CytoHubba Algorithm Reference (≥5 Required)

| Algorithm | Measures | Strengths |
|---|---|---|
| Degree | Number of direct connections | Simple; captures highly connected nodes |
| MCC (Maximum Clique Centrality) | Clique-based centrality | Best for hub identification; preferred primary |
| Betweenness Centrality | Shortest paths through node | Identifies bottleneck/bridge nodes |
| Closeness Centrality | Average distance to all nodes | Captures globally central nodes |
| EPC (Edge Percolated Component) | Percolation-based robustness | Robust to network noise |
| Stress Centrality | Sum of shortest paths | Complementary to Betweenness |
| Radiality | Reachability weighted by distance | Captures peripheral connectivity |

**Minimum required**: Degree + MCC + Betweenness + Closeness + EPC (5 algorithms). Report consensus top genes across all applied algorithms.

---

## Part 4: GEO Data Quality Checklist

Before committing a dataset to the analysis, verify:

- [ ] Sample size: ≥ 10 per group for discovery; ≥ 10 for validation
- [ ] Disease definition: clinical diagnosis or pathological confirmation stated in Series description
- [ ] Control group: healthy controls or adjacent normal (not disease-adjacent tissue unless justified)
- [ ] Tissue type: matches intended tissue for this disease class
- [ ] Platform: GPL ID recorded; cross-dataset platform compatibility confirmed
- [ ] Availability: expression matrix downloadable (not raw FASTQ only)
- [ ] No obvious batch confound: check if all cases from one center and all controls from another
