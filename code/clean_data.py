"""
Create the analysis-ready dataset for the ECC3479 project.

This script reads the integrated quarterly student-vacancy dataset from
data/raw/, applies basic validation and cleaning steps, and saves the final
analysis-ready dataset to data/clean/clean_data.csv.

Pipeline:
data/raw/quarterly_student_vacancy_2020_2025.csv
    -> code/clean_data.py
    -> data/clean/clean_data.csv
"""

from pathlib import Path
import pandas as pd


# ---------------------------------------------------------------------
# 1. Define project paths
# ---------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_PATH = ROOT / "data" / "raw" / "quarterly_student_vacancy_2020_2025.csv"
CLEAN_DATA_PATH = ROOT / "data" / "clean" / "clean_data.csv"

CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------
# 2. Load raw integrated quarterly data
# ---------------------------------------------------------------------

print(f"Looking for raw data at: {RAW_DATA_PATH}")

if not RAW_DATA_PATH.exists():
    raise FileNotFoundError(
        f"Raw data file not found: {RAW_DATA_PATH}\n"
        "Please place the integrated quarterly dataset in data/raw/ "
        "with the filename quarterly_student_vacancy_2020_2025.csv."
    )

df = pd.read_csv(RAW_DATA_PATH)

print("Raw data loaded successfully.")
print(f"Raw data shape: {df.shape}")


# ---------------------------------------------------------------------
# 3. Standardise column names
# ---------------------------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)


# ---------------------------------------------------------------------
# 4. Validate required columns
# ---------------------------------------------------------------------

expected_columns = [
    "year",
    "quarter",
    "quarter_end_month",
    "quarter_end_date",
    "vic_ytd_enrolments",
    "vic_ytd_commencements",
    "estimated_melbourne_vacancies",
    "estimated_melbourne_vacancy_rate_pct",
    "student_geography",
    "vacancy_geography",
    "notes"
]

missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    raise ValueError(
        f"Missing expected columns: {missing_columns}\n"
        f"Available columns: {df.columns.tolist()}"
    )


# ---------------------------------------------------------------------
# 5. Convert variable types
# ---------------------------------------------------------------------

df["quarter_end_date"] = pd.to_datetime(df["quarter_end_date"], errors="raise")

# Keep quarter as a categorical label such as Q1, Q2, Q3, Q4.
df["quarter"] = df["quarter"].astype(str).str.strip().str.upper()

# Create a numeric quarter variable for sorting and validation.
df["quarter_num"] = (
    df["quarter"]
    .str.replace("Q", "", regex=False)
    .astype(int)
)

# Keep quarter_end_month as a readable month label such as Mar, Jun, Sep, Dec.
df["quarter_end_month"] = df["quarter_end_month"].astype(str).str.strip().str.title()

# Create numeric month variable for validation and chronological checks.
month_map = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

df["quarter_end_month_num"] = df["quarter_end_month"].map(month_map)

if df["quarter_end_month_num"].isna().any():
    bad_months = df.loc[df["quarter_end_month_num"].isna(), "quarter_end_month"].unique()
    raise ValueError(f"Unrecognised quarter_end_month values: {bad_months}")

numeric_columns = [
    "year",
    "quarter_num",
    "quarter_end_month_num",
    "vic_ytd_enrolments",
    "vic_ytd_commencements",
    "estimated_melbourne_vacancies",
    "estimated_melbourne_vacancy_rate_pct"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="raise")


# ---------------------------------------------------------------------
# 6. Sort and validate observations
# ---------------------------------------------------------------------

df = df.sort_values(["year", "quarter_num"]).reset_index(drop=True)

if df.empty:
    raise ValueError("The cleaned dataset is empty.")

if df.duplicated(subset=["year", "quarter"]).any():
    duplicated_rows = df[df.duplicated(subset=["year", "quarter"], keep=False)]
    raise ValueError(
        "Duplicate year-quarter observations found:\n"
        f"{duplicated_rows}"
    )

if df[numeric_columns].isna().any().any():
    missing_summary = df[numeric_columns].isna().sum()
    raise ValueError(
        "Missing values found in numeric columns:\n"
        f"{missing_summary}"
    )


# ---------------------------------------------------------------------
# 7. Save cleaned analysis-ready dataset
# ---------------------------------------------------------------------

df.to_csv(CLEAN_DATA_PATH, index=False)

print(f"Clean data saved to: {CLEAN_DATA_PATH}")
print(f"Clean data shape: {df.shape}")
print(df.head())
