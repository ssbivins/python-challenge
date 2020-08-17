#Import module 'os' to create file paths across operating systems and modue 'csv' to read / write csv tiles
import os
import csv

# Establish the path to the file budget_data.csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open the file
with open(csvpath) as csvfile:
    # Declare variable for contents and specify delimiter 
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    csv_header = next(csvreader)

    # Declare counters and placeholder variables
    # Total number of votes cast
    totalVotes = 0
    # Dictionary with candidate : vote counts 
    canVotes = {}
    

    # Read each row in the csvreader file
    for row in csvreader:
        # Get the row[2] to get the candidate's name
        cand = row[2]
        # If the name is not in the dictionary, add it with a value of 0
        if cand not in canVotes:
            canVotes[cand] = 0
        # Add 1 to  the name's counter
        canVotes[cand] += 1
    print(canVotes)