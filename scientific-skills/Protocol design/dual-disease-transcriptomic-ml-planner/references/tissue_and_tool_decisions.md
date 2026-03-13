# Tissue Selection and Immune Deconvolution Tool Decisions

> Last verified: March 2026
> Consult this reference during Step 1 (study type inference) and Step 4 (immune infiltration module).

---

## Part 1: Tissue Selection Rules by Disease Class

Use the tissue **most proximal to disease pathology**. When the research question determines the tissue, that takes precedence.

| Disease Class | Preferred Tissue | Notes |
|---|---|---|
| **Vascular diseases** (aneurysm, atherosclerosis, PAD) | Arterial wall / aortic tissue | Avoid blood unless studying circulating biomarkers specifically |
| **Hepatic / Metabolic** (NAFLD, NASH, cirrhosis) | Liver biopsy tissue | Portal or lobular regions depending on fibrosis focus |
| **Type 2 Diabetes (T2D)** | See sub-rules below | Depends on research question |
| **Autoimmune — joint** (RA, OA, gout) | Synovial tissue | Blood/PBMC secondary if synovial unavailable |
| **Autoimmune — systemic** (SLE, Sjögren's, vasculitis) | PBMC or whole blood | Tissue biopsy (kidney, skin) for organ-specific manifestations |
| **Neurodegenerative** (AD, PD, ALS, HD) | Brain tissue (disease-relevant region) | AD: hippocampus/entorhinal; PD: substantia nigra; use GTEx-compatible GEO sets |
| **Pulmonary** (IPF, COPD, asthma, lung cancer) | Lung tissue / bronchoalveolar lavage | BAL for inflammatory; lung biopsy for fibrotic/malignant |
| **Renal** (CKD, IgA nephropathy, diabetic nephropathy) | Kidney biopsy (cortex preferred) | Avoid urine unless studying urinary biomarkers |
| **Gastrointestinal** (IBD, CRC, CDI) | Colonic mucosal biopsy | Stool or luminal for microbiome-adjacent studies only |
| **Cardiac** (heart failure, myocarditis, cardiomyopathy) | Cardiac muscle / myocardial tissue | Peripheral blood secondary |
| **Oncologic** (any tumor type) | Tumor tissue (matched with adjacent normal) | Specify molecular subtype if relevant (e.g., MSI vs MSS for CRC) |

### T2D Tissue Sub-Rules

| Research Focus | Preferred Tissue |
|---|---|
| Insulin resistance / lipid metabolism | Adipose tissue (subcutaneous or visceral) |
| Hepatic glucose production / lipotoxicity | Liver biopsy |
| Beta-cell dysfunction / insulin secretion | Pancreatic islet tissue (rare GEO data; use GTEx if unavailable) |
| Systemic inflammation | PBMC or whole blood |
| Diabetic nephropathy co-study | Kidney biopsy |

**Decision rule**: State your tissue choice explicitly in the methods section. If selecting liver for T2D, justify with "focus on hepatic insulin resistance and lipotoxicity." If the research question is ambiguous, default to **adipose tissue** (best GEO coverage for T2D metabolic studies) and state the assumption.

---

## Part 2: Immune Deconvolution Tool Selection by Tissue Type

| Tissue Type | Recommended Tool | Rationale | Alternative |
|---|---|---|---|
| **Peripheral blood / PBMC** | CIBERSORT (LM22 matrix) | LM22 designed for hematopoietic cell types | TIMER2.0 (immune estimate module) |
| **Solid tumor (any)** | TIMER2.0 or CIBERSORT-X | TIMER2.0 has tumor-purity correction; CIBERSORT-X allows custom reference | EPIC (with tumor-specific reference) |
| **Brain tissue** | EPIC (with brain cell-type reference) or MuSiC | LM22 is inappropriate for CNS tissue; brain reference matrices required | MuSiC with matched scRNA-seq reference |
| **Liver** | CIBERSORT-X (custom liver signature) or MuSiC | Standard LM22 may miss Kupffer cells; liver-specific signatures recommended | TIMER2.0 (hepatocellular module) |
| **Synovial tissue** | CIBERSORT with custom synovial matrix | Standard LM22 lacks synoviocyte subtypes | TIMER2.0 (if tumor module acceptable as proxy) |
| **Lung tissue** | CIBERSORT-X or EPIC | Good coverage for alveolar macrophages, NK, T cells | TIMER2.0 |
| **Kidney** | CIBERSORT-X or MuSiC | Tubular cell contamination; custom renal reference preferred | EPIC |
| **Cardiac / muscle** | MuSiC with matched scRNA-seq reference | Highly specialized cell types; standard matrices unreliable | EPIC (with custom reference) |
| **Intestinal / colonic mucosa** | CIBERSORT-X or MuSiC | Epithelial contamination; intestinal immune signature matrix recommended | TIMER2.0 |

### How to Apply This Table

1. Identify tissue type from Step 1 dataset selection.
2. Look up recommended tool from table above.
3. If the recommended tool requires a custom matrix and one is unavailable, use the listed alternative and explicitly state the limitation in the methods section.
4. **Never** apply CIBERSORT LM22 directly to brain, synovial, cardiac, or renal tissue without stating that LM22 is designed for hematopoietic cells and results should be interpreted with caution.

### Accessing Tools

| Tool | Access |
|---|---|
| CIBERSORT / CIBERSORT-X | https://cibersortx.stanford.edu (registration required) |
| TIMER2.0 | http://timer.cistrome.org |
| EPIC | Bioconductor package `EPIC` |
| MuSiC | https://github.com/xuranw/MuSiC (R package) |

---

## Part 3: Tissue Matching Across Disease Pairs

When two diseases in a pair require different tissues, follow these rules:

1. **Prefer the tissue shared by both diseases** (e.g., blood/PBMC for two systemic autoimmune diseases).
2. **If tissues are incompatible** (e.g., brain for AD + liver for NAFLD), choose the tissue of the disease with stronger GEO availability, and explicitly state that the cross-tissue comparison limits direct mechanistic interpretation.
3. **Do not mix blood-derived and tissue-derived datasets** in the same DEG analysis without batch correction and a clear statement of the limitation.
4. **Flag cross-tissue studies** in Step 7 Risk Review as a primary reviewer concern.
