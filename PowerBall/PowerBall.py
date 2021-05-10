numbers = open('PowerBallNumbers.txt','r').read().split()
powerBallNumbers = open('PowerBallPowerBallnumbers.txt', 'r').read().split()
totalNumbers = len(numbers)
count = 0
min = 0
max = 0

while count < 69:
    occurences = 0
    count = count + 1

    for i in range(0, totalNumbers):

        if int(numbers[i]) == count:
            occurences = occurences + 1   
    
    print("Probability of a " + str(count) + " is " + str(occurences) + " out of " + str(totalNumbers))    

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Powerball Numbers -----------------------------------------------------------------------------------------------------------------------------------------")
totalNumbers = len(powerBallNumbers)
count = 0
min = 0
max = 0

while count < 26:
    occurences = 0
    count = count + 1

    for i in range (0, totalNumbers):

        if int(powerBallNumbers[i]) == count:
            occurences = occurences + 1

    print("Probability of a " + str(count) + " is " + str(occurences) + " out of " + str(totalNumbers))    