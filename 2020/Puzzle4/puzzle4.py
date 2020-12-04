
import re

INPUT_FILE_PATH = '2020/Puzzle4/input.txt'

def readInput(inputFile):
    with open(inputFile) as f:
        data = f.read()
    
    return data

def splitOnBlankLine(data):
    return data.split("\n\n")

def isKeyInDict(keyToFind, dictToCheck):
    for key in dictToCheck.keys():
        if key == keyToFind:
            return True
    return False


def convertStringsToDict(data):
    newData = []

    for item in data:
        itemDict = {}
        for keyVal in re.split(' |\n', item):

            # Verify that key value is not 
            if len(keyVal) > 0:
                key, val = keyVal.split(":")
                itemDict[key] = val
        newData.append(itemDict)
    
    return newData

def isFieldValid(field, passport):
    
    if field == "byr":
        byr = passport[field]
        if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
            return False
    
    elif field == "iyr":
        iyr = passport[field]
        if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
            return False
    
    elif field == "eyr":
        eyr = passport[field]
        if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
            return False
    
    elif field == "hgt":
        hgt = passport[field]
        if hgt[-2:] == "in":
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                return False

        elif hgt[-2:] == "cm":
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                return False
        else:
            return False
    
    elif field == "hcl":
        hcl = passport[field]
        if len(hcl) > 7 or re.match('[#][a-f0-9]{6}', hcl) is None:
            return False
    
    elif field == "ecl":
        possibleEcl = ["amb", "blu", "brn", "gry", 
            "grn", "hzl", "oth"]
        ecl = passport[field]

        if ecl not in possibleEcl:
            return False
    
    elif field == "pid":
        pid = passport[field]
        if len(pid) != 9 or not pid.isnumeric():
            return False
    
    return True


def firstPart(data):

    # Everything on passport is required except cid (Country ID)
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    # Number of invalid passports
    invalidPassports = 0

    for passport in data:
        for field in requiredFields:
            if not isKeyInDict(field, passport):
                invalidPassports += 1
                break
    
    totalPassports = len(data)

    return totalPassports - invalidPassports

def secondPart(data):
    # Everything on passport is required except cid (Country ID)
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    # Number of invalid passports
    invalidPassports = 0

    for passport in data:
        for field in requiredFields:
            if not isKeyInDict(field, passport):
                invalidPassports += 1
                break
            elif not isFieldValid(field, passport):
                invalidPassports += 1
                break
    
    totalPassports = len(data)

    return totalPassports - invalidPassports
    

def main():

    data = readInput(INPUT_FILE_PATH)
    data = splitOnBlankLine(data)
    data = convertStringsToDict(data)

    firstAnswer = firstPart(data)
    print(f"First Answer: {firstAnswer}")
    
    secondAnswer = secondPart(data)
    print(f"Second Answer: {secondAnswer}")

if __name__ == "__main__":
    main()
    