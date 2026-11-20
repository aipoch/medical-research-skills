# CLI Usage Guide

## Basic Syntax

```bash
Rscript scripts/main.R [OPTIONS]
```

Analysis runs offline using a separately provisioned STRING directory. Before
a full run, follow [external data preparation](external-data.md), verify all six
files, and set `PPI_STRING_CACHE` to their absolute directory. The Skill package
does not include STRING tables.

Accepted gene-list inputs include CSV/TSV/XLSX tables and plain-text `.txt` files with one gene symbol per line.

---

## Required Arguments

These arguments are required unless `--plot_only TRUE` is used.

| Argument | Description |
|----------|-------------|
| `-g FILE`, `--genelist_file FILE` | Gene list file in CSV, TSV, TXT, or XLSX format |
| `-s SPECIES`, `--species SPECIES` | Species: `human`, `mouse`, `9606`, or `10090` |
| `-t INT`, `--threshold INT` | STRING combined-score threshold between `400` and `1000` |

---

## Optional Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `-o DIR`, `--output_dir DIR` | `output` | Output directory inside the skill root |
| `-p LOGICAL`, `--plot_only LOGICAL` | `FALSE` | Reuse `data/ppi_result.rds` and regenerate the plot |
| `-d INT`, `--seed INT` | `42` | Random seed for reproducible layouts |
| `-u INT`, `--timeout_seconds INT` | `600` | Elapsed time limit |
| `--string_cache_dir DIR` | `references/string_cache` (unpopulated) | Supply the verified external data directory for a full run |
| `--string_version TEXT` | `auto` | Pass `v11.5` for the supplied dataset; `auto` selects each table independently |
| `--figure_family TEXT` | `sans` | PDF font family |
| `--figure_width NUM` | `12` | Plot width in inches |
| `--figure_height NUM` | `10` | Plot height in inches |
| `--label TEXT` | `node` | Label mode: `node` or `none` |
| `--label_size NUM` | `0.8` | Label size |
| `--label_color TEXT` | `black` | Label color |
| `--label_dist NUM` | `0` | Label distance from node center |
| `--line_alpha NUM` | `1` | Edge alpha |
| `--line_color TEXT` | built-in palette | Comma-separated edge colors |
| `--line_size NUM` | `0.8` | Base edge width |
| `--line_type TEXT` | `solid` | Edge line type |
| `--mapping_link_alpha TEXT` | `value` | Map edge alpha from interaction score |
| `--mapping_link_color TEXT` | `value` | Map edge color from interaction score |
| `--mapping_link_size TEXT` | `value` | Map edge width from interaction score |
| `--mapping_node_alpha TEXT` | `none` | Map node alpha from degree |
| `--mapping_node_color TEXT` | `none` | Map node color from degree |
| `--mapping_node_size TEXT` | `value` | Map node size from degree |
| `--point_alpha NUM` | `1` | Node alpha |
| `--point_color TEXT` | built-in palette | Comma-separated node border colors |
| `--point_fill TEXT` | built-in palette | Comma-separated node fill colors |
| `--point_shape TEXT` | `circle` | Node shape |
| `--point_size NUM` | `12` | Base node size |
| `--style_layout TEXT` | `nicely` | Layout style: `kk`, `fr`, `nicely`, `circle`, `star`, `grid`, or `randomly` |
| `--style_line TEXT` | `straight` | Edge style: `straight` or `curve` |
| `--theme_size NUM` | `0.8` | Compatibility placeholder |
| `--title TEXT` | empty | Main plot title |

---

## Offline Cache Notes

The skill requires local STRING cache files for the selected species.

Expected files per species:

- `<species_id>.protein.aliases.<version>.txt.gz`
- `<species_id>.protein.info.<version>.txt.gz`
- `<species_id>.protein.links.<version>.txt.gz`

Examples:

- human: `9606.protein.aliases.v11.5.txt.gz`
- mouse: `10090.protein.links.v11.5.txt.gz`

Use explicit `--string_version v11.5` with the verified dataset. The existing
`auto` mode selects the newest version of each table independently and can mix
versions in an inconsistent directory.

---

## Complete Examples

The commands below now use the external dataset. The recorded output sizes and
runtime measurements are historical upstream observations from 2026-04-22; they
are not new measurements of this packaging change.

### Example 1: Basic Human Run

```bash
Rscript scripts/main.R \
  --genelist_file tests/data/gene_list.csv \
  --species human \
  --threshold 700 \
  --string_cache_dir "$PPI_STRING_CACHE" \
  --string_version v11.5 \
  --output_dir tests/output/basic-run
```

### Output Files

| File | Size |
|------|------|
| `data/ppi_result.rds` | `2.75 KB (2815 bytes)` |
| `plot/ppi_network_plot.pdf` | `5.50 KB (5632 bytes)` |
| `session_info.txt` | `1.18 KB (1213 bytes)` |
| `table/ppi_network_edges.xlsx` | `6.60 KB (6757 bytes)` |
| `table/ppi_network_nodes.xlsx` | `6.43 KB (6588 bytes)` |
| `table/ppi_summary.csv` | `128 B (128 bytes)` |

### Runtime and Resource Usage

| Metric | Value |
|--------|-------|
| Start time | `2026-04-22 09:16:55` |
| End time | `2026-04-22 09:17:32` |
| Exit code | `0` |
| Timing mode | `shell` |
| Wall-clock time | `37.164` |
| User CPU time | `29.562` |
| System CPU time | `2.690` |
| Max resident set size | `Not recorded by time tool` |
| Cgroup peak memory | `5.98 GB (6424145920 bytes)` |
| Cgroup current memory | `699.38 MB (733347840 bytes)` |
| Cgroup peak before run | `5.98 GB (6424145920 bytes)` |
| Auxiliary logs saved | `no` |

### Example 2: Custom Plot Styling

```bash
Rscript scripts/main.R \
  --genelist_file tests/data/gene_list.csv \
  --species 9606 \
  --threshold 700 \
  --string_cache_dir "$PPI_STRING_CACHE" \
  --string_version v11.5 \
  --output_dir tests/output/styled-run \
  --style_layout circle \
  --style_line curve \
  --label node \
  --label_size 0.9 \
  --title "PPI Network"
```

### Output Files

| File | Size |
|------|------|
| `data/ppi_result.rds` | `2.75 KB (2815 bytes)` |
| `plot/ppi_network_plot.pdf` | `10.32 KB (10568 bytes)` |
| `session_info.txt` | `1.18 KB (1213 bytes)` |
| `table/ppi_network_edges.xlsx` | `6.60 KB (6757 bytes)` |
| `table/ppi_network_nodes.xlsx` | `6.43 KB (6588 bytes)` |
| `table/ppi_summary.csv` | `128 B (128 bytes)` |

### Runtime and Resource Usage

| Metric | Value |
|--------|-------|
| Start time | `2026-04-22 09:19:07` |
| End time | `2026-04-22 09:19:42` |
| Exit code | `0` |
| Timing mode | `shell` |
| Wall-clock time | `35.447` |
| User CPU time | `29.004` |
| System CPU time | `2.674` |
| Max resident set size | `Not recorded by time tool` |
| Cgroup peak memory | `5.98 GB (6424145920 bytes)` |
| Cgroup current memory | `698.24 MB (732160000 bytes)` |
| Cgroup peak before run | `5.98 GB (6424145920 bytes)` |
| Auxiliary logs saved | `no` |

### Example 3: Plot-Only Regeneration

```bash
Rscript scripts/main.R \
  --plot_only TRUE \
  --output_dir tests/output/basic-run \
  --seed 42
```

### Output Files

| File | Size |
|------|------|
| `data/ppi_result.rds` | `2.75 KB (2815 bytes)` |
| `plot/ppi_network_plot.pdf` | `5.50 KB (5632 bytes)` |
| `session_info.txt` | `1.17 KB (1196 bytes)` |
| `table/ppi_network_edges.xlsx` | `6.60 KB (6757 bytes)` |
| `table/ppi_network_nodes.xlsx` | `6.43 KB (6588 bytes)` |
| `table/ppi_summary.csv` | `128 B (128 bytes)` |

### Runtime and Resource Usage

| Metric | Value |
|--------|-------|
| Start time | `2026-04-22 09:18:16` |
| End time | `2026-04-22 09:18:17` |
| Exit code | `0` |
| Timing mode | `shell` |
| Wall-clock time | `0.873` |
| User CPU time | `1.129` |
| System CPU time | `1.206` |
| Max resident set size | `Not recorded by time tool` |
| Cgroup peak memory | `5.98 GB (6424145920 bytes)` |
| Cgroup current memory | `699.39 MB (733368320 bytes)` |
| Cgroup peak before run | `5.98 GB (6424145920 bytes)` |
| Auxiliary logs saved | `no` |

### Example 4: Use A Custom STRING Cache Directory

```bash
Rscript scripts/main.R \
  --genelist_file tests/data/gene_list.csv \
  --species human \
  --threshold 700 \
  --string_cache_dir "$PPI_STRING_CACHE" \
  --string_version v11.5 \
  --output_dir tests/output/custom-cache-run
```

### Output Files

| File | Size |
|------|------|
| `data/ppi_result.rds` | `2.75 KB (2815 bytes)` |
| `plot/ppi_network_plot.pdf` | `5.50 KB (5632 bytes)` |
| `session_info.txt` | `1.18 KB (1213 bytes)` |
| `table/ppi_network_edges.xlsx` | `6.60 KB (6757 bytes)` |
| `table/ppi_network_nodes.xlsx` | `6.43 KB (6588 bytes)` |
| `table/ppi_summary.csv` | `128 B (128 bytes)` |

### Runtime and Resource Usage

| Metric | Value |
|--------|-------|
| Start time | `2026-04-22 09:14:55` |
| End time | `2026-04-22 09:15:30` |
| Exit code | `0` |
| Timing mode | `shell` |
| Wall-clock time | `35.571` |
| User CPU time | `28.704` |
| System CPU time | `2.830` |
| Max resident set size | `Not recorded by time tool` |
| Cgroup peak memory | `5.98 GB (6424145920 bytes)` |
| Cgroup current memory | `702.87 MB (737009664 bytes)` |
| Cgroup peak before run | `5.98 GB (6424145920 bytes)` |
| Auxiliary logs saved | `no` |

---

## Getting Help

```bash
Rscript scripts/main.R --help
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Error |

---

## Notes

- Runtime progress is printed to stdout/stderr.
- No extra audit text files are generated in this version.
