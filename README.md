# ECC3479 Project

## Research Question
How do changes in international student numbers affect housing vacancy rates in Melbourne?

## Group Members
Qi Ding

## Expected Data Sources
Data on international student numbers from the Department of Education.
Housing vacancy rate data from ABS or property market reports.  
Housing vacancy rate data from property market reports.  

International student source:
https://www.education.gov.au/international-education-data-and-research/explanatory-notes-data-relating-international-students-studying-australia

## Repository Structure
- `README.md`: project overview and instructions for reproducing the workflow
- `code/`: Python scripts used in the project
- `data/raw/`: raw data documentation and source information
- `data/clean/`: cleaned dataset(s) and variable documentation
- `docs/`: notes and supporting documentation
- `outputs/`: tables, figures, or other generated outputs

## Software Information
This project uses Python 3.

Required package:
- pandas

Recommended install command:

```bash
pip install pandas
```

## Manual Steps Required
Some steps must be completed manually before running the project:

1. Obtain the raw data from external sources.
2. Review the source documentation for the datasets.
3. Save the raw data in the `data/raw/` folder if available.

## Raw Data
The raw data used in this project is not included in the repository.

International student data can be obtained from the Australian Department of Education:
https://www.education.gov.au/

Housing vacancy rate data can be obtained from ABS or property market reports.

The data is not included because it comes from external sources and may be updated over time. See `data/raw/README.md` for more details.

## Clean Data
- The current cleaned dataset is a small sample dataset used to demonstrate the workflow and repository structure at this stage of the project.
The cleaned dataset is stored in:

- `data/clean/clean_data.csv`

Documentation for cleaned variables is stored in:

- `data/clean/codebook.md`

## How to Run the Project from Scratch
1. Make sure Python is installed.
2. Install the required package:

```bash
pip install pandas
```

3. Run the cleaning script:

```bash
python code/clean_data.py
```

4. Check the cleaned output in `data/clean/`.

## Script Order
The scripts should be run in the following order:

1. `code/clean_data.py`

This script creates the cleaned dataset used for later analysis.

## Current Project Status
At this stage, the repository includes:
- raw data documentation
- a cleaning script
- a cleaned output dataset

## Initial EDA Findings
- Basic exploratory analysis is provided in `code/eda.ipynb`, with figures saved to `outputs/`.
- The current cleaned dataset is a small sample dataset used to demonstrate workflow.
- In this sample, lower international student numbers are associated with higher vacancy rates.
- These results are illustrative only because the dataset is very small.