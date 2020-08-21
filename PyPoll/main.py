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

    # Print out results on console and write them to console and file
    # Console
    # Print a blank line first (to distinguish the Election results from whatever is above)
    print(" ")
    print("Election Results")
    print("--------------------")
    print(f'Total Votes: {totalVotes}')
    print("--------------------")
   
    
    # Establish the path to the file output.txt
    outpath = os.path.join('.','Analysis', 'output.txt')
    # Open the file and write initial content
    f = open(outpath,"w")
    f.write("Election Results \n")
    f.write("-------------------- \n")
    f.write(f'Total Votes: {totalVotes} \n')
    f.write("-------------------- \n")
    
    # Go through dictionary canVotes to get and print results for each candidate and also write them to file 
    #f For c in canVotes (c is the name, canVotes[c] gets the value, in this case number of votes):
    for c in canVotes:
        name = c
        votes = canVotes[c]
        percentVotes = (votes/totalVotes*100) 
        formatted_percentVotes = "{:.3f}".format(percentVotes)
        # Print candidate information and also write it to file
        print(f'{name}: {formatted_percentVotes}% {votes}')
        # Write candidate information to file
        f.write(f'{name}: {formatted_percentVotes}% {votes} \n')
        
        # Get the highest number of votes to determine winner
        if (votes > votesSoFar):
            votesSoFar = votes
            winnerSoFar = name
   
    # Print winner information
    print("--------------------")
    print(f'Winner: {winnerSoFar}')
    print("--------------------")   
    
    # Write winner information to file and close it
    f.write('-------------------- \n')
    f.write(f'Winner: {winnerSoFar} \n')
    f.write('-------------------- \n')   
    f.close()
