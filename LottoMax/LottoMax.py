winningNumbers = open('Numbers.txt','r').read().split()
Data = {}
removeDataSet = 1

def isSmaller(numberOne, numberTwo):
    return numberOne < numberTwo

def printNumbers():
    for index in Data:
        print("[LottoMax] Number | " + str(Data[index]["Number"]) + " Occurences | " + str(Data[index]["Occurrences"]) + " Proportion | " + str(Data[index]["Proportion"]))

for possibleNumber in range(1, 50):
    occurences = 0
    Data[possibleNumber] = {}
    for index in range(0, len(winningNumbers) - (removeDataSet * 7)):
        if int(winningNumbers[index]) == possibleNumber:
            occurences = occurences + 1
    Data[possibleNumber]["Number"] = possibleNumber            
    Data[possibleNumber]["Occurrences"] = occurences
    Data[possibleNumber]["Proportion"] = float(occurences) / len(winningNumbers)
    print("[LottoMax] " + str(possibleNumber) + " | " + str(Data[possibleNumber]["Occurrences"]) + "/" + str(len(winningNumbers)) + " - " + str(Data[possibleNumber]["Proportion"]))

#printNumbers()
for numberIndex in range(0, len(Data)):
    for index in range(1, len(Data)):
        if Data[index]["Proportion"] < Data[index + 1]["Proportion"]:
            oldData = Data[index]
            Data[index] = Data[index + 1]
            Data[index + 1] = oldData

printNumbers()

