
import pandas as pd
import re

FILE_NAME = 'input.txt'

# https://regex101.com/
# Helpful tool for visualizing regexp


def firstPart():
    validCount = 0 # Number of valid passwords

    # Regexp for parsing lines
    regExp = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>\w):\s(?P<password>\w+)')

    with open(FILE_NAME, 'r') as f:
        for line in f:
            match = regExp.match(line)
            if match:
                minNum = int(match.group('min'))
                maxNum = int(match.group('max'))
                letter = match.group('letter')
                password = match.group('password')

                # Check if password meets criteria
                # The letter must occur a number of times
                # in range [minNum, maxNum]
                letterCount = password.count(letter)
                if letterCount >= minNum and letterCount <= maxNum:
                    validCount += 1
    return validCount

def secondPart():
    validCount = 0 # Number of valid passwords

    # Regexp for parsing lines
    regExp = re.compile(r'(?P<firstPos>\d+)-(?P<secondPos>\d+)\s(?P<letter>\w):\s(?P<password>\w+)')

    with open(FILE_NAME, 'r') as f:
        for line in f:
            match = regExp.match(line)
            if match:
                firstPos = int(match.group('firstPos')) - 1 # -1 for zero indexing
                secondPos = int(match.group('secondPos')) - 1 # -1 for zero indexing
                letter = match.group('letter')
                password = match.group('password')

                

                # Check if password meets criteria
                # Exactly one position must match the letter
                if ((password[firstPos] == letter) != 
                    (password[secondPos] == letter)):
                    validCount += 1
    return validCount

def main():

    firstAnswer = firstPart()
    print(f"First Answer: {firstAnswer}")

    secondAnswer = secondPart()
    print(f"Second Answer: {secondAnswer}")

if __name__ == "__main__":
    main()
