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
        if (cand == "" or cand == " "):
            break
        # If the name is not in the dictionary, add it with a value of 0
        if cand not in canVotes:
            canVotes[cand] = 0
        # Add 1 to  the name's counter
        canVotes[cand] += 1
        # Add 1 to total votes
        totalVotes += 1

    # Print out results 
    print("Election Results")
    print("--------------------")
    print(f'Total Votes: {totalVotes}')
    print("--------------------")
    
    # Go through dictionary canVotes to get and print results for each candidate 
    #f For c in canVotes (c is the name, canVotes[c] gets the value, in this case number of votes):
    for c in canVotes:
        name = c
        votes = canVotes[c]
        percentVotes = (votes/totalVotes*100) 
        formatted_percentVotes = "{:.3f}".format(percentVotes)
        # Print candidate information
        print(f'{name}: {formatted_percentVotes}% {votes}')
        # Get the highest number of votes to determine winner
        if (votes > votesSoFar):
            votesSoFar = votes
            winnerSoFar = name
    print("--------------------")
    print(f'Winner: {winnerSoFar}')
    print("--------------------")   

        # Write results to file
    # Establish the path to the file output.txt
    outpath = os.path.join('.','Analysis', 'output.txt')

    # Open the file
    f = open(outpath,"w")
    f.write("Election Results \n")
    f.write("-------------------- \n")
    f.write(f'Total Votes: {totalVotes} \n')
    f.write("-------------------- \n")
    # Go through dictionary canVotes to get and write to file the results for each candidate
    # Wish I had known how to save the formatted stuff printed out above to avoid looping again 
    # For c in canVotes (c is the name, canVotes[c] gets the value, in this case number of votes):
    for c in canVotes:
        name = c
        votes = canVotes[c]
        percentVotes = (votes/totalVotes*100) 
        formatted_percentVotes = "{:.3f}".format(percentVotes)
        # Print candidate information
        f.write(f'{name}: {formatted_percentVotes}% {votes} \n')
        # Get the highest number of votes to determine winner

    f.write('-------------------- \n')
    f.write('Winner: {winnerSoFar} \n')
    f.write('-------------------- \n')   
    f.close()
