#PyPoll homework solution 
#--------------------------------------------------------------------------
#The total number of votes cast   
#A complete list of candidates who received votes   
#The percentage of votes each candidate won  
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv 

#Set input and output destinations
Election_Data = os.path.join("Resources", "PyPoll_Resources_election_data.csv")
Election_results_output = os.path.join("Analysis", "Election_results_output.txt")


total_vote_count = 0
candidates_list = []

#Use dictionary to store candidates(keys) and total vote counts (values)
vote_counts = {}
#Use dictionary to store candidates(keys) and vote ratio (values)
vote_ratio = {}


#Open and read the CSV file
with open(Election_Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    #Skip header row
    csv_header = next(csv_reader)

    #First loop runs through totals and locates candidates names in Column C  
    for row in csv_reader:
        
        total_vote_count += 1
        candidate_name = row[2]

              
        #Using if statement to append the candidates list with only unique values 
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            vote_counts[candidate_name] =0
        #Calculates total vote counts per candidate in dictionary
        vote_counts[candidate_name] += 1

#Find the percentage of the votes per candidate compared to total votes
for i in vote_counts:
    vote_ratio[i]= (vote_counts[i]/total_vote_count)

#Find the inverse of the total vote counts to find the winner
inverse = [(value,key) for key,value in vote_counts.items()]
Winner = max(inverse)[1]
#print(Winner)

#Setting variables for results list  
First_candidate = list(vote_counts.keys())[0]
Second_candidate=list(vote_counts.keys())[1] 
Third_candidate=list(vote_counts.keys())[2]
Fourth_candidate=list(vote_counts.keys())[3]     

First_candidate_votes=list(vote_counts.values())[0]  
Second_candidate_votes=list(vote_counts.values())[1] 
Third_candidate_votes=list(vote_counts.values())[2]
Fourth_candidate_votes=list(vote_counts.values())[3]       

first_percent = list(vote_ratio.values())[0]
second_percent = list(vote_ratio.values())[1]
third_percent = list(vote_ratio.values())[2]
fourth_percent = list(vote_ratio.values())[3]

#Print election results 
print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_vote_count))
print("---------------------")
print(str(First_candidate) + " : {:.2%}" .format(first_percent) + " (" + str(First_candidate_votes) + ")") 
print(str(Second_candidate) + " : {:.2%}" .format(second_percent) + " (" + str(Second_candidate_votes) + ")")
print(str(Third_candidate) + " : {:.2%}" .format(third_percent) + " (" + str(Third_candidate_votes) + ")")
print(str(Fourth_candidate) + " : {:.2%}" .format(fourth_percent) + " (" + str(Fourth_candidate_votes) + ")")
print("---------------------")
print("Winner: " + str(Winner))
#save output to be able to print and export to text file


# Output = (
# "Election Results\n"
# "---------------------\n"
# f"Total Votes: {total_vote_count}\n"
# "---------------------\n"
#(str(First_candidate) + " : {:.2%}" .format(first_percent) + " (" + str(First_candidate_votes) + ")"))
#f"{First_candidate}:  {:.2%}" .format(second_percent) \n" )
#f"{First_candidate} : {{:.2%}" .format(first_percent)}  ( {First_candidate_votes} ) \n" )
# print(str(Second_candidate) + " : {:.2%}" .format(second_percent) + " (" + str(Second_candidate_votes) + ")")
# print(str(Third_candidate) + " : {:.2%}" .format(third_percent) + " (" + str(Third_candidate_votes) + ")")
# print(str(Fourth_candidate) + " : {:.2%}" .format(fourth_percent) + " (" + str(Fourth_candidate_votes) + ")")) 
#print(Output)

#f"Greatest increase in profit: {Month_change_list[index1 +1]} : {Greatest_profit}\n"