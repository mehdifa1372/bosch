# Local model artifacts

The Flask demo expects trained preprocessing and model artifacts in this directory. They are not committed because they are generated from the competition data and may be large or unsafe to accept from untrusted sources.

Expected filenames used by the current prototype:

- `OrdinalEncoder.pkl`
- `model_ftrl.pkl`
- `cat_data_imp_cols.pkl`
- `min_val_each_col_in_cat_data.pkl`
- `imp_numerical_features_name.pkl`
- `imp_date_cols_name.pkl`
- `imp_date_single_cols_name.pkl`
- `col_24_25.pkl`
- `categorical_columns`
- `numerical_columns`
- `date_columns`
- `final_model.pkl`

Only load artifacts you generated yourself or obtained from a trusted source. Python pickle/joblib files can execute code when loaded.

