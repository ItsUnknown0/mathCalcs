
inputNum = None

# functions

def checkPrime(x : str):

    thyNum = int(x)

    if thyNum == 1:
        return thyNum
    
    divisibleStuff = []

    for nums in range(2,thyNum): # goes through all numbers between the given
        if thyNum%nums == 0:
            divisibleStuff.append(nums)
            print(nums)
    
    print(divisibleStuff)

    if len(divisibleStuff) > 0: # if there is more than a factor, then it is not a prime
        return None
    else: # it's a prime with like one other factor!
        return "yipee"

def userInput():
    entered = input("Enter your number: ")

    if not entered.isnumeric():
        print("Input was not a number. Try again.")
        return userInput()
    else:
        return entered
    
# yuh

inputNum = userInput()

primeReturn = checkPrime(int(inputNum))

if primeReturn != None:
    print(inputNum + " is a prime number!")
else:
    print(inputNum + " is not a prime number!")