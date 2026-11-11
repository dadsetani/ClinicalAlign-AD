# Stage 3: leakage-safe baseline modeling

Run this stage after building `data/derived/multimodal_cohort.csv`:

    python scripts/03_run_baselines.py

The script creates a fixed participant-disjoint 80/20 stratified split. Median
imputation, scaling, hyperparameter tuning, and the classification threshold
are fitted only within training data. Logistic regression, Gaussian naive Bayes, and k-nearest-neighbor models
are implemented with NumPy/SciPy because optional packages for scikit-learn,
PyTorch, XGBoost, and CatBoost are not available in the current environment.

The primary analysis retains all 702 candidate-cohort participants using
training-derived imputation and missingness indicators. Complete-case analyses
are reported separately and may have small test samples. Confidence intervals
are percentile intervals from 1,000 class-stratified bootstrap samples of the
fixed test predictions.

Complete-case populations with fewer than five participants from either class
in the test subset are excluded from model estimation and retained in
`analysis_population_feasibility.csv` as infeasible sensitivity analyses.

These results audit the transparent 702-participant candidate cohort. They do
not automatically replace the legacy manuscript results based on 695
participants.