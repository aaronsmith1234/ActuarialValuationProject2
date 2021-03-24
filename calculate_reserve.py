import import_data

inforceFile = import_data.read_in_data()

# calculate reserve
inforceFile["Reserve"] = (
    inforceFile["genderFactor"] * inforceFile["ageFactor"] * inforceFile["AV"]
)

# export
inforceFile.to_csv("reserves.csv")