# ECC3479 Project

## Research Question

How are changes in international student enrolments associated with rental vacancy rates in Melbourne?

This project examines whether international student demand is descriptively associated with Melbourne rental vacancy rates. The analysis is exploratory and descriptive, not causal.

## Group Members

Qi Ding

## Repository Structure

- `README.md`: project overview, repository structure, software information, and instructions for reproducing the workflow
- `code/`: Python scripts and notebooks used in the project
  - `clean_data.py`: original cleaning script for the initial sample dataset
  - `eda.ipynb`: exploratory data analysis using the updated quarterly dataset
- `data/raw/`: raw data documentation and instructions for obtaining source data
- `data/clean/`: cleaned dataset(s) and codebook
  - `clean_data.csv`: original cleaned sample dataset
  - `quarterly_student_vacancy_2020_2025.csv`: updated quarterly dataset used for the current EDA
  - `codebook.md`: variable documentation
- `docs/`: notes and supporting documentation
- `outputs/`: generated figures, tables, and other outputs

## Software Information

This project uses Python 3.

Required packages:

- pandas
- matplotlib
- statsmodels

Recommended install command:

```bash
pip install pandas matplotlib statsmodels
```

## Data Sources

### International student data

International student data are obtained from the Australian Government Department of Education international student monthly summary and pivot data.

Source:  
https://www.education.gov.au/international-education-data-and-research/international-student-monthly-summary-and-data-tables

The updated dataset uses Victoria year-to-date international student enrolments at quarterly reference points:

- Q1 = March
- Q2 = June
- Q3 = September
- Q4 = December

### Rental vacancy data

Melbourne rental vacancy data are based on public SQM Research vacancy charts.

Source:  
https://sqmresearch.com.au/

The underlying SQM data table requires purchase, so the Melbourne vacancy-rate values used in this project are visually approximated from the public chart. This is documented in `data/raw/README.md`.

## Manual Steps Required

Some steps must be completed manually before running the project:

1. Obtain the Department of Education international student pivot workbook.
2. Filter the student data to Victoria.
3. Extract quarterly reference values using March, June, September and December.
4. Use the SQM public Melbourne vacancy chart to approximate quarterly vacancy rates from 2020 to 2025.
5. Save the cleaned and merged dataset as:

```text
data/clean/quarterly_student_vacancy_2020_2025.csv
```

The cleaned quarterly dataset is already included in `data/clean/` for reproducibility.

## Clean Data

The main cleaned dataset for the updated EDA is:

```text
data/clean/quarterly_student_vacancy_2020_2025.csv
```

It contains quarterly observations from 2020 Q1 to 2025 Q4.

Key variables include:

- `year`
- `quarter`
- `quarter_end_date`
- `vic_ytd_enrolments`
- `estimated_melbourne_vacancy_rate_pct`

Variable definitions are provided in:

```text
data/clean/codebook.md
```

## How to Run the Project from Scratch

1. Make sure Python is installed.

2. Install the required packages:

```bash
pip install pandas matplotlib
```

3. If rebuilding the original sample dataset, run:

```bash
python code/clean_data.py
```

4. Open the EDA notebook:

```text
code/eda.ipynb
```

5. Run all cells in the notebook.

The notebook reads:

```text
data/clean/quarterly_student_vacancy_2020_2025.csv
```

and produces descriptive statistics, time-series plots, a scatter plot, and a correlation table.

## Script and Notebook Order

Run files in this order:

1. `code/clean_data.py`  
   Creates the original sample cleaned dataset.

2. `code/eda.ipynb`  
   Runs exploratory data analysis using the updated quarterly dataset.

3. `code/analysis.ipynb`  
   Runs the main descriptive regression analysis and saves the regression table to `outputs/tables/regression_table_quarterly.csv`.


## Current Project Status

The repository now includes:

- raw data documentation
- original cleaning script
- original cleaned sample dataset
- updated quarterly cleaned dataset
- data codebook
- exploratory data analysis notebook
- project notes and limitations

## EDA Findings

The updated quarterly EDA compares Victoria international student enrolments with estimated Melbourne vacancy rates from 2020 to 2025.

The time-series plots show that international student enrolments changed substantially during and after the COVID-affected period. The estimated Melbourne vacancy rate was high around 2020–2021 and then declined in later years.

However, the scatter plot and correlation table do not show a clear contemporaneous linear relationship between Victoria international student enrolments and Melbourne vacancy rates. The correlation is close to zero in the current quarterly sample.

These results should be interpreted cautiously because:

- the international student data are measured at the Victoria level
- the vacancy data refer to Melbourne
- the vacancy-rate values are approximated from SQM public charts
- the 2020–2025 period is strongly affected by COVID-era disruptions

Therefore, the current analysis is descriptive and exploratory rather than causal.