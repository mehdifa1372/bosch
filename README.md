# Bosch Production-Line Failure Prediction

An end-to-end machine-learning case study for detecting defective products from anonymized manufacturing measurements. The project explores sparse, high-dimensional tabular data, feature engineering across numerical, categorical, and timestamp signals, class imbalance, and deployment through a small Flask application.

## Portfolio highlights

- Builds manufacturing-path and timing features from station-level measurements.
- Uses Matthews correlation coefficient (MCC), a useful metric for imbalanced binary classification.
- Compares gradient boosting, XGBoost, FTRL, and ensemble approaches.
- Includes a lightweight prediction service for demonstrating the trained pipeline.

> **Project status:** research prototype. The notebooks document the experiments; the Flask application still requires trained artifacts derived from the Kaggle data. It is not intended for production use without the validation and hardening described below.

## Repository guide

| File | Purpose |
|---|---|
| `EDA .ipynb` | Exploratory analysis and dataset inspection |
| `Feature_Engineering.ipynb` | Station, time, categorical, and numerical feature construction |
| `Hyperparameter tuning and Modelling.ipynb` | Model selection and tuning |
| `Final Xgb model with filtered Feature.ipynb` | Final XGBoost experiment |
| `Custom Ensemble Model.ipynb` | Ensemble experiment |
| `app2.py` | Flask demonstration service |
| `pkl_files/README.md` | Expected local model artifacts |

## Reproduce the environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The original competition dataset is not redistributed here. Download it from the Bosch Production Line Performance competition on Kaggle and keep it outside version control. Run the notebooks in the order shown above. Because this dataset is large, begin with a sampled development split before running the full pipeline.

## Run the demonstration app

1. Generate the trained artifacts listed in `pkl_files/README.md`.
2. Put those files in `pkl_files/`.
3. Set a Flask secret and start the service:

```bash
export FLASK_SECRET_KEY="replace-with-a-random-value"
python app2.py
```

Open `http://127.0.0.1:5000`. Upload exactly three `.csv` or `.txt` files representing categorical, date, and numerical features. Uploaded data is placed in a request-specific directory and removed after prediction.

## Evaluation checklist

Before publishing final model numbers, record:

- A leakage-safe train/validation split.
- The class distribution and a naive baseline.
- MCC, precision, recall, F1, ROC-AUC, and PR-AUC.
- Training/inference time and memory use.
- The exact feature set and random seed.
- Error analysis for false positives and false negatives.

Numbers are deliberately not claimed in this README until they can be reproduced from a clean environment.

## Engineering roadmap

- Move preprocessing from the Flask route into a tested Python package.
- Serialize one versioned `Pipeline` artifact instead of loading many independent pickle files.
- Add schema validation and structured API errors.
- Add unit tests for feature generation and a small integration fixture.
- Containerize the demo and add model/data provenance metadata.
- Replace row-wise pandas loops with vectorized operations where practical.

## Responsible use

This is an educational portfolio project based on anonymized competition data. Predictions must not be used for real manufacturing decisions without domain validation, monitoring, calibration, and human oversight.

## Author

Mehdi Faraz — machine learning, computer vision, data science, and applied AI.

