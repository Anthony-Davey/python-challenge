#Modules
import os
import csv

#Set path for file
path = "C:\\Users\\Gamer\\OneDrive\\Desktop\\upenn\\homework\\python-challenge\\PyPoll\\"
csvpath = os.path.join(path, "Resources", "election_data.csv")

#Open the csv
with open(csvpath, encoding = 'utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    count = 0
    percentVote = 0.00
    totalIndVotes = 0 
    voterList = []
    resultDict = {}
    for row in csvreader:
        count += 1
        #total number of votes in dataset
        totalVotes = count

        #if current row is not in list then add to list and add to vote counter
        #if not then add up votes as it's the same candidate
        if row[2] not in voterList:
            voterList.append(row[2])
            resultDict[row[2]] = 1
        else:
            resultDict[row[2]] += 1

    max_key = max(resultDict, key = resultDict.get)

    str1 = print("Election Results")
    str2 = print("----------------------")
    str3 = print(f'Total Votes: {totalVotes}')
    str4 = print("----------------------")     
    for key, value in resultDict.items() :
        str5 = print (f'{key} {"{:.3%}".format(value/totalVotes)} ({value}) \n')
    str6 = print("----------------------")
    str7 = print(f'Winner: {max_key}')
    str8 = print("----------------------")
    
    analysisOutput = open("C:\\Users\\Gamer\\OneDrive\\Desktop\\upenn\\homework\\python-challenge\\PyPoll\\Analysis\\analysisOutput.txt","w")
    analysisOutput.write("Election Results \n")
    analysisOutput.write("----------------------\n")
    analysisOutput.write(f'Total Votes: {totalVotes}\n')
    analysisOutput.write("----------------------\n")
    analysisOutput.write(f'{key} {"{:.3%}".format(value/totalVotes)} ({value}) \n')
    analysisOutput.write("----------------------\n")
    analysisOutput.write(f'Winner: {max_key}\n')
    analysisOutput.write("----------------------\n")
    analysisOutput.close()
    

    
        