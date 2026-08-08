# Hospital 30-Day Readmission Analysis

## Overview

This project analyzes hospital encounter data for patients diagnosed with diabetes to identify patterns associated with **30-day hospital readmission**.

Using **Python and pandas**, I cleaned and transformed the original healthcare dataset, performed exploratory data analysis, and created an analysis-ready dataset. I then used **Tableau** to build an interactive dashboard examining how 30-day readmission rates vary across demographic characteristics, hospital utilization, and other encounter-level factors.

The goal of this project is not to predict whether an individual patient will be readmitted, but to identify descriptive patterns that may help inform further investigation into hospital readmission risk.

---

## Objective

The primary objective of this analysis was to answer the following question:

**What characteristics of hospital encounters are associated with higher rates of readmission within 30 days of discharge?**

The analysis focused on several areas, including:

* Overall 30-day readmission rate
* Age
* Gender
* Race
* Length of hospital stay
* Number of medications
* Previous emergency department utilization
* Previous inpatient utilization

---

## Dataset

The project uses the **Diabetes 130-US Hospitals for Years 1999–2008** dataset from the UCI Machine Learning Repository.

The dataset contains:

* **101,766 hospital encounters**
* Data collected from **130 U.S. hospitals and integrated delivery networks**
* Clinical records spanning **1999–2008**
* Demographic, utilization, laboratory, diagnosis, medication, and readmission information

Each row represents a **hospital encounter**, not necessarily a unique patient. The dataset contains separate `encounter_id` and `patient_nbr` identifiers, meaning an individual patient may appear in more than one encounter.

The primary outcome used in this project is whether an encounter resulted in a hospital readmission **within 30 days of discharge**.

---

## Tools

### Python

Used for data import, cleaning, transformation, feature engineering, and exploratory analysis.

Key libraries:

* `pandas`

### Jupyter Notebook

Used to document and perform the exploratory data-analysis workflow.

### Tableau

Used to create the final interactive healthcare analytics dashboard.

### Git / GitHub

Used for version control, project organization, and portfolio presentation.

---

## Data Cleaning and Preparation

The original dataset required several preprocessing steps before analysis.

### 1. Missing-value identification

The dataset uses `"?"` to represent missing information in several variables. These values were converted to Python missing values using `pd.NA`.

Several variables contained substantial missingness, including:

* Weight
* Maximum glucose serum test
* A1C result
* Medical specialty
* Payer code
* Race

### 2. Removal of selected high-missingness variables

The following columns were removed from the working dataset:

* `weight`
* `payer_code`
* `medical_specialty`

These variables contained substantial missing data and were not necessary for the primary questions addressed in this analysis.

### 3. Creation of a 30-day readmission indicator

The original `readmitted` variable contains three categories:

* `<30` — readmitted within 30 days
* `>30` — readmitted after 30 days
* `NO` — no recorded readmission

A new binary variable, `is_readmitted_30`, was created:

```python
df["is_readmitted_30"] = df["readmitted"].apply(
    lambda x: 1 if x == "<30" else 0
)
```

This allows the mean of the binary variable to be interpreted as the **30-day readmission rate**.

### 4. Feature selection

A smaller analysis dataset was created containing variables relevant to the project's objectives, including:

* Encounter and patient identifiers
* Race
* Gender
* Age
* Admission and discharge information
* Length of hospital stay
* Laboratory procedures
* Number of procedures
* Number of medications
* Previous outpatient visits
* Previous emergency visits
* Previous inpatient visits
* Primary diagnosis
* A1C results
* Insulin use
* Diabetes medication use
* Readmission status

### 5. Age transformation

The original dataset represents age using 10-year age intervals such as:

`[20-30)`, `[30-40)`, and `[40-50)`.

For selected analyses, these categories were mapped to numerical midpoint values such as 25, 35, and 45 to simplify visualization and comparison.

### 6. Tableau export

The cleaned and selected dataset was exported as:

```text
cleaned_readmission_data.csv
```

This dataset was then used as the data source for the Tableau dashboard.

---

## Key Metrics

### Total Hospital Encounters

**101,766**

### 30-Day Readmitted Encounters

**11,357**

### Encounters Without 30-Day Readmission

**90,409**

### Overall 30-Day Readmission Rate

**11.16%**

The readmission rate represents the percentage of hospital encounters followed by another recorded admission within 30 days.

---

## Key Findings

### 1. Approximately 11% of encounters resulted in a 30-day readmission

Of the 101,766 encounters analyzed, **11,357 were followed by a readmission within 30 days**, producing an overall readmission rate of approximately **11.16%**.

### 2. Readmitted encounters were associated with slightly longer hospital stays

Average length of stay:

| 30-Day Readmission | Average Length of Stay |
| ------------------ | ---------------------: |
| No                 |              4.35 days |
| Yes                |              4.77 days |

Encounters followed by a 30-day readmission therefore had a somewhat longer average initial hospital stay.

This is an association and should not be interpreted as evidence that longer hospital stays cause readmission.

### 3. Readmitted encounters involved slightly more medications

Average number of medications:

| 30-Day Readmission | Average Medications |
| ------------------ | ------------------: |
| No                 |               15.91 |
| Yes                |               16.90 |

Encounters followed by early readmission involved approximately one additional medication on average.

This may reflect greater clinical complexity among patients who were subsequently readmitted.

### 4. Previous emergency-department utilization showed a notable difference

Average number of previous emergency visits:

| 30-Day Readmission | Average Previous Emergency Visits |
| ------------------ | --------------------------------: |
| No                 |                             0.178 |
| Yes                |                             0.357 |

Encounters followed by a 30-day readmission had approximately **twice the average prior emergency-department utilization** of encounters without an early readmission.

This suggests that previous healthcare utilization may be an important characteristic to examine when studying readmission risk.

### 5. Gender showed very little difference in readmission rate

Observed 30-day readmission rates were approximately:

| Gender | 30-Day Readmission Rate |
| ------ | ----------------------: |
| Female |                  11.25% |
| Male   |                  11.06% |

The difference between male and female encounters was small, suggesting that gender alone was not strongly associated with 30-day readmission in this descriptive analysis.

### 6. Readmission rates varied across age groups

Readmission rates differed across the dataset's 10-year age categories.

For example:

* Ages **20–29:** approximately **14.24%**
* Ages **50–59:** approximately **9.67%**
* Ages **80–89:** approximately **12.08%**

The relationship was not strictly linear, demonstrating why age-specific analysis can provide more information than examining the overall population alone.

These differences should be interpreted descriptively because age groups may contain different numbers of encounters and may differ on many other clinical characteristics.

---

## Tableau Dashboard

The Tableau dashboard was created to make the analysis easier to interpret visually.

The dashboard includes visualizations examining:

* Overall 30-day readmission
* Readmission rate by age
* Readmission rate by gender
* Readmission rate by race
* Readmission count by race
* Readmission rate by length of hospital stay
* Readmission rate by previous inpatient utilization

**Tableau Public Dashboard:**
`[ADD TABLEAU PUBLIC LINK HERE]`

### Dashboard Preview

`[ADD DASHBOARD SCREENSHOT HERE]`

---

## Repository Structure

```text
Hospital-Readmission-Risk-Dashboard/
│
├── data/
│   ├── diabetic_data.csv
│   └── cleaned_readmission_data.csv
│
├── notebooks/
│   ├── analysis.py
│   ├── import_and_cleaning.py
│   └── readmission_analysis.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── tableau/
│
├── 30 Day Diabetic Readmission Data Analysis Insights.twb
│
├── README.md
├── hospital.db
└── table.sql
```

The repository contains the original data, cleaned analysis dataset, Python analysis workflow, Jupyter Notebook, and Tableau workbook used to develop the final dashboard.

---

## Reproducing the Analysis

### 1. Clone the repository

```bash
git clone [REPOSITORY URL]
```

### 2. Navigate to the project directory

```bash
cd Hospital-Readmission-Risk-Dashboard
```

### 3. Install Python dependencies

The primary Python dependency is pandas:

```bash
pip install pandas
```

### 4. Open the analysis notebook

Launch Jupyter Notebook or JupyterLab and open:

```text
notebooks/readmission_analysis.ipynb
```

Run the notebook cells sequentially to:

1. Import the original dataset
2. Inspect data quality
3. Convert missing-value indicators
4. Create the 30-day readmission variable
5. Select analytical variables
6. Perform exploratory analysis
7. Export the cleaned dataset

The resulting analysis-ready dataset is:

```text
data/cleaned_readmission_data.csv
```

### 5. Open the Tableau workbook

The cleaned dataset can then be connected to the included Tableau workbook to reproduce the dashboard visualizations.

---

## Limitations

Several limitations should be considered when interpreting this analysis.

### Encounter-level analysis

The dataset contains **hospital encounters rather than one unique record per patient**. Because a patient may have multiple encounters, results should not be interpreted as percentages of unique patients unless the data are explicitly deduplicated using `patient_nbr`.

### Historical data

The dataset represents healthcare encounters from **1999 through 2008**. Clinical practices, diabetes treatment, hospital operations, and readmission-management strategies have changed since this period.

Therefore, the results should not automatically be assumed to represent current hospital populations.

### Missing data

Several variables contain substantial missing information. Variables with particularly high missingness were either excluded from the analysis or should be interpreted cautiously.

Missing demographic information was not imputed because an accurate value could not be reasonably inferred.

### Descriptive analysis

This project identifies **associations and patterns**, not causal relationships.

For example, a higher readmission rate among encounters involving longer hospital stays does not demonstrate that longer hospitalization causes readmission.

### No adjustment for confounding variables

The comparisons presented in the dashboard are primarily univariate descriptive comparisons. Factors such as age, disease severity, diagnoses, medication burden, utilization history, and length of stay may interact with one another.

A multivariable statistical or predictive model would be required to estimate the independent contribution of individual factors.

### Race analysis

The dashboard currently focuses on the primary displayed race categories. Records categorized as `Other` or containing missing race information are not represented in all race-specific visualizations and should therefore be considered when interpreting those comparisons.

### No predictive model

Despite the repository's focus on readmission risk, this version of the project does not attempt to predict individual patient outcomes.

The project is an **exploratory healthcare data analysis and visualization project**, rather than a clinical risk-prediction system.

---

## Potential Future Improvements

Future versions of this project could include:

* SQL-based validation and aggregation queries
* Multivariable statistical analysis
* Logistic regression for readmission probability
* Analysis of primary diagnosis categories
* Medication-specific analysis
* Additional analysis of previous inpatient and outpatient utilization
* Improved treatment of missing values
* A formal train/test modeling pipeline
* Interactive Tableau filters
* Comparison of encounter-level and unique-patient-level results

---

## Data Source and Citation

**Dataset:** *Diabetes 130-US Hospitals for Years 1999–2008*

UCI Machine Learning Repository

Clore, J., Cios, K., DeShazo, J., & Strack, B. (2014). *Diabetes 130-US Hospitals for Years 1999–2008* [Dataset]. UCI Machine Learning Repository.

**DOI:** `10.24432/C5230J`

The dataset is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

Associated research:

Strack, B., DeShazo, J. P., Gennings, C., Olmo, J. L., Ventura, S., Cios, K. J., & Clore, J. N. (2014). *Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records*. BioMed Research International.

---

## Author

**Jacob Melendrez**

Healthcare Data Analytics Portfolio Project
