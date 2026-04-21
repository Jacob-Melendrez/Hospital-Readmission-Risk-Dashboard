# Library dealing with files and paths. 
import os
# Library for data manipulation and analysis. 
import pandas as pd

# Creates a variable and finds the base directory or folder our .py script is inside. 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Creates a variable for the file path to the specific csv we are analyzing. 
file_path = os.path.join(BASE_DIR, "..", "data", "diabetic_data.csv")

# Prints out the script file we are working with. import_and_cleaning.py
print("\n")
print("Script file:", __file__)
# Prints out the file path to the specific csv file we are analyzing. 
print()
print("Resolved CSV path:", file_path)
print()

#Assigns the dataframe to the csv file being read. 
df = pd.read_csv(file_path)

#This line searches through the entire dataframe for any cells containing the string "?" and replaces them with pd.NA (pandas' standard way to represent missing values). 
# The modified dataframe is then reassigned back to df, so all subsequent operations work with the cleaned data.
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