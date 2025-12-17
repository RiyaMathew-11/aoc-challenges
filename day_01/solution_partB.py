currentPos = 50
inputDict = {}

puzzleInput = open("input.txt", "r").read().split("\n")
x = 0

for line in puzzleInput:
    if line == "":
        break
    # print(line, f"x: {x}")
    inputDict[x] = {"direction": line[0], "size": int(line[1:])}
    x += 1

print(inputDict)
countOfZeroes = 0

def moveLeft(currentPos):
    return (currentPos - 1) % 100


def moveRight(currentPos):
    return (currentPos + 1) % 100

for value in inputDict.values():
    if value["direction"] == "L":
        for i in range(value["size"]):
            currentPos = moveLeft(currentPos)
            if currentPos == 0:
                countOfZeroes += 1
    elif value["direction"] == "R":
        for i in range(value["size"]):
            currentPos = moveRight(currentPos)
            if currentPos == 0:
                countOfZeroes += 1

print(countOfZeroes)