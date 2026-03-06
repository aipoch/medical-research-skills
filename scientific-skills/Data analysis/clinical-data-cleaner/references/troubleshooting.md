## Troubleshooting

**Problem: Validation fails with missing required fields**
- Symptoms: Error listing missing SDTM fields
- Causes:
  - Data export missing columns
  - Field names different from SDTM
  - Partial data extract
- Solutions:
  - Check data export settings
  - Map field names to SDTM standards
  - Export complete dataset

**Problem: Too many outliers detected**
- Symptoms: >20% of data flagged as outliers
- Causes:
  - Wrong detection method for data distribution
  - Data quality issues
  - Incorrect units
- Solutions:
  - Use domain-specific thresholds for clinical data
  - Review raw data for systematic errors
  - Verify unit consistency

**Problem: Date parsing errors**
- Symptoms: Many dates converted to NaT (Not a Time)
- Causes:
  - Mixed date formats in source
  - Non-standard date strings
  - International date confusion (DD/MM vs MM/DD)
- Solutions:
  - Standardize date format in source system
  - Specify date format explicitly
  - Manually review unparseable dates

**Problem: Imputation creates unrealistic values**
- Symptoms: Imputed values outside plausible range
- Causes:
  - Wrong imputation strategy
  - Highly skewed data
  - Different subgroups mixed
- Solutions:
  - Use median instead of mean for skewed data
  - Impute within relevant subgroups
  - Consider multiple imputation

**Problem: Cleaned data larger than original**
- Symptoms: Output file bigger than input
- Causes:
  - Outlier flag columns added
  - Date format expanded (added time)
  - String columns widened
- Solutions:
  - Normal behavior - audit columns add size
  - Compress if needed for storage
  - Archive raw and cleaned separately

**Problem: Memory errors with large datasets**
- Symptoms: "MemoryError" or system freeze
- Causes:
  - Dataset too large for available RAM
  - Inefficient data types
  - Memory leaks in processing
- Solutions:
  - Process data in chunks
  - Optimize data types (categorical, smaller floats)
  - Use cloud-based processing for very large datasets
  - Consider database-based cleaning

---

