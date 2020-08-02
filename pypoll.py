import csv
import os

# The data we need to retrieve
file_to_load = os.path.join('..', 'election_analysis', 'election_results.csv')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

file_to_save = os.path.join('..', 'election_analysis', "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote