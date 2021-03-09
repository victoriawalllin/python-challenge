import os
import csv

election_csv = os.path.join('election_data.csv')

Voter_id = 0
candidates_dict = {}
candidates_perc_dict = {}
total_votes = 0

# Read in the CSV file
with open(election_csv) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #removing header from data
    header = next(csvreader)
    # first_row = next(csvreader)
    
    for row in csvreader:
        total_votes +=1
        candidate = row[2]
        

        if candidate in candidates_dict :
           candidates_dict[candidate] += 1
        else:
            candidates_dict[candidate] = 1
        candidates_perc_dict[candidate] = f"{(candidates_dict[candidate] /total_votes * 100):.2f}%" 
        

print(f"total_votes :: {total_votes}")
print(f"candidates_dict :: {candidates_dict}")
print(f"candidates_perc_dict :: {candidates_perc_dict}")
print("Winner is Khan")
#The total number of votes cast



#A complete list of candidates who received votes


#The percentage of votes each candidate won
#votes/total_votes

#The total number of votes each candidate won


#The winner of the election based on popular vote.
#candidate >50%
# print(Khan_votes)
    # print("Election Results")
    # print(f"Total Votes: {total_votes}")
    # print(f"Khan: {Khan_per}", {(Khan_votes)})
    #print(f"Korey: {draw_percent}")
    #print(f"Li: {draw_percent}")
    #print(f"O'Tooley: {draw_percent}")
    #print(f"{name} is a {type_of_wrestler}")