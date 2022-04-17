#Modules
import os
import csv

#Set path for file
path = "C:\\Users\\Gamer\\OneDrive\\Desktop\\upenn\\homework\\python-challenge\\PyBank\\"
csvpath = os.path.join(path, "Resources", "budget_data.csv")

#Open the csv
with open(csvpath, encoding = 'utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    firstRow = next(csvreader)
    #loop through the data
    count = 1
    dictCount = 0
    totalPL = 0
    prev = int(firstRow[1])
    changeList = []
    dataDict = {}
    
    for row in csvreader:
        count += 1
        #total number of months in dataset
        totalMonths = count

        #net total amount of profit/losses over entire period
        totalPL += int(row[1])
        
        
        #average of the change in daily profit/losses
        change = int(row[1])-prev
        prev = int(row[1])

        changeList.append(change)
        dataDict[row[0]] = changeList[dictCount]
        averageChange = sum(changeList) / len(changeList)
        dictCount += 1

    maxChange = max(changeList)    
    
    minChange = min(changeList)

    maxKey = max(dataDict, key=dataDict.get)
    minKey = min(dataDict, key=dataDict.get)
    averageChange = "{:.2f}".format(averageChange)
    totalPL = totalPL + int(firstRow[1])

    print("Financial Analysis")
    print("--------------------------")
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${totalPL}')
    print(f'Average Change: ${averageChange}')
    print(f'Greatest Increase in Profits: {maxKey} (${maxChange})')
    print(f'Greatest Decrease in Profits: {minKey} (${minChange})')

    analysisOutput = open("C:\\Users\\Gamer\\OneDrive\\Desktop\\upenn\\homework\\python-challenge\\PyBank\\Analysis\\analysisOutput.txt","w")
    analysisOutput.write("Financial Analysis \n")
    analysisOutput.write("----------------------\n")
    analysisOutput.write(f'Total Months: {totalMonths}\n')
    analysisOutput.write(f'Total: ${totalPL}\n')
    analysisOutput.write(f'Average Change: ${averageChange}\n')
    analysisOutput.write(f'Greatest Increase in Profits:{maxKey} (${maxChange})\n')
    analysisOutput.write(f'Greatest Decrease in Profits: {minKey} (${minChange})\n')
    analysisOutput.close()
       
            
        
    