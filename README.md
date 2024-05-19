# Python Challenge: PyBank and PyPoll

<img src="https://www.codecademy.com/resources/blog/wp-content/uploads/2022/12/10-Python-Code-Challenges-for-Beginners-1.png
" alt="Crowdfunding Project Analysis" style="width: 100%; height: auto;">

## Background
This project involves two Python challenges: PyBank and PyPoll. These challenges help transition from Excel-based analysis to more powerful Python scripting for handling large datasets. The tasks are based on analyzing financial records and election data using Python.

***

## Project Structure
The project repository is organized as follows:

```
python-challenge/
│
├── PyBank/
│ ├── Resources/
│ │ └── budget_data.csv
│ ├── analysis/
│ │ └── pybank_analysis.txt
│ └── main.py
│
├── PyPoll/
│ ├── Resources/
│ │ └── election_data.csv
│ ├── analysis/
│ │ └── pypoll_analysis.txt
│ └── main.py
│
└── README.md
```
***


## PyBank Instructions
In the PyBank challenge, the task is to analyze the financial records from a dataset called `budget_data.csv`. The dataset contains two columns: "Date" and "Profit/Losses". The script `main.py` calculates the following:

- The total number of months included in the dataset.
- The net total amount of "Profit/Losses" over the entire period.
- The changes in "Profit/Losses" over the entire period, and the average of those changes.
- The greatest increase in profits (date and amount) over the entire period.
- The greatest decrease in profits (date and amount) over the entire period.

The results are printed to the terminal and exported to `analysis/pybank_analysis.txt`.

## PyPoll Instructions
In the PyPoll challenge, the task is to help a small town modernize its vote-counting process using the dataset `election_data.csv`. The dataset includes three columns: "Voter ID", "County", and "Candidate". The script `main.py` calculates the following:

- The total number of votes cast.
- A complete list of candidates who received votes.
- The percentage of votes each candidate won.
- The total number of votes each candidate won.
- The winner of the election based on popular vote.

The results are printed to the terminal and exported to `analysis/pypoll_analysis.txt`.

## Example Code Snippet
Here's a snippet from the PyBank script that calculates the greatest increase and decrease in profits:

```python
# Calculate the greatest increase and decrease in profits
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

for i in range(1, len(profit_losses)):
    change = profit_losses[i] - profit_losses[i - 1]
    if change > greatest_increase[1]:
        greatest_increase = [dates[i], change]
    if change < greatest_decrease[1]:
        greatest_decrease = [dates[i], change]
```

***

#### Your analysis align with the following results:

```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

***

```Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

***
