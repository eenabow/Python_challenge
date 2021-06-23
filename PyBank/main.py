#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
import os
import csv 

Financial_Data = os.path.join("Resources", "PyBank_Resources_budget_data.csv")
Financial_Analysis_output = os.path.join("Analysis", "Financial_Analysis_output.txt")
Total_Months = 0
Total_Net = 0



#Open and read the CSV file
with open(Financial_Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    #Skip header row
    csv_header = next(csv_reader)

    #Set list of difference in profits and losses
    Net_change_list = []
    Month_change_list = []
   
    #First loop runs through totals 
    for row in csv_reader:

        #calculate total months and total sum of profits/losses
        Total_Months += 1
        Total_Net += int(row[1])
        
        #Net Change is column C (differences list), Net Change List is storing values in column B
        Net_change = [] 
        #Adding column B values into a list
        Net_change_list.append(int(row[1]))
        #Adding column A values into a list
        Month_change_list.append(row[0])
        
        #Second loop runs through the actual calculation
        for i in range(1, len(Net_change_list)):
             Net_change.append(Net_change_list[i]-(Net_change_list[i-1]))


#Calculate average change using differences values    
Average_change = sum(Net_change)/ len(Net_change)

#Find the greatest profit/loss in Net Change 
Greatest_profit = max(Net_change)
Greatest_loss = min(Net_change)

#Find the index number to use for month correlation
index1 = Net_change.index(Greatest_profit)
index2 = Net_change.index(Greatest_loss)

#save output to be able to print and export to text file
Output = (
"Financial Analysis\n"
"---------------------\n"
f"Total Months: {Total_Months}\n"
f"Change over Period: {Total_Net}\n"
f"Average Change: {Average_change:.2f}\n"
f"Greatest increase in profit: {Month_change_list[index1 +1]} : {Greatest_profit}\n"
f"Greatest decrease in profit: {Month_change_list[index2 +1]} : {Greatest_loss}")

print(Output)

#Export to text file 

with open(Financial_Analysis_output, "w") as txt_file: 
    txt_file.write(Output)
