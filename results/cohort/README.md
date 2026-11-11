# Stage 1 cohort audit

Audit date: 2026-09-20

The cohort builder reads the historical ADNI diagnosis and subject
characteristics archives directly from local ZIP files. No participant-level
data are stored in this public-results directory.

## Reproduced findings

- 13,102 raw diagnosis rows were inspected.
- 30 rows had missing examination dates.
- 1 row had a future examination date beyond the audit cutoff.
- 11 rows lacked a harmonizable current diagnosis.
- 13,071 valid diagnosis rows from 2,898 participants were retained.
- 1,081 participants had MCI at a baseline visit.
- Conversion to AD within 1,095 days reproduced exactly 255 converters.

## Unresolved legacy-count discrepancy

The candidate rule requiring non-AD follow-up from day 1,005 onward produced
702 participants: 255 converters and 447 stable participants. The manuscript
reports 695 participants: 255 converters and 440 stable participants.

The seven-person difference is restricted to the stable group. The code does
not remove seven participants arbitrarily. Stage 2 will test whether the legacy
count resulted from modality availability, QC, or an undocumented eligibility
rule. If it cannot be reproduced from a defensible rule, the manuscript will be
updated to the fully auditable cohort rather than preserving an unsupported
count.

## Files

- `cohort_audit.json`: configuration, input checksums, cleaning counts, and rule results.
- `cohort_flow.csv`: aggregate cohort flow.
- `rule_comparison.csv`: comparison of candidate stability definitions.
