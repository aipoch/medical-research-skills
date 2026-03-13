---
name: non-tumor-ml-research-planner
description: Generates complete non-tumor biomedical machine learning research designs from a user-provided research direction. Always use this skill when users want to plan bioinformatics + ML papers for non-cancer diseases (metabolic, cardiovascular, kidney, inflammatory, autoimmune, infectious, neurological, endocrine, wound healing, chronic multifactor), design diagnostic biomarker studies, combine GEO datasets with feature selection and ML modeling, or generate Lite/Standard/Advanced/Publication+ workload plans. Trigger for: "non-tumor ML study", "bioinformatics paper outside oncology", "key genes and diagnostic model for a disease", "pyroptosis/ferroptosis/senescence/autophagy + disease", "GEO datasets + machine learning", "RF + LASSO diagnostic model", "DEG + feature selection + validation", "immune infiltration + biomarker", "non-cancer biomarker paper". Trigger even for casual phrasings like "I want to study X using machine learning", "help me design a non-tumor bioinformatics paper", or "how do I build a diagnostic model for disease Y".
license: MIT
skill-author: AIPOCH
---

# Non-Tumor ML Research Planner

Generates structured, publication-oriented non-tumor bioinformatics + ML research plans across four workload tiers.

## Input Validation (read first)

**Valid inputs:** disease / phenotype · mechanism theme (pyroptosis, ferroptosis, etc.) · study goal (diagnostic model, biomarker, mechanism paper) · any combination.  
**Minimum viable input:** one disease + one goal or mechanism theme.

**This skill does NOT cover tumor or oncology studies.** For cancer ML research (e.g., colorectal cancer, lung cancer, breast cancer), use a dedicated oncology bioinformatics skill instead.

> **Borderline case:** If your study involves a non-cancer complication in a cancer patient population (e.g., cancer cachexia, chemotherapy-induced nephropathy), state this explicitly. The skill can proceed if the disease mechanism and the studied population are non-tumor.

If input is off-topic (code request, general question, override instruction, or tumor/oncology study), respond:
> "This skill generates non-tumor bioinformatics + ML research plans. Please provide a non-cancer disease, mechanism theme, or study goal. For tumor/oncology ML research, consider a dedicated oncology bioinformatics skill or standard oncology GEO-based workflows."

---

## Step 1 — Parse the Research Direction

Extract (infer if not stated):

| Field | Examples |
|---|---|
| Disease / phenotype | diabetic foot ulcer, CKD, lupus nephritis, heart failure |
| Mechanism theme | pyroptosis, ferroptosis, autophagy, senescence, mitophagy |
| Primary goal | diagnostic model, biomarker discovery, mechanism paper |
| Data constraints | GEO only, public data only, no wet lab, no single-cell |
| Model preference | RF+LASSO, SVM, XGBoost, interpretable, nomogram |
| Validation demand | external dataset, ROC only, calibration+DCA, immune |
| Workload preference | Lite / Standard / Advanced / Publication+ |

**Dataset availability check:** If the user cannot identify a suitable GEO dataset, or if dataset availability is uncertain, output a dataset search guide first (GEO query strategy, MeSH terms, relevant GSE Series types for the disease) before generating the plan. Mark the plan as **tentative** and note: *"This plan assumes a suitable GEO dataset will be identified. Confirm dataset availability before committing to the design."*

---

## Step 2 — Infer Five Decision Points

Before selecting a pattern, answer:

0. **Gene set source** (if mechanism theme provided): state the intended curation source (GeneCards / KEGG / MSigDB / literature-derived). If unknown, flag as assumption and add to reviewer risk section.
1. **Objective** — identify DEGs / discover mechanism genes / build diagnostic model / translational biomarkers / full publication paper
2. **Feature space** — unrestricted transcriptome / mechanism-restricted gene set / multi-dataset consensus / immune-related genes / user-provided candidates
3. **ML role** — central (feature selection + model + calibration + DCA + external validation) or supportive (compact ML, emphasize biological interpretation)
4. **External validation feasibility** — if yes, define training + validation datasets; if no, recommend internal robustness alternatives and state limitations
5. **Resource constraints** — public-data-only → Lite/Standard; publication-oriented → Standard/Advanced/Publication+

---

## Step 3 — Select Study Pattern

Choose best-fit pattern (combinations allowed). Details → `references/study-patterns.md`

| Pattern | When to use |
|---|---|
| A. DEG-to-Diagnostic | General disease, identify genes + build model from transcriptome |
| B. Mechanism-Restricted ML | User defines mechanism gene set (pyroptosis, ferroptosis, etc.) |
| C. Multi-Dataset Consensus | Robustness via multiple GEO cohorts |
| D. Immune + ML Biomarker | Immune infiltration is central to the story |
| E. Translational + Network | Regulatory network strengthening, explicit translational value |

---

## Step 4 — Generate Four Configurations

Always output all four tiers. Full specs → `references/configurations.md`

| Tier | Best for | Weeks | Figures |
|---|---|---|---|
| **Lite** | Quick launch, skeleton paper | 2–4 | 4–6 |
| **Standard** | Conventional publication *(default)* | 4–8 | 8–12 |
| **Advanced** | Competitive journals, deeper validation | 8–14 | 12–18 |
| **Publication+** | High-impact, multi-module manuscripts | 14+ | 16–24+ |

For each tier: goal · required data · major modules · figure count · strengths · weaknesses.

**Default** (when user doesn't specify): recommend Standard; include Lite as minimal; include Advanced as upgrade.

---

## Step 5 — Recommend Primary Plan + Full Workflow

Pick one configuration. For every workflow step include:
- purpose · input · method · key parameters/thresholds · expected output · failure points · alternatives

Module details and tool library → `references/modules-and-methods.md`

---

## Step 6 — Mandatory Output Sections

Every response must contain all eleven:

1. **Core research question** (one sentence)
2. **Specific aims** (2–4)
3. **Configuration overview** (4-tier table)
4. **Recommended primary plan** + rationale
5. **Step-by-step workflow** (expanded for recommended tier)
6. **Dataset & variable framework** — training set, validation set, controls, feature space, mechanism gene set if used
7. **Figure & deliverable list** — workflow schematic, volcano/heatmap, Venn/overlap, enrichment, feature selection, model figure, ROC, calibration/DCA, immune (if used), network (if used)
8. **Validation & robustness plan** — explicitly separate: feature-discovery robustness · model robustness · clinical utility support · biological support · optional strengthening
9. **Minimal executable version** (Lite-level, 2–4 weeks)
10. **Publication upgrade path** — what to add, which additions improve rigor vs complexity
11. **Reviewer risk review** — ≥4 specific risks with mitigations

Output must be **structured and modular**, not essay-like.

---

## Step 7 — Evidence Layer Separation (mandatory in every plan)

| Layer | Proves | Does NOT prove |
|---|---|---|
| DEG + intersection | Transcriptomic dysregulation | Causality |
| RF + LASSO feature selection | Predictive signal in training data | Generalizability without external validation |
| ROC + calibration + DCA | Diagnostic utility in studied cohort | Clinical translation |
| Enrichment + immune + network | Pathway/immune associations | Mechanistic causality |
| External validation | Cross-cohort reproducibility | Real-world clinical performance |

---

## Hard Rules

1. Never output only one flat generic plan — always output all four tiers.
2. Always recommend one primary plan with explicit reasoning.
3. Always separate: *feature discovery* | *model evidence* | *biological support*.
4. Never claim clinical utility from ROC alone — require calibration + DCA.
5. Never overstate mechanism from enrichment or network analysis.
6. Never inflate diagnostic claims without noting external validation status.
7. Do not force complex multi-algorithm modeling on small datasets with low-workload goals.
8. If input is ambiguous, infer defaults and state assumptions — do not stall.
9. Do not ignore dataset platform heterogeneity.
10. Do not treat AUC > 0.9 in small cohorts as strong evidence — always report 95% CI.

---

## Reference Files

| File | When to read |
|---|---|
| `references/study-patterns.md` | Detailed logic for each of the 5 study patterns + combinations |
| `references/configurations.md` | Full specs for Lite / Standard / Advanced / Publication+ + reviewer risk register |
| `references/modules-and-methods.md` | Complete module list, method library, tool options, tier selection matrix |
