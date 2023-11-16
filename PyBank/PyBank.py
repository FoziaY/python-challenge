import csv

# Open file
with open('budget_data.csv', 'r') as file:
  csvReader = csv.reader(file)
  months = 0
  net = 0
  next(csvReader)
  profits = []
  dates = []

  # Loop through csv and keep count of some values
  for row in csvReader:
    net += int(row[1])
    months += 1
    dates.append(row[0])
    profits.append(int(row[1]))

  # Create a list of changes
  change = []
  for i in range(len(profits) - 1):
    change.append(profits[i+1] - profits[i])
  
  # Calculate the greatest increase in profits/losses
  greatest_incr = max(change)
  # Calculate the greatest decrease in profits/losses
  greatest_decr = min(change)

  
  max_date = ""
  min_date = ""

  # Finds the date for the greatest changes
  for i in range(len(profits) - 1):
    if profits[i + 1] - profits[i] == greatest_incr:
      max_date = dates[i + 1]
    if profits[i + 1] - profits[i] == greatest_decr:
      min_date = dates[i + 1];

  total = 0

  # Calculate Average Change
  for num in change:
    total += num
  avg_chng = total / len(change)
  
  # Print Putput and write to file
  print("Financial Analysis")
  print("----------------------------")

  print("Total Months:", months)
  print(f"Total: ${net}")
  print(f"Average Change: ${avg_chng:0.2f}")
  print(f"Greatest Increase in profits: {max_date} (${greatest_incr})")

  print(f"Greatest Decrease in profits: {min_date} (${greatest_decr})")

  with open('budget_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {months}\n")
    output_file.write(f"Total: ${net}\n")
    output_file.write(f"Average Change: ${avg_chng:0.2f}\n")
    output_file.write(f"Greatest Increase in profits: {max_date} (${greatest_incr})\n")
    output_file.write(f"Greatest Decrease in profits: {min_date} (${greatest_decr})\n")

