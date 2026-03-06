---
name: digital-twin-discharge-drafter
description: Use when drafting patient discharge summaries, creating personalized discharge instructions, simulating post-discharge outcomes, reducing hospital readmissions, or optimizing care transitions. Generates AI-enhanced discharge documentation with digital twin predictions for improved patient safety.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Digital Twin Discharge Drafter

Generate AI-enhanced discharge summaries and personalized care plans using digital twin patient models to predict outcomes and optimize post-discharge care transitions.

## Quick Start

```python
from scripts.discharge_drafter import DischargeDrafter

drafter = DischargeDrafter()

# Generate comprehensive discharge summary
summary = drafter.generate(
    patient_id="PT12345",
    admission_data=admission_info,
    hospital_course=treatment_history,
    digital_twin_model=patient_model,
    output_format="structured"
)

# Export patient-friendly version
patient_version = drafter.generate_patient_friendly(summary)

print(summary.readmission_risk_score)  # 0.23
print(summary.key_interventions)       # ['home_health', 'med_reconciliation']
```

## Core Capabilities

### 1. Digital Twin-Powered Summary Generation

```python
summary = drafter.create_summary(
    patient_data=patient_record,
    digital_twin_model=twin_model,
    include_predictions=True,
    risk_stratification="high",
    readmission_risk_threshold=0.15
)
```

**Summary Components:**
- **Hospital Course**: AI-summarized treatment narrative
- **Digital Twin Predictions**: 7-day, 30-day outcome probabilities
- **Risk Stratification**: Readmission risk score with factors
- **Medication Reconciliation**: AI-validated med list
- **Follow-up Schedule**: Optimized based on patient model

### 2. Post-Discharge Outcome Simulation

```python
scenarios = drafter.simulate_outcomes(
    patient_model=digital_twin,
    scenarios=[
        "medication_adherent",
        "medication_non_adherent", 
        "follow_up_missed",
        "social_support_optimal"
    ],
    timeframe="30_days",
    metrics=["readmission_risk", "recovery_trajectory", "cost_projection"]
)
```

**Simulation Outputs:**

| Scenario | Readmission Risk | Recovery Time | Cost Impact |
|----------|-----------------|---------------|-------------|
| Optimal adherence | 5% | 14 days | Baseline |
| Med non-adherent | 25% | 28 days | +$8,500 |
| Missed follow-up | 18% | 21 days | +$4,200 |

### 3. Personalized Patient Instructions

```python
instructions = drafter.create_personalized_instructions(
    patient_profile=profile,
    health_literacy_level="assessed",  # or "8th_grade", "college"
    language_preference="English",
    cultural_considerations=True,
    access_barriers=["transportation", "cost"]
)

# Returns structured instructions
print(instructions.medication_list)      # Formatted medication table
print(instructions.followup_appointments)  # Scheduled visits
print(instructions.red_flags)            # When to call doctor
print(instructions.lifestyle_changes)    # Diet, activity restrictions
```

**Personalization Factors:**
- **Health Literacy**: Adjust complexity (Flesch-Kincaid 6th-12th grade)
- **Language**: Multi-language support with medical accuracy
- **Cultural**: Dietary restrictions, family dynamics, beliefs
- **Barriers**: Transportation, cost, caregiver availability

### 4. Risk-Based Care Planning

```python
care_plan = drafter.create_risk_based_plan(
    patient_risk_score=0.72,
    risk_factors=["CHF", "diabetes", "living_alone"],
    interventions=[
        "telehealth_monitoring",
        "home_health_visit",
        "pharmacy_consult"
    ]
)
```

**Risk Stratification:**

| Risk Level | Score | Interventions |
|------------|-------|---------------|
| Low | <0.10 | Standard discharge + phone follow-up |
| Moderate | 0.10-0.25 | + Telehealth monitoring |
| High | 0.25-0.50 | + Home health visit within 48h |
| Very High | >0.50 | + Care coordination + daily check-ins |

### 5. Quality Assurance

```python
qa_report = drafter.validate_summary(
    discharge_summary,
    checks=[
        "completeness_jcaho",
        "medication_accuracy",
        "readability_score",
        "prediction_confidence"
    ]
)
```

## CLI Usage

```bash
# Generate complete discharge package
python scripts/discharge_drafter.py \
  --patient PT12345 \
  --digital-twin-model models/patient_v2.pkl \
  --include-predictions \
  --output-format both \
  --output-dir discharge_summaries/

# Batch process high-risk patients
python scripts/discharge_drafter.py \
  --batch high_risk_patients.csv \
  --priority ICU,CCU \
  --auto-escalate-risk 0.30

# Generate patient-friendly only
python scripts/discharge_drafter.py \
  --patient PT12345 \
  --mode patient-friendly \
  --reading-level 6th_grade \
  --language Spanish \
  --output patient_handout.pdf
```

## Common Patterns

### Pattern 1: CHF Patient Discharge

**Digital Twin Insights:**
- Baseline readmission risk: 22%
- With medication adherence: 8%
- Without follow-up: 35%

**Generated Interventions:**
- Daily weight telemonitoring
- Cardiology appointment within 7 days
- Medication reconciliation with pharmacist
- Home health evaluation

### Pattern 2: Post-Surgical Patient

**Digital Twin Insights:**
- Infection risk peaks day 3-5
- Mobility compliance critical for recovery

**Generated Plan:**
- Wound care video instructions
- Physical therapy schedule
- Red flag symptom checklist
- Pain management protocol

## Quality Checklist

**Pre-Discharge:**
- [ ] Digital twin model updated with hospital course
- [ ] Readmission risk calculated and documented
- [ ] Medication reconciliation completed
- [ ] Follow-up appointments scheduled
- [ ] Patient/caregiver education requirements assessed

**Discharge Summary:**
- [ ] Includes digital twin predictions with confidence intervals
- [ ] Risk factors clearly listed with mitigation strategies
- [ ] Patient-friendly instructions at appropriate literacy level
- [ ] Emergency contact numbers provided
- [ ] 24/7 nurse line access included

**Post-Discharge (24-48 hours):**
- [ ] Automated follow-up call triggered
- [ ] Pharmacy notified of new prescriptions
- [ ] Primary care provider receives summary
- [ ] Home health services activated (if indicated)

## Best Practices

**Digital Twin Model Maintenance:**
- Update models weekly with new patient data
- Validate predictions against actual outcomes
- Retrain models quarterly for accuracy improvement

**Patient Communication:**
- Always provide both clinical and patient-friendly versions
- Use teach-back method to confirm understanding
- Document health literacy level in patient record

## Common Pitfalls

❌ **Over-reliance on AI**: Digital twin predictions supplement, not replace, clinical judgment
✅ **Clinical Oversight**: Physician reviews and approves all AI-generated content

❌ **Generic Instructions**: One-size-fits-all discharge plans
✅ **Personalized Plans**: Tailored to individual patient models and barriers

❌ **Ignoring Low-Risk Patients**: Focusing only on high-risk cases
✅ **Universal Application**: All patients benefit from digital twin insights

---

**Skill ID**: 214 | **Version**: 1.0 | **License**: MIT
