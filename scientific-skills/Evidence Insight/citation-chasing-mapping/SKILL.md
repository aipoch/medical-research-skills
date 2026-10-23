---
name: citation-chasing-mapping
description: Use to map research lineage from supplied or otherwise authorized citation metadata by tracing references and citing works. Produces a bounded, source-attributed citation map; it does not retrieve papers or provide clinical advice.
license: MIT
author: AIPOCH
---
> **Source**: [https://github.com/aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)

# Citation Chasing and Mapping

## When to use

Use this workflow to trace backward references and forward citations from one or more seed works, summarize the resulting research lineage, and identify candidate influential works for further review. It is a manual, metadata-only workflow: this skill package does not include an executable, API client, reference database, or local reference guide.

Do not use it to make clinical decisions, recommend treatment, infer scientific validity from citation counts, or claim comprehensive coverage without a defined and verified source set.

## Inputs and limits

Before starting, establish:

- Seed works, identified by a stable identifier where available (for example DOI, PMID, or a source-local ID).
- The authorized citation metadata and its source. Use records supplied for the task or data the user is authorized to provide; do not imply that this skill fetches data.
- Direction(s) and depth: backward references, forward citing works, or both.
- A work-count and date/time boundary, if needed to keep the map manageable.
- Desired output and any exclusions.

Citation metadata may include title, authors as listed by the source, year, venue, identifiers, reference links, citing-work links, and retrieval/source date. Do not add paper content, author affiliations, citation counts, or identifiers that were not present in the input. Keep source and capture date with each imported relationship so results can be checked later.

## Workflow

1. **Scope the map.** Record seed identifiers, citation source(s), date boundary, traversal direction and depth, maximum work count, and any incomplete inputs. Ask for missing scope that materially changes the result.
2. **Normalize records.** Preserve each source's original identifier and value. Deduplicate only when stable identifiers match; otherwise mark possible duplicates for review rather than merging on title alone.
3. **Trace references.** For each included work, follow the supplied reference links up to the agreed backward depth. Record each edge as `citing work -> cited work` and retain its source.
4. **Trace citing works.** If forward-citation metadata is supplied, follow it to the agreed depth. Record capture dates: citation indexes change, so counts and coverage are time-specific.
5. **Bound and report coverage.** Stop at the agreed depth or work limit. List unexpanded works, missing citation data, inaccessible records, and any source or date limits. Do not present a bounded map as exhaustive.
6. **Summarize cautiously.** Describe visible paths, repeated connections, and candidate influential works. If calculating degree or another graph measure, name the exact input graph and metric. Citation frequency is not a measure of study quality, truth, clinical relevance, or causation.
7. **Return an auditable result.** Include scope, sources and capture dates, included-work and edge counts, deduplication decisions, observed patterns, limitations, and unresolved checks. Keep the underlying identifiers and citation edges with the result.

## Suggested output fields

A work record can contain `source_id`, `doi`, `pmid`, `title`, `authors_as_listed`, `year`, `venue`, and `source_captured_at`. A citation edge can contain `citing_source_id`, `cited_source_id`, `source`, and `captured_at`. Leave unavailable fields empty; never invent example papers, identifiers, counts, or links.

## Validation checklist

- [ ] Seeds, scope, direction, depth, limits, and sources are explicit.
- [ ] Every reported work and edge can be traced to supplied metadata.
- [ ] Deduplication preserves identifiers and flags uncertain matches.
- [ ] Coverage limits and capture dates are reported.
- [ ] Descriptive citation patterns are not presented as quality or clinical evidence.
- [ ] No claim is made that this package ran code, searched a database, or retrieved paper content.

## Output requirements

For a non-trivial map, report:

1. Objective and seed works.
2. Inputs, sources, and capture dates.
3. Traversal method and scope limits.
4. Included works/edges and descriptive findings.
5. Assumptions, missing data, and other limitations.
6. Follow-up checks needed for claims that require reading or evaluating the underlying studies.

If citation metadata or authorization is missing, state what is missing and stop the dependent part of the map. Do not fabricate citations or results.
