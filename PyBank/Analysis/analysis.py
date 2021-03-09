import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

number_of_months = 0
total_net = 0



# Read in the CSV file
with open(budget_csv) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #removing header from data
    header = next(csvreader)
    first_row = next(csvreader)
    total_net += int(first_row[1])

    

    for row in csvreader:
        
        #short hand for number of months equal to number of months (number_of_months = number_of_months + 1)
        number_of_months +=1 
        total_net += int(row[1])
# Print total months and profit/loss
    print(f"Total number of months is {number_of_months}")
    print(f"Profit or loss is {total_net}")
    
    





   # def print_percentages(row):
#     # row is a list of wrestler data
#     print("wrestler was found in the following row")

# The net total amount of "Profit/Losses" over the entire period
# print("Profit or loss is")
#     Profit/Loss = int(row[1])

# # The average of the changes in "Profit/Losses" over the entire period
# def arithmetic_mean(budget_csv[1]):
#     #nums is a list of numbers
#     if len(budget_csv) == 0:
#         return None
#     sum = 0
#     for num in nums:
#         sum = sum + num
#     return sum/len(nums)

# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period


            
            


