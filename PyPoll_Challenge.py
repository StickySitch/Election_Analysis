# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#Instantiating Candidate Options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}

#Instantiating county list and county votes dictionary.
countyList = []
countyVotes = {}


# Instantiating variables to track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Instantiating variables to track the largest county and county voter turnout.
largestCounty = ''
winningCountyCount = 0
winningCountyTurnout = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Adds a vote to the "total_votes" count.
        total_votes = total_votes + 1

        #Gets the candidate name from the current row
        candidate_name = row[2]

        #Extracts the county name from the current row
        countyName = row[1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Checks if "countyName" not already in "countyList"
        #Adds "countyName" to the list if not already in there.
        if countyName not in countyList:

            #Adds the county to the list of counties.
            countyList.append(countyName)

            #Begins tracking the county's vote count.
            countyVotes[countyName] = 0

        #Adds a vote to that county's vote count.
        countyVotes[countyName] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    #Iterates through "countyVotes", prints and calculate county results
    for countyNames in countyVotes:
        
        #Retrieves the county vote count.
        county = countyVotes.get(countyNames)

        #Calculates the percentage of votes for the county.
        countyVotePerc = float(county) / float(total_votes) * 100

        #Prints the county results to the terminal.
        countyResults = (
        f'{countyNames}: {countyVotePerc:.1f}% ({county:,})\n')
        print(countyResults)

         #Saves the county votes to a text file.
        txt_file.write(countyResults)

         #if statement that determines the winning county and get its vote count.
        if (county > winningCountyCount) & (countyVotePerc > winningCountyTurnout):
            winningCountyCount = county
            largestCounty = countyNames
            winningCountyTurnout = countyVotePerc

    #Print the county with the largest turnout to the terminal.
    print((f'\n--------------------------------------\n'
            f'County With Largest Turnout: {largestCounty}'
            f'\n--------------------------------------\n'))

    #Saves the county with the largest turnout to a text file.
    txt_file.write(f'\n--------------------------------------\n'
            f'County With Largest Turnout: {largestCounty}'
            f'\n--------------------------------------\n')
           
          

    #Iterates through "candidate_votes", prints and calculate candidate results
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Saves the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"--------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
