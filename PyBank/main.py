import os
import csv 

Financial_Data = os.path.join("Resources", "PyBank_Resources_budget_data.csv")
print(type(Financial_Data))

Total_Months = 0
Net_Period = []
with open(Financial_Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = "\t")
    
    for row in csv_reader:
        print("Financial Analysis")


