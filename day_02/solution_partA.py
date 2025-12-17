idList = []
invalidIDList = []

# def checkPalidrome(id):
#     return id == id[::-1]

def checkSubstringPair(id):

    if len(id) % 2 != 0:
        return False
    
    half = len(id) // 2
    first_half = id[:half]
    second_half = id[half:]

    return first_half == second_half

with open("input.txt", "r") as file:
    idPairs = file.read().split(",")

for pair in idPairs:
    idList.append(pair.split("-"))

# print(idList)

for idPair in idList:
    for id in range(int(idPair[0]), int(idPair[1]) + 1):
        if checkSubstringPair(str(id)):
            invalidIDList.append(int(id))

print(invalidIDList)

print("Sum of invalid IDs: ", sum(invalidIDList))

# Answer: 12599655151




        
        


