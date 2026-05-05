# Raw Data

## Data sources

### International student data

International student data are obtained from the Australian Government Department of Education international student pivot data.

Source website:  
https://www.education.gov.au/international-education-data-and-research/international-student-monthly-summary-and-data-tables

The relevant data provide year-to-date international student enrolments and commencements by month, year, state and education sector.

For this project, the pivot table is filtered to Victoria. Quarter-end months are used to construct quarterly observations:

- Q1 = March
- Q2 = June
- Q3 = September
- Q4 = December

### Melbourne rental vacancy data

Melbourne rental vacancy data are based on public SQM Research vacancy charts for Melbourne.

Source website:  
https://sqmresearch.com.au/

The SQM public charts provide visual information on rental vacancy counts and vacancy rates. The underlying downloadable data table is not included because it requires purchase. Therefore, the quarterly vacancy count and vacancy rate series used in this project are visually approximated from the public SQM charts.

## Why raw data are not fully included

The raw Department of Education pivot workbook and the SQM underlying data table are not fully included in this repository.

The Department of Education data are available from an external public source and may be updated over time. The SQM underlying data table requires purchase, so it cannot be included directly. Instead, the cleaned quarterly dataset records the manually extracted and approximated values used for the analysis.

## Manual processing steps

1. Obtain the Department of Education international student pivot workbook.
2. Filter the data to Victoria.
3. Extract year-to-date enrolments and commencements for the quarter-end months from 2020 to 2025.
4. Use the SQM public Melbourne vacancy charts to visually approximate quarterly vacancy counts and vacancy rates from 2020 to 2025.
5. Merge the quarterly student data and quarterly vacancy data into `data/clean/quarterly_student_vacancy_2020_2025.csv`.

## Cleaned variables produced

The cleaned quarterly dataset includes:

- `year`: Calendar year.
- `quarter`: Calendar quarter.
- `quarter_end_month`: Month used as the quarter-end reference point.
- `quarter_end_date`: Quarter-end date.
- `vic_ytd_enrolments`: Victoria year-to-date international student enrolments.
- `vic_ytd_commencements`: Victoria year-to-date international student commencements.
- `estimated_melbourne_vacancies`: Approximate number of Melbourne rental vacancies.
- `estimated_melbourne_vacancy_rate_pct`: Approximate Melbourne rental vacancy rate.
- `student_geography`: Geographic level of the student data.
- `vacancy_geography`: Geographic level of the vacancy data.
- `notes`: Notes on construction and limitations.

## Limitations

The international student data are measured at the Victoria level, while the vacancy data refer to Melbourne. This creates a geographic mismatch. The vacancy data are visually approximated from public SQM charts rather than downloaded from the underlying SQM data table. These limitations mean the data should be used for descriptive exploratory analysis rather than causal identification.