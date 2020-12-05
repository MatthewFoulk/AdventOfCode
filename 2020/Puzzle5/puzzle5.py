
import math
from collections import Counter

INPUT_FILE = "2020/Puzzle5/input.txt"

ROW_INDICATORS = 7
COL_INDICATORS = 3

MIN_ROW = 0
MAX_ROW = 127

MIN_COL = 0
MAX_COL = 7

def readInput(inputFile):

    with open(inputFile, 'r') as f:
        data = [line.strip() for line in f]
    
    return data

def firstPart(IDs):
    return max(IDs)

def getIDs(data):

    IDs = []

    for boardingPass in data:

        # Determine seat row
        row = binarySearch(boardingPass[:ROW_INDICATORS], MIN_ROW, MAX_ROW, 'B', 'F')
        # Determine seat column
        col = binarySearch(boardingPass[-COL_INDICATORS:], MIN_COL, MAX_COL, 'R', 'L')

        currID = row * 8 + col
        IDs.append(currID)

    return IDs

def binarySearch(boardingPass, left, right, greaterThanIndicator, LessThanIndicator):

    index = 0

    while (left < right):

        if boardingPass[index] == greaterThanIndicator:
            middle = math.ceil((left + (right - left) / 2))
            left = middle

        elif boardingPass[index] == LessThanIndicator:
            middle = (left + (right - left) // 2) # Floor division
            right = middle
        
        index += 1
    
    if left == right:
        return left
    else:
        raise ValueError("Could not determine number from given")

def secondPart(IDs):
    
    for index in range(min(IDs), max(IDs)):
        if index not in IDs:
            return index

    

def main():

    data = readInput(INPUT_FILE)
    IDs = getIDs(data)

    firstAnswer = firstPart(IDs)
    print(f"First Answer: {firstAnswer}")

    secondAnswer = secondPart(IDs)
    print(f"Second Answer: {secondAnswer}")

if __name__ == "__main__":
    main()