---
name: linkedin-optimizer
description: Use when optimizing LinkedIn profiles for doctors, physicians, nurses, healthcare professionals, or medical researchers. Crafts compelling headlines, writes professional summaries, integrates healthcare keywords, and builds personal branding for medical careers.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# LinkedIn Optimizer for Healthcare Professionals

Optimize LinkedIn profiles for doctors, physicians, nurses, and healthcare professionals to enhance professional visibility and career opportunities.

## Quick Start

```python
from scripts.linkedin_optimizer import LinkedInOptimizer

optimizer = LinkedInOptimizer()

# Generate optimized profile content
profile = optimizer.optimize(
    role="Cardiologist",
    specialty="Interventional Cardiology",
    achievements=["Published 15+ peer-reviewed papers", "Led clinical trial for novel stent"],
    years_experience=12
)

print(profile.headline)
print(profile.about_section)
```

## Core Capabilities

### 1. Headline Optimization

```python
optimizer = LinkedInOptimizer()
headline = optimizer.generate_headline(
    title="Board-Certified Cardiologist",
    specialty="Heart Failure & Transplant",
    differentiator="Clinical Researcher"
)
# Output: "Board-Certified Cardiologist | Heart Failure & Transplant Specialist | Clinical Researcher"
```

**Headline Formulas:**
- `Title | Specialty | Differentiator`
- `Role | Key Skill | Mission`
- `Credentials | Focus Area | Value Proposition`

### 2. About Section Writing

```python
about = optimizer.write_about_section(
    role="Oncologist",
    approach="Patient-centered care with precision medicine",
    expertise=["Immunotherapy", "Clinical trials", "Palliative care"],
    achievements=["Treated 1000+ patients", "Principal investigator on 5 trials"]
)
```

**About Section Structure:**
1. **Opening Hook** (2-3 sentences) - Who you help and how
2. **Expertise Areas** (bullet points) - Key skills and specialties
3. **Key Achievements** (bullet points) - Quantified accomplishments
4. **Call to Action** - How to connect

**Example:**
> I'm a board-certified oncologist dedicated to advancing cancer treatment through precision medicine and immunotherapy. With over 10 years of experience, I specialize in developing personalized treatment plans that improve patient outcomes while maintaining quality of life.
>
> **Areas of Expertise:**
> - Immunotherapy and targeted therapy
> - Clinical trial design and implementation
> - Palliative care integration
> - Multi-disciplinary team leadership
>
> **Key Achievements:**
> - Treated 1000+ cancer patients with 85% positive outcomes
> - Principal investigator on 5 Phase II/III clinical trials
> - Published 20+ peer-reviewed papers on novel treatment protocols
>
> **Let's Connect:** Open to collaborations on clinical research and discussing innovative treatment approaches.

### 3. Keyword Integration

```python
keywords = optimizer.suggest_keywords(
    specialty="Emergency Medicine",
    role="ER Physician",
    target_audience=["Recruiters", "Hospital administrators", "Medical device companies"]
)
```

**High-Value Keywords by Specialty:**

| Specialty | Primary Keywords | Secondary Keywords |
|-----------|-----------------|-------------------|
| Cardiology | Cardiologist, Interventional Cardiology, Heart Failure | Clinical Cardiology, Cardiac Catheterization |
| Oncology | Oncologist, Medical Oncology, Cancer Treatment | Immunotherapy, Precision Medicine |
| Surgery | Surgeon, General Surgery, Minimally Invasive | Robotic Surgery, Laparoscopic |
| Pediatrics | Pediatrician, Child Health, Developmental Medicine | Neonatology, Pediatric Emergency |
| Research | Clinical Research, Principal Investigator, FDA Trials | Drug Development, Protocol Design |

### 4. Experience Section Optimization

```python
experiences = optimizer.optimize_experiences([
    {
        "title": "Attending Physician",
        "organization": "Mayo Clinic",
        "duration": "2019-Present",
        "achievements": ["Reduced readmission rates by 25%", "Implemented new protocol"]
    }
])
```

**Experience Formula:**
- **Action verb** + **What you did** + **Result/Impact**
- Example: "Implemented early discharge protocol reducing average length of stay by 2.3 days and saving $500K annually"

## CLI Usage

```bash
# Optimize complete profile
python scripts/linkedin_optimizer.py \
  --role "Neurologist" \
  --specialty "Movement Disorders" \
  --achievements "Published 10 papers, Led Parkinson's clinic" \
  --output profile.json

# Generate only headline
python scripts/linkedin_optimizer.py \
  --mode headline \
  --title "Emergency Medicine Physician" \
  --specialty "Trauma & Critical Care"
```

## Common Patterns

See `references/linkedin-examples.md` for detailed examples:
- Academic Physician Profile
- Private Practice Doctor
- Medical Researcher
- Healthcare Executive
- Resident/Fellow Profile

## Quality Checklist

**Before Optimization:**
- [ ] Define target audience (recruiters, patients, collaborators)
- [ ] List 3-5 key achievements with metrics
- [ ] Identify unique value proposition

**After Optimization:**
- [ ] Headline under 220 characters
- [ ] About section includes keywords naturally
- [ ] All claims are verifiable
- [ ] Call to action is clear

## References

- `references/linkedin-examples.md` - Profile examples by specialty
- `references/keywords-by-specialty.json` - Keyword database
- `references/headline-templates.md` - Headline formulas

---

**Skill ID**: 201 | **Version**: 1.0 | **License**: MIT
