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
    # Percent holder
    percentVotes = 0.000
    # Highest (winner) vote count holder
    winnerSoFar = ""
    votesSoFar = 0
    
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

    # Print out results 
    print("Election Results")
    print("--------------------")
    print(f'Total Votes: {totalVotes}')
    print("--------------------")
    
    # Go through dictionary canVotes to get and print results for each candidate 
    for k,v in canVotes:
        name = k
        votes = int(v)
        percentVotes = (v/totalVotes*100)
        print(f'{name} {votes} {percentVotes}%') 
        # Print candidate information
        print(f'{name}:  {percentVotes}% ({votes})'
        # Get the highest number of votes to determine winner
        #if (votes > votesSoFar):
        #    votesSoFar = votes
        #    winnerSoFar = k
    print("--------------------")
    print(f 'Winner: ' {winnerSoFar})
    print("--------------------")   

    print(f'Total: ${total}')
    print(f'Average Change: ${averageChange}')
    print(f'Greatest Increase in Profits: {increaseMonth} ${increaseSoFar}')
    print(f'Greatest Decrease in Profits: {decreaseMonth} ${decreaseSoFar}')
