"""
This script creates an analysis-ready dataset for the project.

It first attempts to read raw data from the data/raw/ folder. If the raw data
file is not available, it generates a small sample dataset to demonstrate the
workflow. The script then applies basic cleaning steps and saves the cleaned
dataset to data/clean/clean_data.csv.
"""

import pandas as pd

# Step 1: Define file paths
raw_path = "data/raw/raw_data.csv"
clean_path = "data/clean/clean_data.csv"

# Step 2: Try to load raw data
try:
    df = pd.read_csv(raw_path)
    print("Raw data loaded successfully.")
except FileNotFoundError:
    print("Raw data file not found. Creating a sample dataset instead.")

    # Create a sample dataset
    df = pd.DataFrame({
        "suburb": ["Clayton", "Clayton", "CBD", "CBD"],
        "year": [2020, 2021, 2020, 2021],
        "international_students": [12000, 8000, 25000, 15000],
        "vacancy_rate": [2.5, 4.0, 1.8, 3.5]
    })

# Step 3: Basic cleaning
df_clean = df.dropna()

# Step 4: Save cleaned data
df_clean.to_csv(clean_path, index=False)

print("Cleaned data saved to data/clean/clean_data.csv")