from pathlib import Path
import pandas as pd

# Build reliable file paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

input_file = DATA_DIR / "cleaned_readmission_data.csv"

df = pd.read_csv(input_file)


# Load cleaned dataset
df = pd.read_csv(input_file)
print("Original dataset shape:", df.shape)
print(df.head())

# Keep only columns needed for analysis
analysis_cols = [
    "encounter_id",
    "patient_nbr",
    "race",
    "gender",
    "age",
    "admission_type_id",
    "discharge_disposition_id",
    "time_in_hospital",
    "num_lab_procedures",
    "num_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "diag_1",
    "A1Cresult",
    "insulin",
    "diabetesMed",
    "readmitted",
    "is_readmitted_30"
]

# Check that all needed columns exist
missing_cols = [col for col in analysis_cols if col not in df.columns]
if missing_cols:
    print("Missing columns:", missing_cols)
else:
    print("All analysis columns are present.")

analysis_df = df[analysis_cols].copy()
print("\nAnalysis dataset shape:", analysis_df.shape)
print(analysis_df.head())

# Overall 30-day readmission rate
overall_rate = analysis_df["is_readmitted_30"].mean()
print(f"\nOverall 30-day readmission rate: {overall_rate:.2%}")

# Readmission counts
print("\nReadmission counts:")
print(analysis_df["is_readmitted_30"].value_counts())

# Average length of stay by readmission
print("\nAverage length of stay by readmission:")
print(analysis_df.groupby("is_readmitted_30")["time_in_hospital"].mean())

# Average number of medications by readmission
print("\nAverage number of medications by readmission:")
print(analysis_df.groupby("is_readmitted_30")["num_medications"].mean())

# Average number of emergency visits by readmission
print("\nAverage number of emergency visits by readmission:")
print(analysis_df.groupby("is_readmitted_30")["number_emergency"].mean())

# Readmission rate by gender
print("\nReadmission rate by gender:")
print(analysis_df.groupby("gender")["is_readmitted_30"].mean())

# Readmission rate by age group
print("\nReadmission rate by age group:")
print(analysis_df.groupby("age")["is_readmitted_30"].mean().sort_index())

# Create midpoint values for age ranges
age_map = {
    "[0-10)": 5,
    "[10-20)": 15,
    "[20-30)": 25,
    "[30-40)": 35,
    "[40-50)": 45,
    "[50-60)": 55,
    "[60-70)": 65,
    "[70-80)": 75,
    "[80-90)": 85,
    "[90-100)": 95,
    "[100-110)": 105
}

analysis_df["age_mid"] = analysis_df["age"].map(age_map)

print("\nAge midpoint preview:")
print(analysis_df[["age", "age_mid"]].head())

    # Readmission rate by age midpoint
print("\nReadmission rate by age midpoint:")
print(analysis_df.groupby("age_mid")["is_readmitted_30"].mean())
