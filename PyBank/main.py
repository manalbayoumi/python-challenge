import csv

# Set path for the csv file
budget_data_csv = "PyBank/Resources/budget_data.csv"

#Initialize the variables to hold data
total_months = 0
total_profit_loss = 0
sum_profit_loss_change=0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the rows in the csv file
    for row in csvreader:

        # Count the total number of months in the dataset
        total_months += 1

        # Calculate the total profit/loss over the entire period
        total_profit_loss += int(row[1])

  # Calculate the change in profit/loss between the current row and the previous row
        if total_months > 1: 
            profit_loss_change = int(row[1]) - prev_profit_loss
            sum_profit_loss_change = sum_profit_loss_change + profit_loss_change
            

            # Find the greatest increase in profits (date and amount) over the entire period
            if (profit_loss_change > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change

            # Find the greatest decrease in losses (date and amount) over the entire period
            if (profit_loss_change < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change

# Calculate the average change in profit/loss over the entire period
        prev_profit_loss = int(row[1])
average_change = round(sum_profit_loss_change/(total_months - 1), 2)


# Print the financial analysis to the console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
path= "analysis_report.txt"
with open (path,"w") as output: 
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${total_profit_loss}\n")
    output.write(f"Average Change: ${average_change}\n")
    output.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
