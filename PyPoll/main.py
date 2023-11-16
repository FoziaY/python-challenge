import csv

# Open file
with open('Resources/election_data.csv', 'r') as file:
  csvReader = csv.reader(file)
  votes = 0

  # Create an empty candidates list
  candidates = []

  # Create an empty cand_votes dict
  cand_votes = {}
  next(csvReader)

  # Loop through csv
  for row in csvReader:
    candidate = row[2]

    # Add candidate to the list if they're not already in
    if candidate not in candidates:
      candidates.append(candidate)
    
    # Add candidate as the key 
    # and the number of occurences as the value
    cand_votes[candidate] = cand_votes.get(candidate, 0) + 1
    votes += 1
  
  # Output to file
  with open('analysis/election_analysis.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------------\n")
    output_file.write(f"Total Votes: {votes}\n")
    output_file.write("------------------------\n")

    # Calculate percentage for each candidate
    # and write to file
    for key, value in cand_votes.items():
      perc = (value / votes) * 100
      output_file.write(f"{key}: {perc:0.3f}% ({value})\n")

    output_file.write("------------------------\n")

    # Get the maximum vote by checking which
    # candidate has the highest frequency
    max_vote = max(cand_votes.values())
    for key, value in cand_votes.items():
      if value == max_vote:
        output_file.write(f"Winner: {key}\n")
        break
      
    output_file.write("------------------------\n")
    
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {votes}")
    print("------------------------")

    # Print candidate percentage
    for key, value in cand_votes.items():
      perc = (value / votes) * 100
      print(f"{key}: {perc:0.3f}% ({value})")

    print("------------------------")

    # Print max vote
    max_vote = max(cand_votes.values())
    for key, value in cand_votes.items():
      if value == max_vote:
        print(f"Winner: {key}")
        break

    print("------------------------")


