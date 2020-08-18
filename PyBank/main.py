#Import module 'os' to create file paths across operating systems and modue 'csv' to read / write csv tiles
import os
import csv

# Establish the path to the file budget_data.csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Open the file
with open(csvpath) as csvfile:
    # Declare variable for contents and specify delimiter 
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    csv_header = next(csvreader)

    # Declare counters and placeholder variables
    # Profit or loss last month
    lastMonthResult = 0
    # Change in results this month (this month's results minus last month's results)
    thisMonthChange = 0
    # Biggest increase month-to-month so far
    increaseSoFar = 0
    # Month of biggest increase so far
    increaseMonth = " "
    # Biggest decrease month-to-month so far
    decreaseSoFar = 0
    # Month of biggest decrease so far
    decreaseMonth = " "
    # Total profit or loss
    total = 0
    #Total changes
    totalChange = 0
    # Number of months
    monthCount = 0

    # Read each row in the csvreader file
    for row in csvreader:
        # Except for the first month
        if monthCount != 0:
            # Calculate the change (increase or decrease)
            thisMonthChange = int(row[1]) - lastMonthResult
        
        # If this month profit or loss minus lastMonthResult is greater than increase so far, set increase so far to this month
        if (int(row[1]) - lastMonthResult) > increaseSoFar:
            increaseSoFar = thisMonthChange
            increaseMonth = row[0]
        # Else if this month profit or loss minus lastMonthResult is less than biggest decreaseSoFar set decrease so far to this month
        elif (int(row[1]) - lastMonthResult) < decreaseSoFar:
            decreaseSoFar = thisMonthChange
            decreaseMonth = row[0]
        
        # Add this month's results to total
        total = total + int(row[1])
        # Add this month change to total change
        totalChange = totalChange + thisMonthChange
        # Set last month result to this month's results
        lastMonthResult = int(row[1])
        # Add 1 to month count
        monthCount += 1
    
    # Calculate average change
    averageChange = round((totalChange / (monthCount - 1)),2)

    # Print out results 
    print("Financial Analysis")
    print("--------------------")
    print(f'Total Months: {monthCount}')
    print(f'Total: ${total}')
    print(f'Average Change: ${averageChange}')
    print(f'Greatest Increase in Profits: {increaseMonth} ${increaseSoFar}')
    print(f'Greatest Decrease in Profits: {decreaseMonth} ${decreaseSoFar}')



    
    # Write results to file
    # Establish the path to the file output.txt
    outpath = os.path.join('..','Analysis', 'output.txt')

    # Open the file
    f = open(outpath,"w")
    f.write("Financial Analysis \n")
    f.write("-------------------- \n")
    f.write(f'Total Months: {monthCount} \n')
    f.write(f'Total: ${total} \n')
    f.write(f'Average Change: ${averageChange} \n')
    f.write(f'Greatest Increase in Profits: {increaseMonth} ${increaseSoFar} \n')
    f.write(f'Greatest Decrease in Profits: {decreaseMonth} ${decreaseSoFar} \n')
    f.close()



