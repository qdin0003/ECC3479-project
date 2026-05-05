# Data Codebook

## Dataset 1: `clean_data.csv`

This was the original cleaned dataset used for the initial exploratory analysis.

### Variables

- `suburb` (string): Location in Melbourne, such as Clayton or CBD.
- `year` (integer): Year of observation.
- `international_students` (integer): Number of international students in the relevant period.
- `vacancy_rate` (float, %): Residential vacancy rate.

---

## Dataset 2: `quarterly_student_vacancy_2020_2025.csv`

This dataset contains quarterly observations from 2020 Q1 to 2025 Q4. It combines Victoria-level international student data with estimated Melbourne rental vacancy data.

### Variables

| Variable | Description |
|---|---|
| `year` | Calendar year of the observation. |
| `quarter` | Calendar quarter, from Q1 to Q4. |
| `quarter_end_month` | Month used as the quarter-end reference point. Q1 = March, Q2 = June, Q3 = September, Q4 = December. |
| `quarter_end_date` | Quarter-end date used for time-series plotting. |
| `vic_ytd_enrolments` | Year-to-date international student enrolments in Victoria. Source: Australian Government Department of Education pivot data. |
| `vic_ytd_commencements` | Year-to-date international student commencements in Victoria. Source: Australian Government Department of Education pivot data. |
| `estimated_melbourne_vacancies` | Approximate number of rental vacancies in Melbourne, visually estimated from the public SQM Research vacancy chart. |
| `estimated_melbourne_vacancy_rate_pct` | Approximate Melbourne rental vacancy rate, visually estimated from the public SQM Research vacancy-rate chart. |
| `student_geography` | Geographic level of the international student data. |
| `vacancy_geography` | Geographic level of the vacancy data. |
| `notes` | Notes on data construction and limitations. |

### Important notes

The international student variables are measured at the Victoria level, while the vacancy variables refer to Melbourne. The vacancy series is an approximation digitised from public SQM Research charts because the underlying data table requires purchase. These limitations mean the dataset is suitable for descriptive analysis, not causal identification.