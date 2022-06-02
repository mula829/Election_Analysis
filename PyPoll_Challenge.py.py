# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
counties_options = []
counties_votes = {}

# 1: Create a county list and county votes dictionary.
counties_name = []

counties_votes = {}

# Track the winning candidate, vote count and percentage
winning_county = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    
    print(election_data)
    
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        counties_name=[1] 

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if counties_name not in counties_options:

            # Add the candidate name to the candidate list.
            counties_options.append(counties_name)

            # And begin tracking that candidate's voter count.
            counties_votes[counties_name] = 0

        # Add a vote to that candidate's count
        counties_votes[counties_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
    if counties_name not in counties_options:
        # Add a vote to that candidate's count.
            counties_votes[counties_name] += 1

            # 4b: Add the existing county to the list of counties.
            counties_options.append(counties_name)

            # 4c: Begin tracking the county's vote count.
            counties_votes[counties_name] = 0

        # 5: Add a vote to that county's vote count.
            counties_votes[counties_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    counties_results = (
        f"\nCounties Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(counties_results, end="")

    txt_file.write(counties_results)

    # 6a: Write a for loop to get the county from the county dictionary.
for county in counties_name:
    print(county)
        # 6b: Retrieve the county vote count.
    votes = counties_votes[counties_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    counties_results = (
        f"{counties_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # 6c: Calculate the percentage of votes for the county.
    votes = counties_name[counties_votes]
    vote_percentage = float(votes) / float(total_votes) * 100
  
         # 6d: Print the county results to the terminal.
    winning_counties_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_counties_summary)
         # 6e: Save the county votes to a text file.
txt_file.write(counties_dict)
         # 6f: Write an if statement to determine the winning county and get its vote count.
print(winning_counties_summary)

    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
for counties_name in counties_votes:

        # Retrieve vote count and percentage
        votes = counties_votes.get(counties_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{counties_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(counties_results)
        #  Save the candidate results to our text file.
        txt_file.write(counties_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_county = votes
            winning_counties = counties_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
        winning_counties_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_counties_summary)

    # Save the winning candidate's name to the text file
txt_file.write(winning_counties_summary)
