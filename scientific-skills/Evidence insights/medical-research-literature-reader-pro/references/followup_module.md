# Follow-Up Questions Module

This file defines how to generate follow-up questions for Section 14 of the
Mandatory Output Template.

---

## Purpose

Generate 5–10 concrete next questions that help the user think like a researcher,
not a passive reader. Questions must be:
- **Specific** to this paper's design, data, and findings
- **Study-type-aware** (different questions for RCT vs TCGA mining vs cell experiments)
- **Method-aware** (call out the specific method, not just "the analysis")
- **Non-generic** — avoid "what are the limitations?" or "what future research is needed?"

---

## Question Types by Track

### Track A — Clinical / Epidemiology
- Does this paper establish association, prediction, or causation — and what would it take to establish the next level?
- Which confounder, if uncontrolled, would most plausibly reverse or attenuate the effect?
- Would the conclusion hold in key pre-specified subgroups (by age, sex, disease stage, treatment history)?
- Is the effect size large enough to be clinically meaningful, independent of statistical significance?
- What stronger study design would be needed to confirm this finding?

### Track B — Bioinformatics / Computational
- Is the reported signature or biomarker robust when tested on an independent cohort with a different platform?
- Could preprocessing decisions (normalization method, batch correction choice) explain the reported result?
- Is there a risk of feature leakage, and if corrected, would the model performance hold?
- What biological mechanism could explain why these specific genes/features are selected?
- What is the minimal experiment that would confirm the top computational finding in wet lab?

### Track C — Basic Experimental
- Is the proposed mechanism truly closed — is there a rescue experiment that re-establishes the phenotype?
- Do the in vitro findings hold in the in vivo model, and are there systematic discrepancies?
- Are the cell lines or animal models appropriate for translating this finding to human disease?
- What upstream regulator or downstream effector is the most important missing node in the pathway?
- Which key experiment would be most likely to be challenged in peer review, and how would you defend it?

### Track D — Hybrid
- Does the wet-lab validation truly confirm the computational hypothesis, or does it merely confirm expression?
- Is the target selection from computational results systematic and transparent, or is there cherry-picking risk?
- Which single additional experiment would most strengthen the link between the computational discovery and the biological function?
- Could the result be explained by a confounder in the public dataset (batch effect, stage imbalance, platform bias)?
- What would a fully closed evidence chain look like for this paper's central claim?

---

## Generation Rules

1. Always include at least one question that challenges the paper's central claim specifically.
2. Always include at least one question about what evidence would be needed to move from the current level to the next.
3. For hybrid papers, include at least one question about the discovery-to-validation link.
4. Avoid questions that are answerable by reading the paper more carefully — questions should require new experiments, new data, or deeper analysis.
5. Sequence questions from most fundamental to most translational.
