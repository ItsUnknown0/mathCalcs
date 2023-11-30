
import math

def userInput():
    numberOfSides = input("How many sides are in your regular polygon: ")
    sideLength = input("What is one side's length in your polygon: ")

    if not numberOfSides.isnumeric() and not sideLength.isnumeric():
        print("Please enter the numbers again!")
        userInput()
    else:
        calculations(int(numberOfSides), int(sideLength))

def calculations(numberOfSides, sideLength):

    totalPolyAngle = (numberOfSides - 2)*180
    interiorAngle = math.radians((totalPolyAngle/numberOfSides)/2)
    apo = (math.tan(interiorAngle) * (sideLength/2))
    triSA = (apo*sideLength)/2
    polySA = triSA*numberOfSides

    print("The surface area is: " + str(polySA))

userInput()