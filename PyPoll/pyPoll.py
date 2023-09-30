import os
import csv

# Set path for the election data CSV file
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    csv_header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate's name
        candidate = row[2]

        # If the candidate is not in the list, add them
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Increment the candidate's vote count
        candidate_votes[candidate] += 1
    # Calculate the percentage of votes each candidate won
candidate_percentages = {}
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage
print (total_votes)
print(candidate_votes)
print(candidates)
print(candidate_percentages)
# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis results to a text file
output_file = os.path.join("PyPoll", "analysis", "election_results.txt")
print ("test",output_file)
output_file = "election_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
