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


#Instantiating variables to hold election winner information
winningCandidate = ''
winningCount = 0
winningPercentage = 0



#Open the election results and read the file.
with open(csvFile) as election_data:

    #Reading 'election_results.csv' data, skipping the header row
    fileReader = csv.reader(election_data)
    headers = next(fileReader)

    #looping through rows
    for row in fileReader:
        #Increases 'totalVotes' count by 1
        totalVotes += 1

        #Assigning candidate name to variable
        candidateName = row[2]



        #Adds candidate name if not already in the 'candidateOptions' list
        if candidateName not in candidateOptions:
            candidateOptions.append(candidateName)

            #Instantiating 'candidateOptions' list variables to 0
            candidateVotes[candidateName] = 0

        #Increases vote count for specific candidate by 1
        candidateVotes[candidateName] +=1



#Opens 'election_analysis.txt' file output the results to
with open(saveFile, 'w') as txt_file:

    #Instantiating 'electionResults' string to hold header and total votes 
    electionResults = (
        f'\nElection Results\n'
        f'------------------------------\n'
        f'Total Votes: {totalVotes:,}\n'
        f'------------------------------\n'
    )

    #Print 'electionResults' string
    print(electionResults, end='')

    #Writes 'electionResults' to the 'election_analysis.txt' file
    txt_file.write(electionResults)

    #Loop to calculate percentages
    for candidateName in candidateVotes:
        
        #Instantiating 'votes' variable to hold vote count from specified 'candidateName'
        votes = candidateVotes[candidateName]

        #Calculates the percentage of votes for each candidate
        votePercentage = float(votes) / float(totalVotes) * 100

        #Instantiating string to hold 'candidateName','votePercentage','votes'
        candidateResults = (
            f'{candidateName}: {votePercentage:.1f}% ({votes:,})\n'
        )
        #Prints 'candidateResults'
        print(candidateResults)
        
        #Appends 'candidateResults' to 'election_analysis.txt'
        txt_file.write(candidateResults)

        #Finds the winner by looping through the candidate results, comparing to see who
        #has the highest vote count and percentage.
        if(votes > winningCount) and (votePercentage > winningPercentage):
            winningCount = votes
            winningPercentage = votePercentage
            winningCandidate = candidateName

    #Instantiating 'winningCandidateSummary' string to hold
    #the winners name, vote count and percentage
    winningCandidateSummary = (
        f'------------------------------\n'
        f'Winner: {winningCandidate}\n'
        f'Winning Vote Count: {winningCount:,}\n'
        f'Winning Percentage: {winningPercentage:.1f}%\n'
        f'------------------------------\n'
    )
    #Prints 'winningCandidateSummary' string
    print(winningCandidateSummary)

    #Appends 'winningCandidateSummary' to 'election_analysis.txt' file
    txt_file.write(winningCandidateSummary)