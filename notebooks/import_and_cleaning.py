import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "data", "diabetic_data.csv")

print("Script file:", __file__)
print("Resolved CSV path:", file_path)

df = pd.read_csv(file_path)

df = df.replace("?", pd.NA)

df["is_readmitted_30"] = df["readmitted"].apply(lambda x: 1 if x == "<30" else 0)

cols_to_drop = ["weight", "payer_code", "medical_specialty"]
df = df.drop(columns=cols_to_drop, errors="ignore")

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

clean_df = df[analysis_cols].copy()

print("\nCleaned dataset preview:")
print(clean_df.head())

print("\nCleaned dataset shape:")
print(clean_df.shape)