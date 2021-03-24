import pandas as pd


def read_in_data():  # read in Data
    ageFactors = pd.read_csv("ageFactors.csv")
    ageFactors["ageFactor"] = (
        ageFactors["ageFactor"].str.rstrip("%").astype(float) / 100
    )

    genderFactors = pd.read_csv("genderFactors.csv")
    genderFactors["genderFactor"] = (
        genderFactors["genderFactor"].str.rstrip("%").astype(float) / 100
    )

    inforceFile = pd.read_csv("inforceFile.csv")
    inforceFile["AV"] = inforceFile["AV"].str.lstrip(" $").astype(float)

    # merge inforce file and assumptions
    inforceFile = inforceFile.merge(genderFactors)
    inforceFile = inforceFile.sort_values("Age")
    inforceFile = pd.merge_asof(inforceFile, ageFactors)
    return inforceFile