# Part 1

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

# print(inputDict)
countOfZeroes = 0

for value in inputDict.values():
    if value["direction"] == "L":
        currentPos = (currentPos - value["size"]) % 100
        print(f"X = {value}, currentPos = {currentPos}")
        
    elif value["direction"] == "R":
        currentPos = (currentPos + value["size"]) % 100
        print(f"X = {value}, currentPos = {currentPos}")
    
    if currentPos == 0:
        countOfZeroes += 1

    

print(countOfZeroes)

## Ans = 984