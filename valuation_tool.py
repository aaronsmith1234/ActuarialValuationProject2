import pandas as pd

input_folder = "input_files/"
output_folder = "output_files/"

# read in Data
ageFactors = pd.read_csv(input_folder + "ageFactors.csv")
ageFactors["ageFactor"] = ageFactors["ageFactor"].str.rstrip("%").astype(float) / 100

genderFactors = pd.read_csv(input_folder + "genderFactors.csv")
genderFactors["genderFactor"] = (
    genderFactors["genderFactor"].str.rstrip("%").astype(float) / 100
)

inforceFile = pd.read_csv(input_folder + "inforceFile.csv")
inforceFile["AV"] = inforceFile["AV"].str.lstrip(" $").astype(float)

# merge inforce file and assumptions
inforceFile = inforceFile.merge(genderFactors)
inforceFile = inforceFile.sort_values("Age")
inforceFile = pd.merge_asof(inforceFile, ageFactors)

# calculate reserve
inforceFile["Reserve"] = (
    inforceFile["genderFactor"] * inforceFile["ageFactor"] * inforceFile["AV"]
)

# export
inforceFile.to_csv(output_folder + "reserves.csv")