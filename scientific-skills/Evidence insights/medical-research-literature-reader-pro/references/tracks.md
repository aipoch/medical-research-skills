# Track Analysis Modules

This file contains the complete per-item analysis checklists for all five tracks.
Load the relevant track(s) based on the routing decision in SKILL.md Step 1–2.

---

## Track A: Clinical / Epidemiology

*Activate for: RCT, cohort, case-control, cross-sectional, real-world study, diagnostic study,
prognostic study, clinical ML prediction, systematic review, meta-analysis.*

1. **Clinical question type** — therapy, diagnosis, prognosis, screening, risk prediction, or outcome association?
2. **Study design level** — RCT, cohort, case-control, cross-sectional, real-world, diagnostic, prognostic, SR/meta-analysis?
3. **Population and eligibility appraisal** — are inclusion/exclusion criteria appropriate and clearly reported?
4. **Baseline comparability check** — are groups balanced at baseline? Was randomization adequate (for RCTs)?
5. **Exposure / intervention / comparator clarity** — is the intervention well-defined? Is the comparator appropriate?
6. **Endpoint appraisal** — primary vs secondary endpoints; clinically meaningful vs surrogate endpoints; pre-specified vs post-hoc?
7. **Follow-up and missingness** — duration adequate for the outcome? Loss to follow-up handled appropriately?
8. **Confounding and bias control** — which confounders were adjusted for? Which were not? What biases are present (selection, information, performance)?
9. **Statistical strategy review** — regression approach, survival analysis, subgroup analyses, multiplicity adjustments, causal inference claims
10. **Effect size vs clinical meaning** — statistically significant ≠ clinically important; NNT/NNH where applicable
11. **Safety / adverse event interpretation** — if applicable: were safety endpoints pre-specified? Adequate follow-up for delayed effects?
12. **External validity** — can findings generalize beyond the study population, setting, and time period?
13. **Causality boundary judgment** — what causal language is justified given the design? (RCT supports causation; observational supports association)
14. **Guideline / standard-of-care positioning** — where does this paper sit relative to current practice?
15. **Clinical translation potential** — exploratory, decision-supportive, or practice-changing?
16. **Final Clinical Evidence Rating** — Low / Moderate / High credibility within evidence type, with rationale

---

## Track B: Bioinformatics / Computational

*Activate for: TCGA/GEO/public-database mining, transcriptomics, proteomics, metabolomics,
single-cell, spatial transcriptomics, prognostic signature, biomarker screening, pathway enrichment,
multi-omics, computational disease modeling.*

1. **Data source identification** — TCGA, GEO, ArrayExpress, CPTAC, in-house cohort, scRNA-seq, spatial, etc.
2. **Cohort composition and sample size** — sample size adequate? Training vs validation sizes? Cancer stage and subtype representation?
3. **Preprocessing transparency** — normalization method, filtering thresholds, QC steps, batch correction, missing data handling — all reported?
4. **Differential / feature discovery logic** — how were candidate genes/features selected? Are thresholds justified?
5. **Model construction logic** — which algorithms and pipelines? Why chosen over alternatives?
6. **Overfitting risk** — feature leakage check (was preprocessing nested inside CV?), model instability, small sample / high feature count ratio
7. **Internal validation** — train/test split strategy, cross-validation type and fold count, bootstrap rigor
8. **External validation** — true external validation (independent cohort, different platform) vs resampling-based?
9. **Multi-dataset consistency** — do results replicate across datasets and platforms? Direction consistent?
10. **Biological interpretability** — do computational outputs (hub genes, signature genes, enriched pathways) make biological sense in disease context?
11. **Reproducibility audit** — code availability, GEO/TCGA accession numbers, supplementary parameter tables
12. **Biomarker / signature credibility rating** — considering validation strength, platform generalizability, and clinical context
13. **Mechanistic support check** — is the finding purely associative, or is there biological support (prior literature, pathway plausibility)?
14. **Translational potential** — diagnostic, prognostic, patient stratification, therapeutic target hypothesis, or purely exploratory?
15. **Final Computational Evidence Rating** — Low / Moderate / High credibility, with rationale

---

## Track C: Basic Experimental

*Activate for: cell line experiments, animal models, organoids, PDX, pathway mechanism papers,
target validation, knockdown / knockout / overexpression / CRISPR, inhibitor studies.*

1. **Experimental system identification** — cell lines, primary cells, tissues, organoids, animal model (strain, sex, age), PDX
2. **Mechanistic hypothesis extraction** — what is the proposed mechanism? Is it clearly stated?
3. **Model suitability review** — are the chosen systems appropriate for the biological question?
4. **Control design assessment** — negative controls, positive controls, vehicle controls, rescue controls, sham controls — all present and appropriate?
5. **Intervention and perturbation mapping** — knockdown vs knockout vs overexpression vs inhibitor vs editing; are perturbation efficiencies reported?
6. **Reagent / material reliability** — antibody validation (species, dilution, positive control), cell line identity (STR profiling), assay kit quality, oligo sequence transparency
7. **Replication and sample adequacy** — biological replicates vs technical replicates; n per group; statistical power
8. **Figure-level trust review** — WB loading controls and band quantification, IF/IHC staining specificity, microscopy quantification, flow cytometry gating, migration assay normalization
9. **Phenotype evidence review** — what phenotypes were truly demonstrated? Are effect sizes biologically meaningful?
10. **Mechanism chain completeness** — is the upstream → pathway → downstream → phenotype chain complete, or are there gaps?
11. **In vitro to in vivo connection** — do the in vitro and in vivo findings tell the same story, or are they fragmented?
12. **Rescue / closure loop review** — was the mechanism loop closed with a rescue experiment? What is still open?
13. **Statistical and reporting quality** — appropriate tests, variance reported, multiple comparison correction, pre-specified vs exploratory
14. **Reproducibility readiness** — could another laboratory reasonably reproduce the key experiments?
15. **Final Experimental Evidence Rating** — Low / Moderate / High credibility, with rationale

---

## Track D1: Hybrid — Bioinformatics + Experimental Validation

*Activate when computational discovery AND wet-lab validation are both central to the paper's core claims.*

1. **Discovery-to-validation alignment** — did the wet-lab validation genuinely arise from the computational discovery, or were they developed in parallel?
2. **Candidate selection transparency** — was the target(s) chosen systematically from computational results, or cherry-picked?
3. **Expression validation vs functional validation** — repeating expression patterns in a different model is NOT functional relevance
4. **Functional validation vs mechanistic validation** — demonstrating a phenotype is NOT the same as establishing a full mechanism
5. **Dataset conclusion vs lab conclusion consistency** — do the computational findings and experimental findings point in the same direction and magnitude?
6. **Hypothesis-to-experiment fit** — do the experiments actually answer the computational hypothesis, or do they test a related but different question?
7. **Multi-layer evidence chain rating:**
   - Layer 1 — Discovery (computational): association strength
   - Layer 2 — Expression validation (wet-lab): reproducibility
   - Layer 3 — Functional validation: phenotype evidence
   - Layer 4 — Mechanistic validation: pathway-level proof
   - Layer 5 — Translational bridge: clinical / animal connection
8. **Final Hybrid Credibility Judgment** — overall strength of the combined evidence chain; identify the weakest link

---

## Track D2: Hybrid — Clinical / Epidemiology + Machine Learning

*Activate for: NHANES + ML, EHR prediction models, explainable-AI clinical prediction,
clinical risk score development with ML methods.*

1. **Prediction target validity** — is the outcome clinically coherent, meaningful, and well-defined?
2. **Cohort and label quality** — are labels reliable? Is the outcome objectively measured?
3. **Class imbalance and sampling strategy** — reported? Handled with SMOTE, weighting, or stratified splitting?
4. **Pipeline leakage risk audit** — was preprocessing (normalization, imputation, feature selection) nested correctly inside the validation loop?
5. **Model benchmarking fairness** — were comparator models (logistic regression, decision tree) trained and tuned with the same pipeline?
6. **Validation level** — internal only / temporal holdout / geographic external / true prospective?
7. **Calibration and clinical utility** — calibration curves reported? Decision-curve analysis (DCA) present? Net benefit vs treat-all/treat-none?
8. **Explainability boundary judgment** — SHAP / feature importance reflects model behaviour, NOT biological causation or clinical mechanism
9. **Clinical utility readiness** — exploratory hypothesis / publishable-only / ready for prospective validation / actionable in current form?
10. **Final ML-Clinical Credibility Rating** — Low / Moderate / High, with specific rationale
