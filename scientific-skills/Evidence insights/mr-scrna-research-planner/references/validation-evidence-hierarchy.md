# Validation and Evidence Hierarchy
# mr-scrna-research-planner

---

## Evidence Tiers

### Causal-Level Evidence (stronger — label explicitly as causal)

| Evidence | Source | What It Establishes |
|---|---|---|
| IVW MR (p < 0.05, consistent direction) | TwoSampleMR | Association between genetically-proxied exposure and outcome |
| Multivariable MR (independent effect) | MVMR package | Causal effect robust to correlated exposures |
| Colocalization (PP.H4 > 0.75) | coloc R | Same causal variant drives eQTL and GWAS signals — rules out LD confounding |
| SMR + HEIDI (p.HEIDI > 0.05) | SMR software | Gene expression mediates the causal path; rejects pleiotropy |
| Steiger-confirmed direction | TwoSampleMR | Confirms the hypothesized causal direction |

### Correlation-Level Evidence (supportive — label explicitly as associative)

| Evidence | Source | What It Establishes |
|---|---|---|
| DEG between high/low score groups | scRNA FindMarkers | Differential expression — not mechanism |
| Module scoring patterns | AUCell / UCell | Cell-level activity — not causality |
| Pathway enrichment results | clusterProfiler, GSEA | Functional annotation — not mechanism |
| Cell communication inferences | CellChat / NicheNet | Predicted signaling — not confirmed interaction |
| Pseudotime associations | Monocle3 / Slingshot | Trajectory ordering — not temporal causality |
| Bulk expression in independent cohort | GEO / TCGA | Replication of association — not causal replication |

---

## Validation Coverage by Config

| Validation Layer | Lite | Standard | Advanced | Publication+ |
|---|---|---|---|---|
| Within-dataset consistency | ✅ | ✅ | ✅ | ✅ |
| Cross-method MR consistency | — | ✅ | ✅ | ✅ |
| Independent bulk cohort | — | ✅ | ✅ | ✅ |
| Tissue-level expression (GTEx/HPA) | — | ✅ | ✅ | ✅ |
| Second independent scRNA dataset | — | — | ✅ | ✅ |
| Disease subgroup stratification | — | — | ✅ | ✅ |
| Colocalization / SMR | — | — | ✅ | ✅ |
| Multi-ancestry replication | — | — | — | ✅ |
| Independent cohort replication | — | — | — | ✅ |

---

## Article Coverage Matrix

| Pattern | Minimum Required Modules | Recommended Additional |
|---|---|---|
| Mechanism gene set → score → DEG → MR | Scoring, DEG, univariable MR, sensitivity | External validation, pathway, pseudotime |
| Key cell → cell-specific DEG → MR | Cell annotation, composition, DEG, MR | Communication, trajectory, second dataset |
| Candidate genes → MR → scRNA localization | MR (full sensitivity), localization | Pathway, trajectory |
| Exposure → disease → cell | Exposure MR, outcome MR, cell localization | Mediation, colocalization |
| MR-prioritized genes → mechanism | MR results, scRNA DEG, pathway | SCENIC, communication, pseudotime |
| Full sensitivity set | Heterogeneity, pleiotropy, LOO, Steiger | Bidirectional (if biologically justified) |
| External bulk validation | ≥ 1 GEO/TCGA cohort | Second independent cohort |

---

## Self-Critical Risk Review Template

Every output plan must include a risk review covering:

1. **Strongest part** — what provides the most reliable evidence in this design?
2. **Most assumption-dependent part** — what assumption, if wrong, collapses the story?
3. **Most likely false-positive source** — where does spurious signal most easily enter?
4. **Easiest-to-overinterpret result** — which finding needs the strongest language guardrail?
5. **Likely reviewer criticisms** — what will reviewers challenge first?
6. **Fallback plan** — if first-pass MR is null or scRNA signal is weak, what's the alternative design?

---

## Language Rules

- MR findings: "provides causal evidence for", "causally associated with", "genetically predicted"
- Correlation findings: "associated with", "differentially expressed in", "enriched in"
- **NEVER use:** "proves", "demonstrates causality", "confirms the mechanism" for correlation-level evidence
- **ALWAYS state:** which evidence tier each claim belongs to
