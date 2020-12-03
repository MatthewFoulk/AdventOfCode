
INPUT_FILE_NAME = '2020\Puzzle1\input.txt'

def readInputIntoList():
    """
    Reads the input into a list, where each list entry is
    a number from a new line.
    Returns the list of integers
    """
    with open(INPUT_FILE_NAME, 'r') as f:
        # Add each line (a number) to the list and remove the newline character
        inputList = [int(line.strip()) for line in f]
    return inputList

def firstPart():

    expenseReport = readInputIntoList()

    count = len(expenseReport) # number of nums in expense report

    # Compare each number to all the ones following it
    for index1 in range(0, count):
        for index2 in range(index1 + 1, count):
            num1 = expenseReport[index1]
            num2 = expenseReport[index2]
            # Check if the sum the two numbers is 2020
            if num1 + num2 == 2020:
                # Print the product of the two numbers
                return num1 * num2

def secondPart():
    
    expenseReport = readInputIntoList()

    count = len(expenseReport) # Num of nums in expense report

    for index1 in range(0, count):
        for index2 in range(index1 + 1, count):
            for index3 in range(index2 + 1, count):
                num1 = expenseReport[index1]
                num2 = expenseReport[index2]
                num3 = expenseReport[index3]
                # Check if the sum is 2020
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

def main():
    firstAnswer = firstPart()
    print(f"First Answer: {firstAnswer}")

    secondAnswer = secondPart()
    print(f"Second Answer: {secondAnswer}")

if __name__ == "__main__":
    main()