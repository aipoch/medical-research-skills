---
name: two-sample-mr-research-planner
description: Generates complete two-sample Mendelian randomization (MR) research designs from a user-provided research direction. Use when users want to design, plan, or build a study using two-sample MR to test causal relationships. Triggers: "design a two-sample MR study", "build a publishable MR paper", "test whether this biomarker causally affects this disease", "generate Lite/Standard/Advanced MR plans", "screen multiple exposures with MR", "bidirectional MR design", "causal inference using GWAS summary statistics", or "I want to study X and Y using MR". Always outputs four workload configurations (Lite / Standard / Advanced / Publication+) with a recommended primary plan, step-by-step workflow, figure plan, validation strategy, minimal executable version, and publication upgrade path.
license: MIT
skill-author: AIPOCH
---

# Two-Sample Mendelian Randomization Research Planner

Generates a complete two-sample MR study design from a user-provided research direction. Always outputs four workload configurations and a recommended primary plan.

## Supported Study Styles

| Style | Description | Example |
|-------|-------------|---------|
| **A. Single Exposure → Single Outcome** | One biomarker or trait to one disease | Serum uric acid → gout; vitamin D → osteoporosis |
| **B. Multi-Exposure Screening** | Panel of exposures to one outcome | Dietary factors → endometriosis; cytokine panel → RA |
| **C. Bidirectional MR** | Reciprocal causal testing | Inflammation ↔ depression; BMI ↔ osteoarthritis |
| **D. Lifestyle / Diet / Behavioral** | Self-reported behavioral exposures | Coffee intake → hypertension; sleep duration → stroke |
| **E. Biomarker / Molecular Trait** | Circulating proteins, metabolites | Cytokines → autoimmune disease; plasma proteins → Alzheimer's |
| **F. Publication-Oriented** | Comprehensive sensitivity-rich design | Full estimator suite with complete figure set |

## Minimum User Input

- One exposure (or exposure set) + one outcome
- If limited detail is provided, infer a reasonable default design and state all assumptions explicitly

## Step-by-Step Execution

### Step 1: Infer Study Type

Identify:
- Exposure(s) and outcome
- Exposure class (dietary, biomarker, metabolite, behavioral, disease trait, molecular)
- User goal: screening, bidirectional, causal verification, or publication strength
- Whether MVMR or colocalization is justified
- Time or resource constraints stated by the user

### Step 2: Output Four Configurations

Always generate all four. For each configuration describe: goal, required data, major modules, expected workload, figure set, strengths, and weaknesses.

| Config | Goal | Timeframe | Best For |
|--------|------|-----------|----------|
| **Lite** | Fast minimal causal test | 2–4 weeks | Quick launch, 1 exposure × 1 outcome |
| **Standard** | Publication-ready core MR | 4–8 weeks | Single or small panel + sensitivity suite |
| **Advanced** | Robust multi-extension design | 8–14 weeks | Bidirectional, MVMR, replication GWAS |
| **Publication+** | High-impact comprehensive paper | 12–20 weeks | Full sensitivity, MVMR, colocalization, power |

### Step 3: Recommend One Primary Plan

Select the best-fit configuration and explain why, given the exposure type, outcome, and any stated user constraints (time, data access, publication goal).

### Step 4: Full Step-by-Step Workflow

For each step include: step name, purpose, input, method, key parameters/thresholds, expected output, failure points, and alternative approaches.

**Core modules to address when relevant:**

- Exposure GWAS selection + ancestry matching
- Outcome GWAS selection
- Instrument extraction (p < 5×10⁻⁸, LD clumping r² < 0.001 / 10,000 kb)
- F-statistic screening (F > 10)
- Harmonization (palindromic SNP handling)
- IVW (primary analysis, random effects)
- MR-Egger, weighted median, simple/weighted mode (complementary)
- Heterogeneity (Cochran's Q, I²)
- Pleiotropy (MR-Egger intercept, MR-PRESSO)
- Leave-one-out analysis
- Bidirectional MR (when justified — see Hard Rules)
- MVMR (when confounding exposures need adjustment)
- Power / MDES discussion
- Colocalization (Advanced / Publication+ only; PP.H4 > 0.8 standard)

**Exposure-class IV count benchmarks** — state expected IV count and flag weak-instrument risk accordingly:

→ Full benchmarks by exposure class: [references/iv_benchmarks.md](references/iv_benchmarks.md)

**GWAS data sources by exposure class:**

→ Recommended databases and last-verified dates: [references/gwas_databases.md](references/gwas_databases.md)

**Fault tolerance guidelines:**
- If the target GWAS is unavailable: state this explicitly, suggest the closest publicly available alternative, and recommend the Lite configuration until data access is confirmed
- If IV count falls below 3: warn the user that MR is not feasible with current instruments; suggest waiting for larger GWAS or pivoting to a proxy exposure
- If F-statistic < 10 for all IVs: do not proceed with IVW as primary; escalate to weak-instrument-robust methods (LIML, sisVIVE) and note this as a study limitation

### Step 5: Figure and Deliverable Plan

Always list:
- Scatter plots (exposure–outcome per estimator)
- Forest plots (leave-one-out)
- Funnel plots (pleiotropy visual)
- Summary results table (all estimators)
- Sensitivity analysis table

### Step 6: Validation and Robustness Plan

State what each layer proves and what it does not prove. Distinguish:
- **Primary MR evidence**: IVW result + instrument validity checks (F > 10, no strong pleiotropy signal)
- **Sensitivity support**: estimator consistency across MR-Egger, weighted median, mode; Cochran Q non-significant
- **Higher-tier causal strengthening**: MVMR (adjusts for correlated exposures), bidirectional MR (rules out reverse causation), colocalization (rules out LD confounding)

### Step 7: Risk Review

Always include a self-critical section addressing:
- Strongest part of the design
- Most assumption-dependent part
- Most likely source of false positives
- Easiest part to overinterpret
- Most likely reviewer criticisms: weak instruments, pleiotropy, ancestry mismatch, sample overlap, multiple-testing (for screening studies), behavioral phenotype noise, insufficient IV count for dietary/microbiome exposures
- Revision strategy if first-pass findings fail

### Step 8: Minimal Executable Version

Slim version using only publicly available GWAS: 1 exposure (or small set), 1 outcome, IVW + 1–2 complementary estimators, heterogeneity/pleiotropy/leave-one-out, concise interpretation. Confirm this fits within any stated time constraints before recommending.

### Step 9: Publication Upgrade Path

Explain what to add beyond Standard, which additions most improve publication strength, and which modules add rigor versus complexity. For molecular trait MR (proteins, metabolites), always include colocalization as a required upgrade for high-impact journals.

## R Code Framework Guidelines

When providing R code examples or frameworks:
- Always use the `TwoSampleMR` package (CRAN) as the primary tool
- Mark all GWAS IDs as examples with an explicit inline comment: `# EXAMPLE ID — replace with your target phenotype ID`
- Do not present example IDs as validated or guaranteed to resolve correctly
- Provide the IEU Open GWAS API query pattern so users can search for their own phenotype IDs

**Standard R framework template:**

```r
library(TwoSampleMR)
library(MRPRESSO)

# Step 1: Extract instruments for exposure
# EXAMPLE ID below — replace with your target exposure GWAS ID
exposure <- extract_instruments(outcomes = "ukb-b-XXXXX")  # EXAMPLE ID

# Step 2: Extract outcome data
# EXAMPLE ID below — replace with your target outcome GWAS ID
outcome <- extract_outcome_data(
  snps = exposure$SNP,
  outcomes = "ieu-b-XXXXX"  # EXAMPLE ID
)

# Step 3: Harmonise
harmonized <- harmonise_data(exposure, outcome)

# Step 4: Primary and sensitivity analyses
res <- mr(harmonized, method_list = c(
  "mr_ivw",
  "mr_egger_regression",
  "mr_weighted_median",
  "mr_weighted_mode"
))

# Step 5: Heterogeneity and pleiotropy
het  <- mr_heterogeneity(harmonized)
plt  <- mr_pleiotropy_test(harmonized)
loo  <- mr_leaveoneout(harmonized)
```

To find valid GWAS IDs: `ao <- available_outcomes(); View(ao)`

## Hard Rules

1. Never output only one generic plan — always output all four configurations.
2. Always recommend one primary plan with justification.
3. Always separate necessary modules from optional modules.
4. Distinguish primary MR evidence, sensitivity support, and higher-tier causal strengthening.
5. Do not force bidirectional or MVMR if the topic does not justify it.
6. Do not overclaim causality when instruments are weak or behavioral phenotypes are noisy.
7. Do not treat nominal estimator agreement as proof if sensitivity analyses are inconsistent.
8. Do not ignore ancestry mismatch or sample-overlap concerns.
9. If the user provides limited detail, infer a reasonable default design and state all assumptions clearly.
10. Do not produce only a literature summary or flat methods list.
11. **Out-of-scope redirect**: If the user requests a non-MR causal inference design (RCT, propensity score matching, DAG-based observational analysis, Bayesian network, etc.), clearly state that this skill covers two-sample MR only and recommend consulting appropriate resources (e.g., CONSORT for RCTs, STROBE for observational studies).

## Input Validation

This skill accepts: a research direction involving a causal question between an exposure (biomarker, dietary factor, behavioral trait, molecular trait, or disease) and an outcome, where the user wants to design a two-sample Mendelian randomization study.

If the user's request does not involve MR study design — for example, asking to design an RCT, conduct a systematic review, write a manuscript introduction, perform propensity score analysis, or answer a general epidemiology question — do not proceed with the MR planning workflow. Instead respond:
> "Two-Sample MR Research Planner is designed to generate Mendelian randomization study designs using GWAS summary statistics. Your request appears to be outside this scope. Please provide an exposure–outcome pair you want to test using MR, or use a more appropriate skill for your task (e.g., a systematic review skill for literature synthesis, or an experimental design skill for RCTs)."

## Reference Files

| File | Content | Used In |
|------|---------|---------|
| [references/gwas_databases.md](references/gwas_databases.md) | Recommended GWAS sources by exposure class with last-verified dates | Step 4 — GWAS selection |
| [references/iv_benchmarks.md](references/iv_benchmarks.md) | Typical IV count ranges and weak-instrument risk flags by exposure class | Step 4 — instrument extraction |
