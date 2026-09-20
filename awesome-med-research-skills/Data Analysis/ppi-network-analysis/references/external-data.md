# Prepare the external STRING dataset

Full analysis needs the six STRING v11.5 gzip files listed in
[string-v11.5.sha256](string-v11.5.sha256), covering human (`9606`) and mouse
(`10090`) aliases, info and links. They total 196,355,105 bytes (about 196 MB).
Keep the compressed files intact and the complete set together.

## Prepare once

Obtain the complete dataset from a checkout of the canonical source repository,
[AIpoch medical-research-skills](https://github.com/aipoch/medical-research-skills),
at a revision containing `datasets/ppi-network-analysis/string-v11.5`.
Skill Release ZIPs and the flattened
[awesome-medical-research-skills mirror](https://github.com/aipoch/awesome-medical-research-skills)
contain only the Skill, not this dataset directory. Users of either distribution
need the canonical checkout or separately provided exact data files. Existing
installations with bundled tables can copy all six files to the external directory
and verify them against the same checksum list before updating the Skill.
If the dataset is unavailable, ask the dataset provider
for the exact six files and applicable notices before proceeding. There is no
automatic download or published CDN endpoint in this workflow.

In a POSIX shell, replace the three absolute paths below. Choose a new directory
outside the installed Skill; the plain `mkdir` intentionally stops if it already
exists, avoiding replacement of an existing dataset.

```bash
PPI_SKILL_ROOT="/absolute/path/to/installed/ppi-network-analysis"
PPI_DATA_SOURCE="/absolute/path/to/source/datasets/ppi-network-analysis/string-v11.5"
export PPI_STRING_CACHE="/absolute/path/to/user-data/ppi-string-v11.5"

(
  set -eu
  mkdir "$PPI_STRING_CACHE"
  for species in 9606 10090; do
    for table in aliases info links; do
      cp "$PPI_DATA_SOURCE/$species.protein.$table.v11.5.txt.gz" "$PPI_STRING_CACHE/"
    done
  done
  cd "$PPI_STRING_CACHE"
  shasum -a 256 -c "$PPI_SKILL_ROOT/references/string-v11.5.sha256"
)
```

The parent of the chosen directory must already exist. Proceed only when all
six checks report `OK` and the command exits successfully. For an existing
directory, run only the checksum command from inside it before reuse. On Windows,
compare each file with `Get-FileHash -Algorithm SHA256` against the same checksum
list, then pass the absolute directory to the R CLI.

A missing file, mismatched digest or partial copy is an incomplete preparation.
Restore the exact affected files from the provider, then verify the entire set
again. SHA-256 establishes byte identity; it does not grant redistribution rights.
Keep the dataset provider's applicable terms and notices with your data.

## Run analysis

From the installed Skill directory, use the existing options:

```bash
Rscript scripts/main.R \
  --genelist_file tests/data/gene_list.csv \
  --species human \
  --threshold 700 \
  --string_cache_dir "$PPI_STRING_CACHE" \
  --string_version v11.5 \
  --output_dir tests/output/basic-run
```

In a new shell, set `PPI_STRING_CACHE` again, or pass the absolute directory
literally. This variable is a shell convenience; the R program consumes the
`--string_cache_dir` argument. Explicit `v11.5` ensures all three selected-species
tables use the same version. Missing directories or tables produce the existing
`SKILL_FILE_NOT_FOUND` error. No network fallback runs.

Plot-only regeneration uses an existing `output_dir/data/ppi_result.rds` and does
not read STRING tables; use the plot-only command in the main Skill guide.

## Ownership and cleanup

The external directory belongs to the user and may be shared by multiple runs.
Back it up with its checksum list and provider notices. Skill updates and removal
do not move, replace or delete this directory. Remove it manually only when no
remaining workflow needs it; later full analyses need it provisioned again.
Analysis outputs continue to use the existing output directory inside the Skill.
