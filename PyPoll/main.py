#PyPoll homework solution 

import os
import csv 

Election_Data = os.path.join("Resources", "PyPoll_Resources_election_data.csv")

total_vote_count = 0

#Open and read the CSV file
with open(Election_Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    #Skip header row
    csv_header = next(csv_reader)

    for row in csv_reader:
        #calculate total vote count
        total_vote_count += 1

        
        #Total_Net += int(row[1])
        #Average
print("Total Votes:"+ str(total_vote_count))
#print("Net over Period:"+ str(Total_Net))