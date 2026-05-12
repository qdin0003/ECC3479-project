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

## Raw integrated dataset

The final raw input used by the project pipeline is:

```text
data/raw/quarterly_student_vacancy_2020_2025.csv