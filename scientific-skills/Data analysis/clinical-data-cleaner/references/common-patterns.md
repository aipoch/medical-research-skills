## Common Patterns

### Pattern 1: Regulatory Submission Preparation

**Scenario**: Preparing SDTM datasets for FDA submission.

```json
{
  "submission_type": "FDA NDA",
  "domains": ["DM", "LB", "VS", "AE", "MH"],
  "cleaning_approach": "Conservative - flag rather than remove",
  "validation": "CDISC SDTM IG v3.2",
  "audit_requirements": "Complete traceability of all changes",
  "deliverables": [
    "Cleaned datasets",
    "Cleaning reports",
    "Programming specifications"
  ]
}
```

**Workflow:**
1. Load raw data from EDC system
2. Validate against SDTM domain specifications
3. Clean using conservative settings (flag outliers)
4. Generate comprehensive audit trails
5. Validate final datasets with Pinnacle 21
6. Document all cleaning decisions
7. Package for regulatory submission

**Output Example:**
```
FDA Submission Package:
  
Datasets:
  ✓ dm.xpt (1,247 subjects)
  ✓ lb.xpt (45,678 records)
  ✓ vs.xpt (12,470 records)
  
Cleaning Statistics:
  - Missing values imputed: 234
  - Outliers flagged: 89
  - Date formats standardized: 1,247
  
Audit Trail:
  - Cleaning reports: 3 files
  - All actions documented
  - 21 CFR Part 11 compliant
  
Validation:
  ✓ Pinnacle 21: 0 errors, 3 warnings
  ✓ CDISC SDTM IG v3.2 compliant
```

### Pattern 2: Interim Analysis Data Preparation

**Scenario**: Cleaning data for interim analysis during ongoing trial.

```json
{
  "analysis_type": "Interim efficacy",
  "data_cutoff": "2023-12-31",
  "cleaning_priority": "Speed with quality",
  "domains_needed": ["DM", "LB", "VS"],
  "outlier_handling": "Flag for statistician review",
  "timeline": "3 days"
}
```

**Workflow:**
1. Extract data with cutoff date
2. Quick validation of key fields
3. Impute missing values with median
4. Flag outliers (don't remove)
5. Standardize dates
6. Deliver to statistics team
7. Document known issues

**Output Example:**
```
Interim Analysis Dataset:
  Data cutoff: 2023-12-31
  Subjects: 456/500 enrolled
  
Cleaning Summary:
  - Processing time: 2 hours
  - Missing values: 45 (imputed)
  - Outliers flagged: 12
  - Ready for analysis: Yes
  
Notes for Statistician:
  - 3 subjects with incomplete follow-up
  - 1 site with delayed data entry
  - All outliers reviewed and plausible
```

### Pattern 3: Database Migration Cleanup

**Scenario**: Cleaning data when migrating between data management systems.

```json
{
  "migration_type": "EDC system upgrade",
  "source_system": "Legacy EDC",
  "target_system": "New Veeva",
  "challenges": [
    "Different date formats",
    "Field name changes",
    "Encoding issues"
  ],
  "validation": "Compare before/after counts"
}
```

**Workflow:**
1. Export all data from legacy system
2. Map old field names to SDTM
3. Standardize formats (dates, categories)
4. Clean missing/outlier values
5. Validate record counts match
6. Test import to new system
7. Document all transformations

**Output Example:**
```
Database Migration Results:
  Legacy records: 15,678
  Migrated records: 15,678
  Match: ✓ 100%
  
Transformations Applied:
  - Date format: 23,456 fields
  - Field names: 156 mappings
  - Missing values: 234 imputed
  - Outliers: 45 flagged
  
Validation:
  ✓ Subject counts match
  ✓ Record counts match
  ✓ Critical values preserved
  ✓ Import to new system successful
```

### Pattern 4: External Data Integration

**Scenario**: Integrating external lab data with clinical database.

```json
{
  "data_source": "Central lab",
  "integration_type": "LB domain augmentation",
  "challenges": [
    "Different units",
    "Varying reference ranges",
    "Date/time zone issues"
  ],
  "cleaning_focus": "Standardization and validation"
}
```

**Workflow:**
1. Load central lab data export
2. Map local lab codes to LBTESTCD
3. Standardize units (convert if needed)
4. Validate against reference ranges
5. Handle date/time zones
6. Merge with existing LB data
7. Validate no duplicates

**Output Example:**
```
Central Lab Integration:
  External records: 8,234
  Successfully integrated: 8,234 (100%)
  
Standardization:
  - Unit conversions: 234 records
  - Date adjustments: 8,234 records
  - Code mappings: 45 tests
  
Validation:
  ✓ No duplicate records
  ✓ All USUBJID matched
  ✓ Units standardized
  ✓ Reference ranges aligned
  
Data Quality:
  - Outliers flagged: 23
  - Missing values: 0
  - Ready for analysis: Yes
```

---

## Quality Checklist

**Pre-Cleaning:**
- [ ] **CRITICAL**: Verify input data is from validated source (EDC, not draft)
- [ ] Confirm data export date and cutoff
- [ ] Check file format (CSV/Excel) and encoding
- [ ] Verify domain specification (DM, LB, VS)
- [ ] Review study protocol for expected data structure
- [ ] Check for data lock status
- [ ] Confirm access permissions and data security
- [ ] Document raw data file location (for audit)

**Cleaning Configuration:**
- [ ] **CRITICAL**: Select appropriate missing value strategy for data type
- [ ] Choose outlier method appropriate for domain (use 'domain' for LB/VS)
- [ ] Set outlier action based on regulatory requirements (prefer 'flag')
- [ ] Review custom configuration if provided
- [ ] Confirm cleaning parameters with statistician
- [ ] Document rationale for all parameter choices
- [ ] Check if stratification needed (by site, treatment arm)
- [ ] Validate cleaning approach in Statistical Analysis Plan

**During Cleaning:**
- [ ] **CRITICAL**: Review validation warnings (missing fields)
- [ ] Check missing value imputation counts
- [ ] Review outlier detection results
- [ ] Verify flagged outliers are appropriate
- [ ] Check date standardization success rate
- [ ] Monitor for unexpected data loss
- [ ] Review cleaning log for anomalies
- [ ] Compare row counts before/after

**Post-Cleaning:**
- [ ] **CRITICAL**: Validate cleaned data against CDISC SDTM IG
- [ ] Check Pinnacle 21 (or similar) validation results
- [ ] Review all cleaning actions in audit trail
- [ ] Verify SDTM domain structure correct
- [ ] Test import to analysis software (SAS, R)
- [ ] Generate summary statistics for key variables
- [ ] Compare with expected ranges
- [ ] Document any deviations from protocol

**Regulatory Compliance:**
- [ ] **CRITICAL**: All cleaning actions documented with rationale
- [ ] Audit trail complete and archived
- [ ] Cleaning programs under version control
- [ ] Validation documentation complete
- [ ] Reviewed by independent QC (if required)
- [ ] Approved by statistician/medical monitor
- [ ] Aligned with Statistical Analysis Plan
- [ ] Ready for regulatory submission

---

## Common Pitfalls

**Data Quality Issues:**
- ❌ **Cleaning raw/draft data** → Final data different from cleaned
  - ✅ Only clean locked/validated data
  
- ❌ **Removing outliers without investigation** → Lose legitimate extreme values
  - ✅ Flag outliers; review before removing
  
- ❌ **Inappropriate imputation** → Biases statistical analysis
  - ✅ Choose strategy based on missingness mechanism
  
- ❌ **Ignoring missing patterns** → MNAR data treated as MCAR
  - ✅ Analyze missingness patterns; consult statistician

**Regulatory Issues:**
- ❌ **Incomplete audit trail** → Regulatory rejection
  - ✅ Log every single change with rationale
  
- ❌ **Changing data without documentation** → Compliance violation
  - ✅ Never modify raw data; create new cleaned dataset
  
- ❌ **Not validating against SDTM IG** → Submission issues
  - ✅ Always run CDISC validation tools
  
- ❌ **Cleaning after database lock** → Protocol violation
  - ✅ Clean before lock; any post-lock changes need documented approval

**Technical Issues:**
- ❌ **Wrong date parsing** → Incorrect temporal relationships
  - ✅ Validate date formats; check against CRFs
  
- ❌ **Unit conversion errors** → Invalid clinical values
  - ✅ Double-check all unit conversions
  
- ❌ **Subject ID mismatches** → Data linkage failures
  - ✅ Verify USUBJID consistency across domains
  
- ❌ **Overwriting original files** → Data loss
  - ✅ Always save to new file; preserve raw data

---

