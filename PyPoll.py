import csv
import os

#Instantiate variable to hold 'election_results.csv' data
csvFile = os.path.join('Resources','election_results.csv')

#Instantiate variable to hold output file
saveFile = os.path.join('Analysis', 'election_analysis.txt')

#Instantiating varable to hold total vote count
totalVotes = 0
#Instantiating list to hold candidate optoins
candidateOptions = []
#Instantiating dict to hold the votes for each candidate
candidateVotes = {}


#Open the election results and read the file.
with open(csvFile) as election_data:

    #Reading 'election_results.csv' data, skipping the header row
    fileReader = csv.reader(election_data)
    headers = next(fileReader)

    #looping through rows
    for row in fileReader:
        totalVotes += 1

        #Assigning candidate name to variable
        candidateName = row[2]
        #Adds candidate name if not already in the 'candidateOptions' list
        if candidateName not in candidateOptions:
            candidateOptions.append(candidateName)

            #Instantiating 'candidateOptions' list variables to 0
            candidateVotes[candidateName] = 0
        candidateVotes[candidateName] +=1


#Loop to calculate percentages
for candidateName in candidateVotes:
    
    votes = candidateVotes[candidateName]
    #Calculates the percentage of votes for each candidate
    votePercentage = float(votes) / float(totalVotes) * 100

    print(f'{candidateName}: recieved {votePercentage:.1f}% of the vote.')

#Opening and writing to output file
with open(saveFile, 'w') as txt_file:
    txt_file.write('Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson')
    



#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of the candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
