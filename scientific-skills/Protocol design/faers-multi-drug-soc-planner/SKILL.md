---
name: faers-multi-drug-soc-planner
description: Generates complete FAERS-based multi-drug single-SOC safety comparison research designs from a user-provided drug set, comparator, and adverse event domain. Always use this skill when users want to compare safety signals across multiple drugs using FAERS or OpenFDA data within one System Organ Class (SOC) or bounded AE domain. Trigger for: "FAERS study comparing drugs within one SOC", "publishable FAERS safety comparison paper", "compare neuropsychiatric adverse events across beta-blockers", "Lite/Standard/Advanced FAERS safety plans", "active-comparator restricted disproportionality", "adjusted ROR logistic regression FAERS", "within-class head-to-head drug comparison", "pharmacovigilance signal comparison", "single-SOC PT-level FAERS design", or any phrasing like "I want to compare drug X and drug Y for adverse events in FAERS" or "build a comparative pharmacovigilance paper". Always output four workload configurations (Lite / Standard / Advanced / Publication+) with a recommended primary plan, step-by-step workflow, figure plan, validation strategy, minimal executable version, and publication upgrade path.
license: MIT
skill-author: AIPOCH
---

# FAERS Multi-Drug Single-SOC Safety Comparison Research Planner

Generates a complete FAERS comparative pharmacovigilance study design from a user-provided drug set, comparator logic, and target SOC. Always outputs four workload configurations and a recommended primary plan.

## Supported Study Styles

- **A. Drug Class vs Active Comparator** — e.g., beta-blockers vs ACE inhibitors for psychiatric disorders
- **B. Within-Class Head-to-Head** — e.g., propranolol vs atenolol vs metoprolol for neuropsychiatric AEs
- **C. Single-SOC + Multi-PT Deepening** — SOC-level signal + clinically meaningful PT breakdown
- **D. Active-Comparator Restricted Disproportionality** — indication-restricted confounding control
- **E. Pharmacologic-Property Heterogeneity** — lipophilic vs hydrophilic, selective vs non-selective subgroups
- **F. Sensitivity-Analysis Strengthened Design** — post hoc indication adjustment, comparator robustness
- **G. Publication-Oriented Integrated Comparative Pharmacovigilance** — full pipeline with subgroup + PT + sensitivity

## Minimum User Input

- One drug or drug class + one comparator or comparator logic + one target SOC or AE domain

## Interface Contract

**Inputs:**
- `drug_set` — one or more drug names or a drug class (e.g., "beta-blockers", "propranolol, atenolol")
- `comparator` — active comparator drug or class (e.g., "ACE inhibitors", "lisinopril"); may be inferred if omitted
- `target_soc` — one MedDRA SOC or bounded AE domain (e.g., "Psychiatric disorders"); may be inferred if omitted
- `config_preference` *(optional)* — "Lite", "Standard", "Advanced", or "Publication+" to pre-select a plan

**Outputs:**
- Four-configuration comparison table (Lite / Standard / Advanced / Publication+)
- Recommended primary plan with justification
- Step-by-step workflow with module-level detail
- Figure plan and table plan
- Validation and robustness plan
- Risk review section
- Minimal executable version (2–3 week path)
- Publication upgrade path table

**Integration note:** Outputs are structured text plans suitable for handoff to data-analysis skills (R/Python pipeline generators) or academic-writing skills.

## Example Inputs

**Example A (Canonical within-class):**
> "Compare beta-blockers (propranolol, atenolol, metoprolol) vs lisinopril for psychiatric adverse events in FAERS. Give me all four configurations."

**Example B (Minimal executable):**
> "I need a quick 3-week FAERS study comparing fluoroquinolones vs beta-lactams for tendon adverse events. Minimal plan only."

## Step-by-Step Execution

### Step 1: Infer Study Type
Identify:
- Drug set and comparator set
- Target SOC and key PTs (if specified)
- Comparison type: class vs class, within-class, subgroup vs subgroup
- Whether active-comparator restricted disproportionality is justified (shared indication required)
- Whether PT-level deepening is central or supportive
- Whether pharmacologic subgroup contrast is biologically motivated
- Resource constraints: public OpenFDA only, raw FAERS, single SOC

### Step 2: Output Four Configurations

Always generate all four:

| Config | Goal | Timeframe | Best For |
|--------|------|-----------|----------|
| **Lite** | Crude + adjusted ROR, one SOC, one comparator | 2–4 weeks | Quick signal check, pilot |
| **Standard** | Full active-comparator design + PT deepening + within-class | 5–8 weeks | Core publishable paper |
| **Advanced** | Standard + pharmacologic subgroup + post hoc sensitivity + richer PT hierarchy | 8–13 weeks | Competitive journal target |
| **Publication+** | Advanced + alternate comparator robustness + richer figure logic + real-world validation suggestions | 12–18 weeks | High-impact submission |

For each configuration describe: goal, required data, major modules, expected workload, figure set, strengths, weaknesses.

### Step 3: Recommend One Primary Plan
Select the best-fit configuration and explain why given drug class biology, comparator suitability, SOC scope, and publication ambition.

### Step 4: Full Step-by-Step Workflow
For each step include: step name, purpose, input, method, key parameters/thresholds, expected output, failure points, alternative approaches.

**Core modules to address when relevant:**

**Data Access & Retrieval**
- OpenFDA API or FAERS quarterly JSON download
- Time-window definition (e.g., 2013–present or bounded period)
- Duplicate case handling (OpenFDA has partial deduplication; note if using raw FAERS)
- Justify OpenFDA vs raw FAERS based on preprocessing needs

**Data Quality Gate** *(apply before proceeding)*
- Minimum case count: require n ≥ 30 cases per drug group before proceeding; if n < 30, flag as underpowered and recommend expanding time window or broadening drug-name regex
- API failure fallback: if OpenFDA API is unavailable, use FAERS quarterly ASCII file downloads from FDA website (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html); provide download path in the plan
- Sparse indication fields: if indication completeness < 20% of cases, note in limitations and recommend (a) reporting complete cases only as sensitivity, or (b) using drug-class indication as proxy; do not treat sparse indication as grounds for abandoning comparator restriction
- Zero-case scenario: if a key PT returns 0 cases for one drug arm, flag as unanalyzable for that PT; remove from primary table but include in supplementary

**Drug Normalization & Case Cleaning**
- Regular-expression medicinal-product name normalization
- Mapping to generic names via RxNorm / ATC / OHDSI
- Role-code filtering: retain primarysuspect (`PS`) only; note `SS`/`C`/`I` exclusions
- Duplicate removal (patient + event + date logic)
- Output: clean drug-indexed case file with counts per drug

**Comparator Definition**
- Active comparator selection: shared therapeutic indication required
- Justify comparator by indication overlap; exclude classes with confounding concern
- Head-to-head within-class comparator logic if applicable
- Output: comparator group definition table with justification

**Outcome (SOC + PT) Definition**
- MedDRA SOC assignment (one primary SOC; optionally one adjacent SOC)
- PT list construction: select 5–12 clinically meaningful PTs within the SOC
- Broad SOC signal + specific PT deepening hierarchy
- Output: SOC/PT definition table with MedDRA codes

**Descriptive Case Characterization**
- Demographics: age (median/IQR), sex, weight, country, reporter type
- Indication summary, serious outcome counts
- Time-to-onset (TTO): median days from drug start to AE onset (if available)
- Output: Table 1 — case characteristics by drug group

**Crude ROR Analysis**
- 2×2 contingency table per drug per outcome (SOC and PT)
- ROR = (a/b) / (c/d); 95% CI via Woolf method
- Signal threshold: lower CI > 1.0 as primary; report all with CI
- Output: crude ROR table per drug per SOC/PT

**Adjusted ROR (Logistic Regression)**
- Logistic regression: outcome ~ drug_group + covariates
- Covariates: age, sex, weight, key comorbidities relevant to indication (e.g., hypertension, HF, AF for cardiovascular drugs)
- Reference: active comparator group as reference level
- Report aROR with 95% CI; compare crude vs adjusted
- Failure point: sparse cells for rare PTs → Firth penalized logistic or note instability

**Within-Class Head-to-Head Comparison**
- Pairwise drug comparisons within class (e.g., propranolol vs atenolol)
- Logistic model with one drug as reference
- Interpret directional consistency across PTs
- Note: for ≥ 4 pairwise comparisons, apply Bonferroni or FDR correction; report uncorrected and corrected results side by side

**Pharmacologic Subgroup Comparison** (Advanced+)
- Map each drug to pharmacologic property subgroup (e.g., lipophilic vs hydrophilic)
- Compare aROR distributions across subgroups
- Frame as hypothesis-supporting, not causal proof

**Sensitivity Analysis** (Standard+)
- Post hoc: add non-primary indication adjustment (e.g., migraine, anxiety for beta-blockers)
- Alternate comparator robustness: swap one comparator; check directional stability
- Role-code sensitivity: include SS cases and compare
- Output: sensitivity table alongside primary results

### Step 5: Figure Plan

| Figure | Content |
|--------|---------|
| Fig 1 | Overall workflow / study design schematic |
| Fig 2 | Case selection flowchart (CONSORT-style) |
| Fig 3 | SOC-level forest plot (aROR per drug vs comparator) |
| Fig 4 | PT-level forest plot (aROR per drug per key PT) |
| Fig 5 | Within-class head-to-head comparison figure |
| Fig 6 | Time-to-onset summary (violin or box) per drug group |
| Fig 7 | Sensitivity analysis comparison (primary vs sensitivity aROR) |
| Table 1 | Drug normalization + comparator definition |
| Table 2 | Descriptive case characteristics |
| Table 3 | Crude + adjusted ROR summary (SOC + PT) |
| Table 4 | Sensitivity analysis summary |

### Step 6: Validation and Robustness Plan

Distinguish clearly:
- **Data-cleaning robustness** — normalization consistency, duplicate handling, role-code restriction
- **Comparator robustness** — indication overlap validity, inappropriate comparator avoidance
- **Adjusted signal support** — crude vs adjusted ROR comparison; covariate transparency
- **Within-class heterogeneity evidence** — directional consistency across drugs and PTs
- **Sensitivity-analysis support** — stability of findings under alternate model specifications

State what each layer proves and what it does not prove:
- Disproportionality signal ≠ incidence estimate
- Adjusted ROR controls measured confounders, not unmeasured indication bias
- Active comparator reduces but does not eliminate confounding by indication
- PT-level signals are exploratory without multiplicity correction unless pre-specified

### Step 7: Risk Review

Always include a self-critical section addressing:
- Strongest part: active-comparator restriction + logistic adjustment
- Most assumption-dependent: completeness of indication fields in FAERS (often sparse)
- Most likely false-positive source: multiple PT comparisons without multiplicity correction
- Easiest to overinterpret: ROR as "risk" rather than "reporting proportion difference"
- Most likely reviewer criticisms: underreporting bias, notoriety bias, residual confounding by indication, drug-name misclassification, no external population-based validation
- Revision if findings fail: switch to PT-level primary outcome; restrict to highest-quality reporter types (HCP-only); expand covariate set

### Step 8: Minimal Executable Version

OpenFDA only, one drug class + one active comparator, one SOC, primary suspect restriction, drug normalization, crude + adjusted ROR, 3–5 key PTs, one summary table + one forest plot. 2–3 week timeline.

### Step 9: Publication Upgrade Path

| Addition | Publication Gain | Effort |
|----------|-----------------|--------|
| Add second active comparator | High (comparator robustness) | Low |
| Add within-class head-to-head | High (heterogeneity story) | Low–Medium |
| Add time-to-onset summary | Medium | Low |
| Add pharmacologic subgroup comparison | Medium (mechanistic framing) | Medium |
| Add post hoc sensitivity analysis | High (reviewer defense) | Low |
| Expand PT architecture to 10–12 PTs | Medium | Low |
| Add HCP-only reporter sensitivity restriction | Medium | Low |

## Hard Rules

1. Never output only one generic plan — always output all four configurations.
2. Always recommend one primary plan with justification.
3. Always separate necessary modules from optional modules.
4. Distinguish disproportionality evidence, adjusted signal support, heterogeneity evidence, and sensitivity support.
5. Never treat FAERS signals as incidence estimates — label as reporting disproportionality.
6. Never overclaim causal drug effects from disproportionality alone.
7. Do not force broad all-SOC scans when user clearly wants one SOC or narrow domain.
8. Do not ignore comparator suitability; flag if indication overlap is weak.
9. Do not ignore drug-name misclassification risk — always include normalization step.
10. If user provides limited detail, infer a reasonable default design and state assumptions clearly.

## Input Validation

This skill accepts: a drug set (one or more drugs or a drug class) + a comparator (or inferrable comparator) + a target SOC or AE domain, submitted for FAERS comparative pharmacovigilance study design.

**Out-of-scope response templates:**

*If the user provides only one drug with no comparator and no SOC:*
> "To design a FAERS comparative study, this skill needs at minimum: (1) a target drug or drug class, (2) a comparator, and (3) a target adverse event domain. I'll infer a reasonable comparator and SOC based on the drug's indication — please confirm or correct my assumptions before proceeding."

*If the user requests an all-SOC sweep or pan-MedDRA signal scan:*
> "This skill is designed for single-SOC comparative pharmacovigilance designs. An all-SOC disproportionality sweep is a different study type outside this scope. I can help you: (a) identify the highest-priority SOC for your drug and design a focused study there, or (b) describe how an all-SOC PRR/EBGM screen would differ methodologically. Which would be more useful?"

*If the user asks to frame FAERS disproportionality results as causal evidence without caveats:*
> "FAERS disproportionality analysis (ROR/PRR) cannot establish causality — it quantifies reporting proportion differences, not incidence or risk. This skill will always include appropriate epistemic caveats. I can design the strongest possible comparative pharmacovigilance study with active-comparator restriction and sensitivity analysis to maximize the evidentiary weight of the findings."

*If the request is unrelated to FAERS/pharmacovigilance study design:*
> "FAERS Multi-Drug SOC Planner is designed to generate comparative pharmacovigilance study designs using FAERS or OpenFDA data. Your request appears to be outside this scope. Please use a more appropriate tool for your task."
