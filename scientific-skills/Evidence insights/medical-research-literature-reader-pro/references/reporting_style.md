# Reporting Style and Interpretation Safety

This file defines writing standards and interpretation safety rules for all outputs.

---

## Writing Standards

**Write with:** precision · medical fluency · analytical sharpness · caution on causal language.

**Tone calibration by mode:**
- Quick Read: concise, direct, accessible
- Standard Structured Report: analytical, precise, evidence-type-aware
- Expert Deep Review: rigorous, critical, research-grade; assume a sophisticated reader

**Avoid in all modes:**
- Vague compliments ("this is an interesting paper", "the authors did a thorough job")
- Generic filler ("more research is needed", "future studies should investigate")
- Hype-driven interpretation that amplifies the paper's own language
- Treating all study types with a single generic summary format
- Implying that statistical significance equals biological or clinical importance

---

## Interpretation Safety Rules

**Never overclaim these specific equivalences:**

| What the paper shows | What it does NOT show |
|---|---|
| Association in observational data | Causation |
| ML model prediction accuracy | Mechanistic explanation |
| SHAP / feature importance ranking | Biological causality or pathway proof |
| Expression validation (qPCR, IHC) | Functional relevance |
| In vitro phenotype | In vivo or clinical relevance |
| Internal cross-validation AUC | Clinical deployment readiness |
| Significant hits in TCGA / GEO | Validated therapeutic targets |
| Bioinformatics analysis alone | Proof of any claim requiring experimental evidence |

---

## Calibrating Evidence Language

Use language that matches the study design's actual causal strength:

| Study Design | Appropriate Language |
|---|---|
| RCT with adequate power and blinding | "caused", "reduced", "prevented" (with appropriate caveats) |
| Prospective cohort | "associated with", "predicted", "was a risk factor for" |
| Retrospective / cross-sectional | "was associated with", "correlated with" |
| Bioinformatics / computational | "was identified as a candidate", "was associated in dataset X", "may play a role" |
| Cell experiment | "affected [phenotype] in [cell type]", "modulated [pathway] in vitro" |
| Animal model | "reduced tumour growth in [mouse model]", "was associated with [phenotype] in vivo" |

---

## Flagging Overclaiming in the Source Paper

If the paper itself uses language that overstates its evidence level, note this explicitly
in Section 8 (What the Paper Cannot Claim):

> "The authors describe their finding as [quote or paraphrase]. Given the study design
> ([design type]), this language overstates the evidence level. The most accurate
> characterization is [corrected statement]."

Common overclaiming patterns to flag:
- "proved" / "demonstrated" used for correlational or computational findings
- "the mechanism is" stated from a single-pathway experiment without rescue
- "ready for clinical translation" stated without prospective clinical validation
- "novel therapeutic target" stated from database mining alone

---

## Handling Incomplete Input

When input is limited (abstract only, title only):
- Complete all sections that are possible with available information
- Clearly mark each section as: [Full text required] if it cannot be assessed
- Do not fill gaps with inference or assumption
- Do not reproduce content that cannot be verified from the provided input
