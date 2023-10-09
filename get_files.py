import os

for dataset in ["training_data", "testing_reviewer1", "testing_reviewer2"]:
    for patient in os.listdir(dataset):
        print("23,23,23,23,23,23," + dataset + "/" + patient)
    print("\n\n")