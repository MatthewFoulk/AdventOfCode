
INPUT_FILE = '2020\Puzzle3\input.txt'

def readInput(inputFile):
    with open(inputFile, 'r') as f:
        data = [list(line.strip()) for line in f]
    
    return data

def firstPart(landscape, slope):

    # Slope
    changeInX = slope[0]
    changeInY = slope[1]

    # Current position
    x = 0
    y = 0

    # Max position in x and y direction
    maxX = len(landscape[0]) - 1
    maxY = len(landscape) - 1

    # Num of trees encountered in toboggan run
    treeCount = 0

    while (y <= maxY):

        # Tree encountered
        if (landscape[y][x] == '#'):
            treeCount += 1

        x += changeInX
        y += changeInY

        # Wrap backaround into the repeating environment
        if (x > maxX):
            x -= (maxX + 1)

    return treeCount

def secondPart(landscape, slopes):

    treesMultiplied = 1

    for slope in slopes:
        treesMultiplied *= firstPart(landscape, slope)
    
    return treesMultiplied


def main():

    landscape = readInput(INPUT_FILE)

    firstSlope = (3, 1)
    firstAnswer = firstPart(landscape, firstSlope)
    print(f"First Answer: {firstAnswer}")

    secondSlopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    secondAnswer = secondPart(landscape, secondSlopes)
    print(f"Second Answer: {secondAnswer}")


if __name__ == "__main__":
    main()
