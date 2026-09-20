---
name: ppi-network-analysis
description: Use when you need a standardized R CLI workflow to build a protein-protein interaction network from a local gene list and an offline STRING cache, export node and edge tables, and render a reproducible PDF network plot. NOT for online API fetching, arbitrary graph databases, multi-omics integration, or non-STRING interaction sources.
license: MIT
author: AIPOCH
---
> **Source**: [https://github.com/aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)

# PPI Network Analysis

## When to Read External Files

| Situation | File to Read | Purpose |
|-----------|--------------|---------|
| Preparing a full analysis or missing the STRING dataset | `references/external-data.md` | Provision and verify the external v11.5 dataset before analysis |
| Need algorithm details | `references/algorithm.md` | Explain local STRING mapping, interaction filtering, network metrics, and plot interpretation |
| Need to execute the analysis | `scripts/main.R` | Run the CLI entry point with a complete `Rscript` command |
| Encounter an error | `references/troubleshooting.md` | Map standardized error codes to causes and fixes |
| Need CLI examples or baseline usage | `references/cli-guide.md` | Review installation notes, offline cache requirements, and runnable examples |
| Need a runnable smoke test | `tests/data/` | Use the bundled small gene list for verification |

## Usage

Before a full analysis, follow `references/external-data.md` to prepare the six
STRING v11.5 files outside the installed Skill. Set `PPI_STRING_CACHE` to that
verified directory. The Skill package contains the gene-list example, code and
documentation; STRING tables are provisioned separately. If the directory or
required files are unavailable, stop and complete that preparation first.

```bash
Rscript scripts/main.R \
  --genelist_file ./input/gene_list.csv \
  --species human \
  --threshold 700 \
  --string_cache_dir "$PPI_STRING_CACHE" \
  --string_version v11.5 \
  --output_dir output/basic-run \
  --seed 42 \
  --timeout_seconds 600
```

```bash
Rscript scripts/main.R \
  --plot_only TRUE \
  --output_dir output/basic-run \
  --seed 42 \
  --timeout_seconds 600
```

## Arguments

| Short | Long | Type | Default | Required | Description |
|-------|------|------|---------|----------|-------------|
| `-g` | `--genelist_file` | character | none | yes, unless `--plot_only TRUE` | Gene list file in CSV, TSV, TXT, or XLSX format |
| `-s` | `--species` | character | none | yes, unless `--plot_only TRUE` | Species: `human`, `mouse`, `9606`, or `10090` |
| `-t` | `--threshold` | integer | none | yes, unless `--plot_only TRUE` | STRING combined-score threshold from `400` to `1000` |
| `-o` | `--output_dir` | character | `output` | no | Output directory inside the skill root |
| `-p` | `--plot_only` | logical | `FALSE` | no | Reuse `output_dir/data/ppi_result.rds` and regenerate the network plot |
| `-d` | `--seed` | integer | `42` | no | Random seed used for layout reproducibility |
| `-u` | `--timeout_seconds` | integer | `600` | no | Elapsed time limit in seconds |
|  | `--string_cache_dir` | character | `references/string_cache` (unpopulated) | supply for full analysis | Verified external STRING data directory; see `references/external-data.md` |
|  | `--string_version` | character | `auto` | no | Use explicit `v11.5` for the separately provisioned dataset; `auto` selects each table independently |
|  | `--figure_family` | character | `sans` | no | PDF font family: `sans`, `serif`, or `mono` |
|  | `--figure_width` | numeric | `12` | no | Plot width in inches |
|  | `--figure_height` | numeric | `10` | no | Plot height in inches |
|  | `--label` | character | `node` | no | Label mode: `node` or `none` |
|  | `--label_size` | numeric | `0.8` | no | Label size |
|  | `--label_color` | character | `black` | no | Label color |
|  | `--label_dist` | numeric | `0` | no | Label distance from the node center |
|  | `--line_alpha` | numeric | `1` | no | Edge alpha |
|  | `--line_color` | character | built-in palette | no | Comma-separated edge colors |
|  | `--line_size` | numeric | `0.8` | no | Base edge width |
|  | `--line_type` | character | `solid` | no | Edge line type; supported values in plotting are `solid`, `dashed`, or `dotted` |
|  | `--mapping_link_alpha` | character | `value` | no | Map edge alpha from interaction score: `value` or `none` |
|  | `--mapping_link_color` | character | `value` | no | Map edge color from interaction score: `value` or `none` |
|  | `--mapping_link_size` | character | `value` | no | Map edge width from interaction score: `value` or `none` |
|  | `--mapping_node_alpha` | character | `none` | no | Map node alpha from degree: `value` or `none` |
|  | `--mapping_node_color` | character | `none` | no | Map node color from degree: `value` or `none` |
|  | `--mapping_node_size` | character | `value` | no | Map node size from degree: `value` or `none` |
|  | `--point_alpha` | numeric | `1` | no | Node alpha |
|  | `--point_color` | character | built-in palette | no | Comma-separated node border colors |
|  | `--point_fill` | character | built-in palette | no | Comma-separated node fill colors |
|  | `--point_shape` | character | `circle` | no | Node shape: `circle` or `square` |
|  | `--point_size` | numeric | `12` | no | Base node size |
|  | `--style_layout` | character | `nicely` | no | Layout style: `kk`, `fr`, `nicely`, `circle`, `star`, `grid`, or `randomly` |
|  | `--style_line` | character | `straight` | no | Edge style: `straight` or `curve` |
|  | `--theme_size` | numeric | `0.8` | no | Theme size placeholder retained for compatibility |
|  | `--title` | character | empty | no | Main plot title |

## Input Format

### Supported input types

`--genelist_file` accepts the following formats:
- `.csv`
- `.tsv`
- `.txt`
- `.xlsx`

### Gene list parsing rules

- Plain-text `.txt` files can be provided as one gene symbol per line without a header.
- For `.csv`, `.tsv`, and `.xlsx`, the tool automatically selects a likely gene column.
- Preferred column names include: `gene`, `genes`, `genename`, `genesymbol`, `symbol`, `hgnc`, `hgncsymbol`, `mgi`, `ensembl`, `ensemblgeneid`, `geneid`, and `id`.
- If no standard gene column name is found, the tool falls back to the column with the strongest non-numeric signal.
- Values may contain multiple genes separated by commas, semicolons, pipes, tabs, or spaces; these are split automatically.
- Empty inputs, unsupported file extensions, or inputs with no parsable genes will raise a `SKILL_EMPTY_DATA` or `SKILL_INVALID_PARAMETER` error.

### Minimal examples

#### TXT example

```text
TP53
EGFR
BRCA1
MYC
```

#### CSV example

```csv
gene
TP53
EGFR
BRCA1
MYC
```

## Output Files

| File | Format | Description |
|------|--------|-------------|
| `data/ppi_result.rds` | RDS | Serialized PPI bundle with mappings, interactions, nodes, summary, and metadata |
| `table/ppi_network_edges.xlsx` | XLSX | Edge table with `from`, `to`, and `combined_score` |
| `table/ppi_network_nodes.xlsx` | XLSX | Node table with `gene`, `degree`, `betweenness`, and `closeness` |
| `table/ppi_summary.csv` | CSV | Summary metrics for input genes, mapped genes, unmapped genes, nodes, edges, and threshold |
| `plot/ppi_network_plot.pdf` | PDF | Rendered PPI network plot from the local STRING interaction graph |
| `session_info.txt` | TXT | R version, platform, and package version information |

## Error Handling

| Error Code | Meaning | How to Fix |
|-----------|---------|------------|
| `SKILL_FILE_NOT_FOUND` | Input gene list, STRING cache directory, required cache files, or `data/ppi_result.rds` in plot-only mode was not found | Confirm the path exists, required cache files are present, and run a full analysis before `--plot_only TRUE` |
| `SKILL_EMPTY_DATA` | No valid genes were parsed, no genes mapped to STRING, fewer than two mapped STRING IDs remained, no interactions passed filtering, or the interaction table was empty for plotting | Check that the input is not empty, verify gene symbols are supported by the local STRING cache, and lower the threshold if the network is too sparse |
| `SKILL_INVALID_PARAMETER` | A required argument is missing, a numeric value is out of range, an unsupported choice was supplied, the output path is invalid, or the input extension is unsupported | Recheck the parameter value and allowed choices, especially `--species`, `--threshold`, mapping options, plot options, and output paths |
| `SKILL_MISSING_COLUMNS` | Required columns were not found in a STRING cache table | Confirm the local aliases, info, and links files are valid STRING cache files with expected columns |
| `SKILL_PACKAGE_NOT_FOUND` | Required R packages are not installed | Install the missing packages listed in the error message before rerunning |

Detailed fixes and troubleshooting steps: READ `references/troubleshooting.md`

## Testing

### Smoke test with the bundled gene list and external STRING data

```bash
Rscript scripts/main.R \
  --genelist_file tests/data/gene_list.csv \
  --species human \
  --threshold 700 \
  --string_cache_dir "$PPI_STRING_CACHE" \
  --string_version v11.5 \
  --output_dir tests/output/basic-run
```

### Plot-only regeneration test

```bash
Rscript scripts/main.R \
  --plot_only TRUE \
  --output_dir tests/output/basic-run \
  --seed 42
```

### Expected outputs after test

- `tests/output/basic-run/data/ppi_result.rds`
- `tests/output/basic-run/table/ppi_network_edges.xlsx`
- `tests/output/basic-run/table/ppi_network_nodes.xlsx`
- `tests/output/basic-run/table/ppi_summary.csv`
- `tests/output/basic-run/plot/ppi_network_plot.pdf`
- `tests/output/basic-run/session_info.txt`
