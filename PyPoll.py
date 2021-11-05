import csv
import os


csvFile = os.path.join('Resources','election_results.csv')
saveFile = os.path.join('Analysis', 'election_analysis.txt')

#Open the election results and read the file.
with open(csvFile) as election_data:
    # To Do: Read and analyze data
    fileReader = csv.reader(election_data)
    headers = next(fileReader)
    print(headers)

    
    #for row in fileReader:
       





with open(saveFile, 'w') as txt_file:
    txt_file.write('Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson')
    



#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of the candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
