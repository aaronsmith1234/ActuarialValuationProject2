import import_data

inforceFile = import_data.read_in_data()

output_folder = "output_files/"
# calculate reserve
inforceFile["Reserve"] = (
    inforceFile["genderFactor"] * inforceFile["ageFactor"] * inforceFile["AV"]
)

# export
inforceFile.to_csv(output_folder + "reserves.csv")