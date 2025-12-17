
idList = []
invalidIDList = []

def checkIDPattern(id):
    
    idStr = str(id)
    
    # take substring from length of idStr // 2 to 1
    # if substring * any number == string -> return True
    # else return False

    i = len(idStr) // 2
    while(i > 0):
        substring = idStr[:i]
        for j in range(1, len(idStr) // i + 1):
            if substring * j == idStr:
                return True
        i -= 1
    
    return False


with open("input.txt", "r") as file:
    idPairs = file.read().split(",")

for pair in idPairs:
    idList.append(pair.split("-"))


for idPair in idList:
    for id in range(int(idPair[0]), int(idPair[1]) + 1):
        if checkIDPattern(id):
            invalidIDList.append(id)

print(invalidIDList)

print("Sum of invalid IDs: ", sum(invalidIDList))