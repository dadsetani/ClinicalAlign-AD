# ClinicalAlign-AD

Reproducible analysis and manuscript source for predicting 36-month
MCI-to-Alzheimer's disease conversion from ADNI-derived clinical, biomarker,
and imaging data.

For a complete clickable-style path index of files intended for the public
repository, see `REPOSITORY_MANIFEST.md`. The repository is stored as ordinary
files and directories; no ZIP archive is required.

## Data governance

ADNI participant-level data are access-controlled and are not included in this
repository. Place locally supplied source archives and tables in `data/raw/`;
the analysis reads them from there by default. Raw and participant-level
derived files are excluded from Git and must not be redistributed.

## Reproducibility environment

The analysis and tests were run with Python 3.13.15 and the exact package
versions pinned in `requirements-core.txt`. Install those dependencies with:

    python -m pip install -r requirements-core.txt

## Reproduction stages

1. Build and audit the 36-month conversion cohort.
2. Merge clinical, plasma NfL, DTI, and FreeSurfer features with explicit QC.
3. Run baselines, ablations, and uncertainty analyses.
4. Regenerate manuscript tables and figures.
5. Compile and validate the manuscript.

## Stage 1: cohort audit

From the repository root, run:

    python scripts/01_build_cohort.py

The command reads `Diagnosis.zip` and `Subject_Characteristics.zip`, writes the
participant-level candidate cohort to the Git-ignored `data/derived/` directory,
and writes non-identifying audit summaries to `results/cohort/`.

Run the unit test suite with:

    python -m unittest discover -s tests -v

## Stage 2: baseline multimodal dataset

After Stage 1 has created the candidate cohort, run:

    python scripts/02_build_multimodal_dataset.py

This command selects temporally eligible baseline clinical, plasma NfL, DTI,
and FreeSurfer records; applies modality-specific QC; writes the private
participant-level table to `data/derived/multimodal_cohort.csv`; and writes only
aggregate coverage, missingness, overlap, and QC summaries to
`results/modalities/`. Temporal windows and feature mappings are declared in
`configs/modalities.json`.

## Stage 3: baselines, ablations, and uncertainty

Run:

    python scripts/03_run_baselines.py

The script creates a fixed participant-disjoint stratified holdout, performs
training-only cross-validation and preprocessing, evaluates predefined feature
ablations, and calculates bootstrap confidence intervals. Participant-level
split assignments and predictions remain under `data/derived/`; aggregate
results are written to `results/modeling/`. Model and feature-set definitions
are declared in `configs/modeling.json`.

## Stage 4: manuscript assets

Run:

    python scripts/04_make_manuscript_assets.py

The command regenerates aggregate manuscript tables in `tables/`, scientific
figures in `figures/`, and non-identifying table source data in
`results/manuscript/`. The current manuscript reports only analyses reproduced
by the repository pipeline. Earlier neural contrastive and synthetic results
that could not be regenerated in the available environment are not retained as
primary manuscript evidence.

## Compile the manuscript

With a TeX distribution that includes `elsarticle` and `latexmk`, compile the
current manuscript and bibliography from the repository root with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex

The generated PDF and LaTeX auxiliary files are build artifacts and should not
be committed.

## Current cohort definitions

The legacy manuscript reported 695 participants: 255 converters and 440 stable
participants. The executable candidate rule yields 702 participants: 255
converters and 447 stable participants. The analysis does not force agreement
with the legacy total; it reports the seven-participant discrepancy and uses
the transparent candidate cohort throughout the reproducible results.

## Citation and license

Citation metadata are provided in `CITATION.cff`. The MIT License applies to
the analysis source code and tests only. ADNI data remain subject to the ADNI
Data Use Agreement; the license does not grant rights to redistribute those
data or third-party materials.

## Package the public repository

Create a Base64-encoded ZIP as the Prism-safe text file `Base64.txt`:

    python scripts/package_repository.py

The text file is created in the repository root and is not included in the
archive. To restore the ZIP outside the repository, run from the repository
root:

    python -c "import base64, pathlib; pathlib.Path('../ClinicalAlign-AD.zip').write_bytes(base64.b64decode(pathlib.Path('Base64.txt').read_text(encoding='ascii').strip()))"

The archive contains only the explicitly selected public files; participant-
level data and build artifacts are excluded.
