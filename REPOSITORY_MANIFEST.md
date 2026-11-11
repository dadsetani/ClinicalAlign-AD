# ClinicalAlign-AD repository manifest

All repository files are stored directly in this project. Citation metadata
are provided in `CITATION.cff`, and software licensing terms are in `LICENSE`.

## Manuscript

- `main.tex` --- current manuscript source
- `References.bib` --- bibliography database
- `tables/cohort_characteristics.tex`
- `tables/model_performance.tex`
- `tables/complete_case.tex`

## Reproduction scripts

- `scripts/01_build_cohort.py`
- `scripts/02_build_multimodal_dataset.py`
- `scripts/03_run_baselines.py`
- `scripts/04_make_manuscript_assets.py`
- `scripts/package_repository.py`

## Analysis package

- `src/clinicalalign_ad/__init__.py`
- `src/clinicalalign_ad/cohort.py`
- `src/clinicalalign_ad/modalities.py`
- `src/clinicalalign_ad/modeling.py`

## Configuration

- `.gitignore`
- `configs/cohort.json`
- `configs/modalities.json`
- `configs/modeling.json`
- `requirements-core.txt`
- `LICENSE`
- `CITATION.cff`

## Tests

- `tests/test_cohort.py`
- `tests/test_modalities.py`
- `tests/test_modeling.py`

## Aggregate, non-identifying results

- `results/cohort/`
- `results/modalities/`
- `results/modeling/`
- `results/manuscript/`

## Generated scientific figures

- `figures/reproducible_workflow.png`
- `figures/modality_coverage.png`
- `figures/heldout_auc_ablation.png`

## Files intentionally excluded

- `data/raw/` contains local access-controlled source data and is excluded from Git.
- `data/derived/` contains participant-level derived tables and predictions.
- `main.pdf` is a local build artifact and can be regenerated with
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex`.

The root `.gitignore` enforces these exclusions. Do not upload the excluded
participant-level data to a public repository.