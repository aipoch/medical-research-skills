---
name: citation-chasing-mapping
description: Use when identifying seminal papers in a research field, mapping research lineage and intellectual heritage, discovering related work through reference tracking, or finding potential collaborators through co-citation analysis. Maps citation networks to trace research evolution, identify influential papers, and discover hidden connections in scientific literature. Supports systematic reviews, bibliometric analysis, and research planning through comprehensive citation tracking.
allowed-tools: "Read Write Bash Edit"
license: MIT
metadata:
  skill-author: AIPOCH
  version: "1.0"
---

# Scientific Citation Network and Knowledge Mapper

## When to Use This Skill

- identifying seminal papers in a research field
- mapping research lineage and intellectual heritage
- discovering related work through reference tracking
- finding potential collaborators through co-citation analysis
- tracking citation patterns to identify research trends
- building literature reviews with comprehensive coverage

## Quick Start

```python
from scripts.main import CitationChasingMapping

# Initialize the tool
tool = CitationChasingMapping()

from scripts.citation_mapper import CitationNetworkMapper

mapper = CitationNetworkMapper(data_source="PubMed")

# Build citation network from seed paper
network = mapper.build_network(
    seed_paper={
        "pmid": "12345678",
        "title": "Breakthrough Discovery in Immunotherapy"
    },
    backward_depth=2,  # references of references
    forward_depth=2,   # citing papers of citing papers
    max_papers=500
)

# Identify seminal papers
seminal_papers = mapper.identify_seminal_works(
    network=network,
    min_citations=100,
    centrality_threshold=0.8
)

print(f"Found {len(seminal_papers)} highly influential papers:")
for paper in seminal_papers[:5]:
    print(f"  - {paper.title} (cited {paper.citation_count} times)")

# Find research clusters
clusters = mapper.identify_research_clusters(
    network=network,
    algorithm="louvain",
    min_cluster_size=10
)

# Generate collaboration map
collaboration_map = mapper.generate_collaboration_network(
    network=network,
    institution_field="affiliation"
)

# Create visualization
mapper.visualize_network(
    network=network,
    layout="force_directed",
    color_by="publication_year",
    size_by="citation_count",
    output_file="citation_network.pdf"
)
```

## Core Capabilities

### 1. Build Comprehensive Citation Networks

Construct bidirectional citation graphs from seed papers with configurable depth.

```python
# Build network from multiple seed papers
network = mapper.build_network(
    seed_papers=[
        {"pmid": "12345678", "title": "Original Discovery"},
        {"pmid": "87654321", "title": "Follow-up Study"}
    ],
    backward_depth=3,  # References
    forward_depth=2,   # Citing papers
    max_papers=1000,
    include_citations=True
)

# Export network for Gephi
mapper.export_network(network, format="gexf", file="network.gexf")
```

### 2. Identify Seminal Works

Use centrality metrics to find field-defining papers.

```python
# Calculate centrality metrics
centrality = mapper.calculate_centrality(
    network=network,
    metrics=["betweenness", "eigenvector", "pagerank"]
)

# Identify seminal papers
seminal = mapper.identify_seminal_works(
    centrality=centrality,
    min_citations=100,
    top_n=20
)

for paper in seminal:
    print(f"{paper.title}: {paper.centrality_score}")
```

### 3. Discover Research Clusters

Detect communities and emerging research topics.

```python
# Detect research clusters
clusters = mapper.detect_clusters(
    network=network,
    algorithm="louvain",
    resolution=1.0
)

# Analyze cluster topics
for cluster_id, cluster in clusters.items():
    topic = mapper.extract_cluster_topic(cluster)
    print(f"Cluster {cluster_id}: {topic}")
    print(f"  Size: {cluster.size} papers")
    print(f"  Growth rate: {cluster.growth_rate}")
```

### 4. Generate Interactive Visualizations

Create publication-ready network visualizations.

```python
# Create interactive visualization
viz = mapper.visualize(
    network=network,
    layout="force_directed",
    node_color="publication_year",
    node_size="citation_count",
    edge_color="citation_type",
    interactive=True
)

# Save as HTML for web
viz.save_html("citation_network.html")

# Save static for publication
viz.save_pdf("figure_1.pdf", dpi=300)
```

## Command Line Usage

```bash
python scripts/main.py --seed-pmid 12345678 --depth 2 --max-papers 500 --output network.json --visualize
```

## Best Practices

- Start with high-quality seed papers
- Set reasonable depth limits to avoid noise
- Validate key papers through multiple sources
- Update networks regularly as literature evolves

## Quality Checklist

Before using this skill, ensure you have:
- [ ] Clear understanding of your objectives
- [ ] Necessary input data prepared and validated
- [ ] Output requirements defined
- [ ] Reviewed relevant documentation

After using this skill, verify:
- [ ] Results meet your quality standards
- [ ] Outputs are properly formatted
- [ ] Any errors or warnings have been addressed
- [ ] Results are documented appropriately

## References

- `references/guide.md` - Comprehensive user guide
- `references/examples/` - Working code examples
- `references/api-docs/` - Complete API documentation

---

**Skill ID**: 193 | **Version**: 1.0 | **License**: MIT
