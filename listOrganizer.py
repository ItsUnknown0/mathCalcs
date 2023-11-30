
# Starting Variables

inputData = []
savedDataFile = open("savedData.txt", "a+")

# Functions

def userInput():
    number = input("Input the number: ")

    if number == "stop":
        print("doing the stuff...")
        return "stopped"

    if not number.isnumeric():
        print("The input was not a number. Please try again.")
        return userInput()
    
    inputData.append(int(number))
    return userInput()

print("type 'stop' when you want to stop adding numbers!")

userInput()

# Finishing

inputData.sort()
savedDataFile.write("\n=== New List ===\n\n")

print(inputData)

# funcs

def sortWriteData():
    i = 1

    for num in inputData:
        savedDataFile.write(str(num) + ", ")

        i += 1
        if i > 3:
            i = 1
            savedDataFile.write("\n")

def writeFrequency():
    
    allNums = []
    
    for num in inputData:
            
        if not num in allNums:
            allNums.append(num)

    print(allNums)

    for processed in allNums:
        frequency = str(inputData.count(processed))
        savedDataFile.write(str(processed) + ": " + frequency + "\n")

# yuh

sortWriteData()

savedDataFile.write("\nFrequencies:\n")

writeFrequency()

print("finished writing")

savedDataFile.close()