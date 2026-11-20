# Algorithm Details

## Method Overview

This skill builds a protein-protein interaction (PPI) network from a user-supplied gene list by using a fully local STRING cache. The workflow does not call any online APIs and does not depend on remote services during execution.

At a high level, the workflow is:

1. Read a gene list from CSV, TSV, TXT, or XLSX.
2. Parse and normalize gene identifiers from the input.
3. Normalize the species setting to a supported STRING taxonomy ID.
4. Locate local STRING cache files for aliases, protein metadata, and links.
5. Map input genes to STRING protein identifiers using the aliases table.
6. Filter local interactions by the requested combined-score threshold.
7. Convert STRING IDs back to gene symbols.
8. Build an undirected interaction graph with `igraph`.
9. Compute node-level centrality metrics.
10. Export network tables, a summary table, a serialized bundle, and a PDF plot.

## Input Parsing and Gene Normalization

### Supported input formats

The skill accepts the following gene-list formats:
- CSV
- TSV
- TXT
- XLSX

### Parsing strategy

- Plain-text `.txt` files may contain one gene symbol per line without a header.
- Table-based files (`.csv`, `.tsv`, `.xlsx`) are parsed by selecting the most likely gene column.
- Preferred column names include `gene`, `genes`, `genename`, `genesymbol`, `symbol`, `hgnc`, `hgncsymbol`, `mgi`, `ensembl`, `ensemblgeneid`, `geneid`, and `id`.
- If none of these standard names are present, the parser falls back to the column with the strongest non-numeric signal.
- Multiple genes in a single cell are automatically split on commas, semicolons, pipes, tabs, or whitespace.
- Empty values, missing values, and duplicate genes are removed before downstream analysis.

### Failure conditions during input parsing

The parser raises an error when:
- the file extension is unsupported,
- the workbook is empty,
- no gene-like values can be extracted, or
- the final parsed gene set is empty.

## Species Resolution

The skill supports two organisms:
- human (`human`, `Homo sapiens`, `9606`)
- mouse (`mouse`, `Mus musculus`, `10090`)

The supplied species label is normalized to a canonical internal representation containing:
- species name,
- STRING taxonomy ID,
- Latin species name.

This normalized species metadata is then used to locate the matching local STRING cache files.

## Local STRING Cache Requirements

The analysis runs from a separately provisioned directory passed with
`--string_cache_dir`; see [external data preparation](external-data.md). It
requires three STRING tables for the selected species:

- aliases file
- protein info file
- protein links file

For example, a valid human cache version may include:
- `9606.protein.aliases.v11.5.txt.gz`
- `9606.protein.info.v11.5.txt.gz`
- `9606.protein.links.v11.5.txt.gz`

Pass `--string_version v11.5` for the verified external dataset. All three files
for the selected species must match that version. The existing `auto` mode
selects each table independently and can mix versions if the directory contains
an incomplete set of newer tables.

## Gene-to-STRING Mapping Logic

### Mapping process

Input genes are mapped to STRING proteins through the local aliases table.

The mapping workflow is:

1. Read the aliases table and the protein info table.
2. Detect the STRING protein ID column and alias/symbol column.
3. Convert both input genes and alias symbols to uppercase for case-insensitive matching.
4. Match each input gene to a STRING protein ID using the aliases table.
5. Remove unmapped genes.
6. Keep one mapping per gene after de-duplication.
7. Join protein metadata from the info table when available.

### Practical implications

- Mapping success depends on whether the supplied identifiers are represented in the local aliases table.
- Unsupported symbols, outdated names, or identifiers absent from the local cache remain unmapped.
- If no genes map to STRING, the analysis stops with `SKILL_EMPTY_DATA`.

## Interaction Filtering

After mapping, the skill extracts interactions from the local STRING links table.

### Filtering rule

Only interactions that satisfy both conditions are kept:

1. both endpoints are in the mapped STRING ID set;
2. `combined_score >= threshold`

The threshold must be an integer between `400` and `1000`.

### Threshold interpretation

- Lower thresholds keep more edges and may produce denser but less stringent networks.
- Higher thresholds keep fewer edges and usually emphasize higher-confidence STRING relationships.
- The entry script emits a warning when the threshold is below `700`, suggesting that larger values may be preferable for higher-confidence networks.

If no interactions remain after filtering, the analysis stops with `SKILL_EMPTY_DATA`.

## Graph Construction

The filtered STRING edges are converted back from STRING protein IDs to gene symbols and then cleaned before graph construction.

### Cleaning steps

- Remove edges with missing mapped gene symbols.
- Remove self-loops where the source and target map to the same gene symbol.
- Remove duplicate edges.

### Graph model

The final network is built as an undirected graph using `igraph::graph_from_data_frame(..., directed = FALSE)`.

This means:
- the graph is treated as non-directional,
- each node corresponds to a gene symbol,
- each edge corresponds to a retained STRING interaction.

## Network Metrics

After the graph is built, the skill computes three node-level centrality metrics.

### 1. Degree

Degree is the number of edges connected to a node.

Interpretation:
- Higher degree suggests that a gene is connected to more genes in the retained network.
- Nodes with high degree may act as hubs in the local interaction graph.

### 2. Betweenness

Betweenness is computed with normalized undirected betweenness centrality.

Interpretation:
- Higher betweenness suggests that a gene lies on more shortest paths between other nodes.
- Such nodes may bridge subnetwork structure or connect otherwise weakly linked regions.

### 3. Closeness

Closeness is computed as normalized closeness centrality.

Interpretation:
- Higher closeness suggests that a node is, on average, closer to all other reachable nodes in the graph.
- Nodes with high closeness may be relatively central in the retained network topology.

These metrics are exported in the node table and are intended as structural summaries of the final filtered network.

## Output Logic

A successful run produces:

- serialized bundle: `data/ppi_result.rds`
- edge table: `table/ppi_network_edges.xlsx`
- node table: `table/ppi_network_nodes.xlsx`
- summary table: `table/ppi_summary.csv`
- network plot: `plot/ppi_network_plot.pdf`
- session information: `session_info.txt`

### Summary table content

The summary table records the following metrics:
- number of input genes,
- number of mapped genes,
- number of unmapped genes,
- number of nodes in the network,
- number of edges in the network,
- threshold used.

## Plotting Logic

The network plot is generated from the retained graph and supports configurable layout, node appearance, edge appearance, labels, and title.

### Reproducibility controls

- `--seed` controls layout reproducibility for stochastic layouts.
- `--figure_width`, `--figure_height`, and `--figure_family` control PDF rendering.
- Mapping options can encode edge score or node degree into color, alpha, or size.

### Plot-only mode

When `--plot_only TRUE` is used, the tool reuses an existing `data/ppi_result.rds` bundle in `output_dir` and regenerates only the plot. A full run must therefore be completed once before plot-only mode can succeed.

## Reproducibility Notes

- The workflow is deterministic except for layout components controlled by `--seed`.
- `session_info.txt` records the R runtime and package versions.
- The skill writes outputs only inside the skill root.
- The analysis does not execute user input through `eval()`, `exec()`, or shell interpolation.

## Method Limitations

- The network depends entirely on the local STRING cache and does not query current online STRING content.
- Only human and mouse are supported.
- Network size and density depend strongly on input-gene coverage and the selected threshold.
- Unmapped genes are excluded from the final network.
- The plotted network is a filtered interaction view, not a causal or directional pathway model.
- This skill is designed for local STRING-based PPI construction and is not intended for arbitrary graph databases, multi-omics integration, or non-STRING interaction sources.
