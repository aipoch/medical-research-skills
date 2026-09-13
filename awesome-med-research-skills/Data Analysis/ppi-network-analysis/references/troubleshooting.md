# Troubleshooting Guide

## Common Errors

### `SKILL_FILE_NOT_FOUND`

Meaning:

- The input gene list file does not exist.
- The requested STRING cache directory does not exist or is not a directory.
- Required STRING cache files are missing for the selected species.
- `--plot_only TRUE` was used before `data/ppi_result.rds` had been created.

How to fix:

- Confirm the input file path is correct.
- Complete [external data preparation](external-data.md), including SHA-256
  verification. STRING tables are outside the installed Skill.
- Pass that existing directory with `--string_cache_dir` and select
  `--string_version v11.5`; the default `references/string_cache` is unpopulated.
- Ensure the cache directory contains the required aliases, info, and links files for the selected species, such as:
  - `9606.protein.aliases.v11.5.txt.gz`
  - `9606.protein.info.v11.5.txt.gz`
  - `9606.protein.links.v11.5.txt.gz`
- For plot-only mode, run a full analysis first so `output_dir/data/ppi_result.rds` is created.

---

### `SKILL_EMPTY_DATA`

Meaning:

- No valid genes were parsed from the input file.
- The Excel workbook was empty.
- No genes mapped to STRING from the local cache.
- Fewer than two mapped STRING IDs remained, so a network could not be built.
- No STRING interactions remained after threshold filtering.
- No valid gene-symbol interactions remained after STRING ID mapping.
- The interaction table was empty when the plot step started.

How to fix:

- Confirm the gene list is not empty.
- Check that gene symbols are valid and supported by the local STRING aliases table.
- If using CSV, TSV, or XLSX, confirm the gene column is readable and contains gene identifiers rather than only numeric values.
- Lower `--threshold` if the network is too sparse.
- Check console `[WARN]` and `[ERROR]` messages for the last failure point.

---

### `SKILL_INVALID_PARAMETER`

Meaning:

- A required parameter was not provided.
- A numeric parameter was out of range or not positive.
- A choice parameter used an unsupported value.
- The input file extension is unsupported.
- The output directory was empty or attempted to escape the skill root.
- The species label was unsupported.

Typical triggers:

- Missing `--species` or `--threshold` when `--plot_only FALSE`
- `--threshold` outside `400` to `1000`
- `--seed` or `--timeout_seconds` not positive integers
- `--line_alpha` or `--point_alpha` outside `0` to `1`
- Unsupported values for:
  - `--species`
  - `--figure_family`
  - `--label`
  - `--point_shape`
  - `--style_layout`
  - `--style_line`
  - `--mapping_link_alpha`
  - `--mapping_link_color`
  - `--mapping_link_size`
  - `--mapping_node_alpha`
  - `--mapping_node_color`
  - `--mapping_node_size`

How to fix:

- Re-run with `Rscript scripts/main.R --help` to review valid arguments.
- Confirm required arguments are supplied.
- Check numeric ranges and choice values carefully.
- Use only supported species values: `human`, `mouse`, `9606`, or `10090`.
- Keep `--output_dir` inside the skill root.
- Use only supported input types: CSV, TSV, TXT, or XLSX.

---

### `SKILL_MISSING_COLUMNS`

Meaning:

- A required column was missing from a parsed STRING cache table.
- The aliases, info, or links file was present but did not contain the expected columns.

How to fix:

- Verify that the cache files are genuine STRING export files.
- Check whether the aliases table includes an ID column and an alias/symbol column.
- Check whether the info table includes a STRING protein ID column.
- Check whether the links table includes source node, target node, and score columns.
- Replace corrupted or incompatible cache files with the correct STRING cache version.

---

### `SKILL_PACKAGE_NOT_FOUND`

Meaning:

- One or more required R packages were not installed.

Typical packages checked by the entry script:

- `optparse`
- `dplyr`
- `openxlsx`
- `igraph`

How to fix:

- Install the missing package(s) reported in the error message.
- Example:

```r
install.packages(c("optparse", "dplyr", "openxlsx", "igraph"))
```

- Then rerun the command.

---

## Additional Checks

- Review console logs with `[INFO]`, `[WARN]`, and `[ERROR]` prefixes to locate the last successful step before failure.
- Inspect `session_info.txt` when reproducing package-version differences.
- If `--plot_only TRUE` fails, verify that `output_dir/data/ppi_result.rds` already exists from a previous successful run.
- If a custom cache directory is used, confirm the selected species has matching aliases, info, and links files in the same cache version.
