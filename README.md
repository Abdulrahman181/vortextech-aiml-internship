# VortexTech AI/ML Internship notebooks

This repository contains two introductory Titanic exercises:

- `week1.ipynb` — basic cleaning and exploratory plots.
- `week2.ipynb` — one decision-tree classifier and a train/test split with accuracy and F1 output.

## Data and setup

The Titanic training CSV is **not included**. Obtain a permitted copy of `train.csv` from the Titanic dataset/competition, then either:

1. Keep the existing Kaggle default at `/kaggle/input/competitions/titanic/train.csv`;
2. Place the file at `data/train.csv` (or at repository-root `train.csv`); or
3. Set `TITANIC_TRAIN_CSV` to the CSV's path before starting the notebook, for example:

   ```bash
   export TITANIC_TRAIN_CSV="$HOME/datasets/titanic/train.csv"
   ```

An explicitly set `TITANIC_TRAIN_CSV` is used on its own. If no candidate exists, the notebook raises a `FileNotFoundError` that lists the paths it checked. Run each notebook from top to bottom after selecting the data path.

For a local Python environment, Python 3.10–3.12 is recommended. Install the pinned notebook dependencies with:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Open the notebooks in Jupyter or another notebook frontend in that environment. The Jupyter frontend itself is not included in `requirements.txt`; Kaggle already provides one.

## Credentials and data handling

Do not commit `train.csv`, Kaggle API credentials, or other private data. Keep Kaggle credentials in your local Kaggle configuration, not in notebook cells or outputs. If a credential was ever committed or exposed, revoke/rotate it in Kaggle; deleting a working-tree copy does not invalidate an exposed key.

## Scope and limitations

These are small learning examples, not a production pipeline. `week2.ipynb` uses a single un-tuned decision tree and a fixed random split; its score is not a benchmark or a validated performance claim. Previously saved notebook outputs were cleared so results are regenerated from the user's data when the cells are run. No dataset is vendored, and model performance was not run or validated as part of this repository repair.
