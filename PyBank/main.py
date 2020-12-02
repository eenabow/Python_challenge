#PyBank homework solution 

import os
import csv 

Financial_Data = os.path.join("Resources", "PyBank_Resources_budget_data.csv")


Total_Months = 0
Total_Net = 0
Average_Change = []
previous_profit = int(first_row[1])
Greatest_profit_increase = []
Greatest_loss_decrease = []

#Open and read the CSV file
with open(Financial_Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    #Skip header row
    csv_header = next(csv_reader)

    #I don't understand the below 
    first_row = next(csv_reader)
    Total_Net += int(first_row[1])

    for row in csv_reader:
        #calculate total months
        Total_Months += 1
        Total_Net += int(row[1])

        #Calculate change in net
        Net_change = float(row[1]) - previous_profit
        previous_profit = int(row[1])
        net_change_list += [row[0]]

        Average_change = sum(net_change_list)/ len(net_change_list)
        
print("Total Months:"+ str(Total_Months))
print("Net over Period:"+ str(Total_Net))
print("Average Change:"+ str(Average_change))

