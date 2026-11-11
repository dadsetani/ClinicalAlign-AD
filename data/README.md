# Data inputs

Participant-level ADNI data must remain local and must not be committed.

Place locally supplied, access-controlled ADNI source files in `data/raw/`.
Stage 1 expects these archives there:

- `Diagnosis.zip`
  - `DXSUM_PDXCONV_ADNIALL.csv`
- `Subject_Characteristics.zip`
  - `PTDEMOG.csv`
  - `FHQ.csv`
  - `RECFHQ.csv`
  - `FAMXHPAR.csv`
  - `FAMXHSIB.csv`

Later stages additionally use the NfL, DTI, FreeSurfer, vital-sign, medical
history, and neurological examination files listed below. Files in `data/raw/`
and participant-level derived outputs in `data/derived/` must remain local and
must not be committed or redistributed. Public repository outputs are
restricted to aggregate statistics, schemas, configuration files, and
checksums that do not expose participant identifiers.

Stage 2 expects the following additional local files:

- `NFL.zip`
- `VITALS_18Sep2026.csv`
- `NEUROEXM_18Sep2026.csv`
- `MEDHIST_18Sep2026.csv`
- `INITHEALTH_18Sep2026.csv`
- `ADNI_DTIROI_V1_18Sep2026.csv`
- `DTIROI_ROBUSTMEAN_18Sep2026.csv`
- `DTIROI_MEAN_18Sep2026.csv`
- `UCSFFSX7_18Sep2026.csv`
