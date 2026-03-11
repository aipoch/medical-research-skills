# Similar Literature Module

This file defines the rules for selecting and presenting related studies in Section 13
of the Mandatory Output Template.

---

## Selection Rules

Provide a focused, relevant list — not a keyword dump. Aim for 3–8 studies.

**Priority order:**
1. Same disease + same core research question
2. Same study design (e.g., another NHANES cross-sectional, another TCGA prognostic signature)
3. Same methodological approach (e.g., another ML + SHAP clinical prediction, another
   bioinformatics + functional validation paper)
4. Higher-quality benchmark papers — stronger evidence, broader cohort, better validation,
   more complete mechanism

**Avoid:**
- Papers that are only tangentially related by keyword
- Bloated bibliography-style lists with no comparative context
- Papers that are identical in design and add nothing new

---

## Presentation Format

For each suggested study, provide all four fields:

```
**[Title or abbreviated citation]**
- Why similar: [shared disease, design, or method]
- What it adds vs the current paper: [specific incremental value]
- Relative quality: Stronger / Weaker / Complementary — [one-sentence reason]
```

---

## Track-Specific Guidance

**Track A (Clinical):**
Focus on studies with: same primary endpoint, same population, or higher-level design
(e.g., if the current paper is a cohort study, suggest the relevant RCT or meta-analysis).

**Track B (Bioinformatics):**
Focus on: same disease + same data type (e.g., another scRNA-seq study in the same tumour),
or a paper with stronger external validation of the same signature/biomarker.

**Track C (Experimental):**
Focus on: papers that close the mechanism loop the current paper left open, or papers using
stronger model systems for the same pathway.

**Track D (Hybrid):**
Focus on papers that integrate the same combination of evidence types, particularly those
with more complete validation chains.

---

## Handling Uncertainty

If the exact papers cannot be confirmed with certainty, note this explicitly:

> "The following are representative studies of this type; please verify publication details
> before citing."

Do not fabricate titles, authors, journal names, or PMIDs. If no closely relevant studies
can be reliably identified, state: *"I cannot reliably identify closely related studies
without access to a live literature database. I recommend searching PubMed with the
following terms: [specific search string]."*
