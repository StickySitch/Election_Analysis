# Election Audit: Colorado Board of Elections
## Overview & Purpose
To help the Colorado Board of Elections, I've employed the power of the Python programming language to audit their election data. The purpose of this election audit is to gather and calculate the data below. With this data we can easily calculate and display the election winner; Along with other important metrics such as turnout percentage.
#### Data:
- Total  votes
##### County Data
- County vote counts
- County vote percentage (Turnout percentage)
- County with the largest turnout
##### Candidate Data
- Candidate name
- Candidate vote count
- Candidate vote percentage
##### Winner Data
- Winner name
- Winning vote count
- Winning percentage
## Resources
- **Source Data:** election_results.csv
- **Language & Version:** Python 3.7.6
- **Software:** Visual Studio Code
## Results
Now that the basic information is out of the way, lets get down to the nitty gritty! Below you can see an image of the data results:
#### Data Results:
![All Results Image](https://github.com/StickySitch/Election_Analysis/blob/main/Analysis/ImgResources/C7CR0Xn.png)


Now lets break down the precinct data a little bit!

- **Total votes cast in the congressional election**
	- As displayed above, you can see in this election, there was a total of ```369,711``` votes. Below, you will see the breakdown of the counties in the precinct.
	
- **Breakdown of each counties total votes & vote percentage**
The audit of the election yielded results for three counties:  ```Jefferson```, ```Denver``` and ```Arapahoe```.
	
	- **Jefferson County Results:**
		- Jefferson county has a vote count of ```38,855```. With this vote count, Jefferson makes up ```10.5%``` of the total votes cast.
	- **Denver County Results:**
		- Denver county fills a much larger percentage of the election "pie" with a total vote count of ```306,055```! Denver's votes account for ```82.8%``` of the  total votes of the election!
	- **Arapahoe County Results:**
		- Arapahoe has the lowest vote count of all the counties. The total vote count is ```24,801```. Their ```24,801``` votes make up ```6.7%```.
- **County with Largest Vote Count**
	- It's easy to see who the victor is here. With ```Denver``` making up ```82.8%``` of the total votes, they by far have the largest vote count out of all of the counties. 

- **Breakdown of votes & vote percentage for candidates**
This election had three candidates: ```Charles Casper Stockham```, ```Diana DeGette```, and ```Raymon Anthony Doane```
	- ```Charles Casper Stockham```
		- **Vote Count:** ```85,213```
		- **Vote Percentage:** ```23.0%```
		
	- ```Diana DeGette```
		- **Vote Count:** ```272,892```
		- **Vote Percentage:** ```73.8%```
		
	- ```Raymon Anthony Doane```
		- **Vote Count:** ```11,606```
		- **Vote Percentage:** ```3.1%```
		
- **Winner of the Election**
	- ```Diana DeGette``` has won by a landslide! With a vote count of ``` 272,892```, Diana has over **triple** the votes of the runner up! Diana accumulated ```73.8%``` of the total votes. 
### County Results Code: 
```python
#Instantiating county list and county votes dictionary.
countyList  = []
countyVotes  = {}
```
To begin we instantiate a list to hold the county names from the for loop below.

```python
# For each row in the CSV file.
for  row  in  reader:
	# Adds a vote to the "total_votes" count.
	total_votes  =  total_votes  +  1
	
	#Gets the candidate name from the current row
	candidate_name  =  row[2]
	
	#Extracts the county name from the current row
	countyName  =  row[1]
```
Above you can see a snippet of the ```for loop``` that is iterating through the .csv file. The part we want to look at is ```countyName  =  row[1]```. This line of code, grabs the county name associated with the row the iteration is currently on and assigns it to ```countyName```. Below you can see the ```countyName``` variable being used in our ```if statement```:
```python
#WE ARE CURRENTLY INSIDE THE FOR LOOP FROM ABOVE
#Checks if "countyName" not already in "countyList"
#Adds "countyName" to the list if not already in there.
if  countyName  not  in  countyList:
	#Adds the county to the list of counties.
	countyList.append(countyName)
	
	#Begins tracking the county's vote count.
	countyVotes[countyName] =  0
	
#Adds a vote to that county's vote count.
countyVotes[countyName] +=  1
```
The ```countyName``` of the current row from our ```countyName  =  row[1]``` code above is used as a reference in our if statement. ```if  countyName  not  in  countyList:``` checks the ```countyList  = []``` we instantiated at the start for the ```countyName```. If the name does NOT already exist in the list, two things happen:
1. First we add the ```countyName``` to our ```countyList  = []``` using the append function like so: ```countyList.append(countyName)```.

2. Since the ```countyName``` wasn't already in our ```countyList  = []```, this would be the first time we are running into the county. Now that be have added the county to the list in the first step, we need to make the counties votes count equal to zero: ```countyVotes[countyName] =  0```. This will assign our ```countyName``` a value of zero and add it to the ```countyVotes``` dictionary.

After the two steps above, the ```if statement``` is left and a vote is added to the counties vote count: ```countyVotes[countyName] +=  1```

#### County Results Calculations:
Now that we have our list of counties and the vote count that county accumulated, we can make our calculations.
```python
for  countyNames  in  countyVotes:
	#Retrieves the county vote count.
	county  =  countyVotes.get(countyNames)
	
	#Calculates the percentage of votes for the county.
	countyVotePerc  =  float(county) /  float(total_votes) *  100
```
Above we have a snippet of a new ```for loop``` that is iterating through the ```countyNames``` in the ```countyVotes``` dictionary.

The first line executed in our for loop is: ```county  =  countyVotes.get(countyNames)```. Using the .get() function, we are retrieving the ```countyNames``` vote count and assigning it to a new variable called ```county```.
Now that we have the vote count for the county, we can calculate the percentage of votes the county is responsible for. To do this we simply divided the counties vote count with the total votes, then multiplying by 100 to get our percentage value, like so: ```countyVotePerc  =  float(county) /  float(total_votes) *  100```
#### Finding the County with the most votes:
Lastly for our counties we want to find the county with the largest turnout. To do this, we can use an ```If statement``` like the snippet below:
```python
if (county  >  winningCountyCount) & (countyVotePerc  >  winningCountyTurnout):
	winningCountyCount  =  county
	largestCounty  =  countyNames
	winningCountyTurnout  =  countyVotePerc
```
This ```if statement``` is checking to see if the county in the current iteration of the ```for loop``` has a greater vote count AND percentage than the previous "highest" number assigned. If they are greater, the ```countyName``` is assigned to the ```largestCounty``` variable. The vote count and percentage are also assigned to their own variables. 



### Candidate Results Code: 
Since the code to do calculate the candidate results is essentially identical to county calculations, I will just post of few snippets of importance.
#### Gets candidate names, and tally's the votes:
```python
for  row  in  reader:
	# Adds a vote to the "total_votes" count.
	total_votes  =  total_votes  +  1
	
	#Gets the candidate name from the current row
	candidate_name  =  row[2]
	
	#Extracts the county name from the current row
	countyName  =  row[1]
	
	# If the candidate does not match any existing candidate add it to
	# the candidate list
	if  candidate_name  not  in  candidate_options:
		# Add the candidate name to the candidate list.
		candidate_options.append(candidate_name)
	
		# And begin tracking that candidate's voter count.
		candidate_votes[candidate_name] =  0
	
		# Add a vote to that candidate's count
		candidate_votes[candidate_name] +=  1
```
As you can see, like I said, essentially identical.
#### Candidate Results Calculations:

```python
#Iterates through "candidate_votes", prints and calculate candidate results

for  candidate_name  in  candidate_votes:
	# Retrieve vote count
	votes  =  candidate_votes.get(candidate_name)
	
	# Calculate percentage
	vote_percentage  =  float(votes) /  float(total_votes) *  100

	candidate_results  = (
	f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

  

	# Prints each candidate's voter count and percentage to the
	# terminal.
	print(candidate_results)

	# Saves the candidate results to our text file.
	txt_file.write(candidate_results)
	
	# Determine winning vote count, winning percentage, and candidate.
	if (votes  >  winning_count) and (vote_percentage  >  winning_percentage):
		winning_count  =  votes
		winning_candidate  =  candidate_name
		winning_percentage  =  vote_percentage
```
Same old same old here! Just like the counties, the candidate with the highest vote count and percentage is found using our ```if statement``` at the bottom. The percentage calculations are also done up above, just like before.
## **Election-Audit Summary**
As you can see from everything I have shown you, this script has worked wonders for this current election. Using this script for other elections will be even easier now! With a few changes, we can use this script with any election. For example, if we simply change our ```file_to_load  =  os.path.join("Resources", "election_results.csv")``` file path to the a new elections data set, our script, without any other modifications could perform the same analysis and calculations as this election.
There is also an opportunity to handle larger elections. For example, we could simply change our counties to States. The last modification needed to complete a national election would be to make sure our  ```countyName  =  row[1]```, which would now be ```stateName```, is referencing the correct row of the .csv file (Election data)
