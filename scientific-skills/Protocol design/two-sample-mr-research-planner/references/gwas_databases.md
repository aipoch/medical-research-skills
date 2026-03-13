# GWAS Database Recommendations by Exposure Class

> Last verified: March 2026
> Primary access portal for most resources: IEU Open GWAS (https://gwas.mrcieu.ac.uk)

---

## Biomarker / Molecular Traits

| Database / Consortium | Key Traits | Ancestry | Access |
|---|---|---|---|
| **UK Biobank** (UKB) | 2,400+ blood/urine biomarkers | EUR-dominant | IEU Open GWAS; UKB RAP |
| **deCODE genetics** | Plasma proteome (SOMAscan ~5,000 proteins) | EUR (Icelandic) | Publication supplementary; MR-Base |
| **UK Biobank Olink** (UKB-PPP) | ~2,900 proteins (proximity extension) | EUR-dominant | IEU Open GWAS; UKB RAP |
| **INTERVAL / SomaScan** | ~3,600 plasma proteins | EUR | Published GWAS summary stats |
| **Kettunen 2016 / Wurtz 2021** | NMR metabolomics (225 metabolites) | EUR (Finnish) | IEU Open GWAS |
| **MR-MegEx / eQTLGen** | Blood eQTLs (gene expression) | EUR-dominant | eqtlgen.org |
| **GTEx v8** | Tissue-specific eQTLs | EUR-dominant | gtexportal.org |

**Typical IV count (cis-pQTL):** 1–10 per protein (often genome-wide significant); trans-pQTLs may add more but carry pleiotropy risk.

---

## Dietary / Nutritional Exposures

| Database / Consortium | Key Traits | Ancestry | Access |
|---|---|---|---|
| **UK Biobank FFQ GWAS** | 83 dietary habits (food frequency questionnaire) | EUR | IEU Open GWAS (ukb-b-*) |
| **EPIC** | Dietary intake measures | EUR (multi-country) | Published summary stats |
| **23andMe / Neale Lab UKB** | Coffee, alcohol, tea intake | EUR | IEU Open GWAS |
| **CHARGE Consortium** | Vitamin D, omega-3 fatty acids | EUR-dominant | Published summary stats |

**Typical IV count:** 2–15 per dietary trait; many dietary exposures yield <5 genome-wide significant SNPs. Flag weak-instrument risk if N_IVs < 10.

---

## Behavioral / Lifestyle Exposures

| Database / Consortium | Key Traits | Ancestry | Access |
|---|---|---|---|
| **UK Biobank** | Sleep duration, physical activity, smoking, alcohol | EUR-dominant | IEU Open GWAS |
| **Sleep Disorder GWAS** (Jansen 2019, Dashti 2019) | Sleep duration, insomnia, chronotype | EUR | Published summary stats; IEU Open GWAS |
| **GSCAN Consortium** | Smoking initiation, cigarettes per day, alcohol | EUR | IEU Open GWAS |
| **MVP / UKB** | Physical activity (accelerometry) | EUR-dominant | IEU Open GWAS |

**Typical IV count:** 3–50 per behavioral trait; phenotype measurement noise (self-report) is a major source of bias. Prefer objective measurement GWAS (accelerometry over questionnaire) when available.

---

## Gut Microbiome

| Database / Consortium | Key Traits | Ancestry | Access |
|---|---|---|---|
| **MiBioGen Consortium** (Kurilshikov 2021) | 196 microbial taxa | EUR (18 cohorts) | mibiogen.eu; IEU Open GWAS |
| **FINRISK / FGFP** | Gut microbiota diversity metrics | EUR (Finnish/Belgian) | Published summary stats |
| **UK Biobank Gut Microbiome** | 16S / shotgun sequencing taxa | EUR-dominant | Under active release |

**Typical IV count:** 1–5 per taxon; many taxa have 0 genome-wide significant SNPs. MR feasibility should be assessed before committing to a full study. Frame microbiome MR analyses as **exploratory only**.

---

## Disease / Clinical Outcomes

| Database / Consortium | Key Traits | Ancestry | Access |
|---|---|---|---|
| **FinnGen** | 2,000+ disease endpoints (ICD-10 based) | EUR (Finnish) | finngen.fi; IEU Open GWAS |
| **UK Biobank** | Hospital Episode Statistics phenomes | EUR-dominant | IEU Open GWAS |
| **GWAS Catalog** | Curated published GWAS across all traits | Mixed | ebi.ac.uk/gwas |
| **IGAP / EADB** | Alzheimer's disease | EUR | Published; IEU Open GWAS |
| **PGC** | Psychiatric disorders (MDD, SCZ, BIP, ADHD) | EUR-dominant | pgc.unc.edu; IEU Open GWAS |
| **CARDIoGRAM / HERMES** | Coronary artery disease, heart failure | EUR | Published; IEU Open GWAS |
| **DIAGRAM** | Type 2 diabetes | EUR-dominant | Published; IEU Open GWAS |

---

## Ancestry Matching Guidance

- Default to **European ancestry (EUR)** GWAS pairs for primary analysis when available; this minimizes LD structure mismatch.
- For non-EUR populations: use **EAS** (BBJ, CKB, UKBB-Asian) or **AFR** (AWI-Gen, H3Africa) specific GWAS when available.
- **Do not mix ancestries** across exposure and outcome GWAS without explicitly modeling this as a limitation.
- Cross-ancestry MR is an active research area; flag it as exploratory if used.

---

## Sample Overlap Check

- Check whether the exposure and outcome GWAS share participants (common sources: UK Biobank, 23andMe).
- Substantial sample overlap biases IVW toward the observational estimate; use GSMR with HEIDI-outlier test or sensitivity analyses robust to overlap.
- Report overlap status in the methods section.
