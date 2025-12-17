countOfForklifts = 0

def check_8_directions(matrix, row, col):
    # Check 8 adjacent cells of the element at (row, col)
    # Return true if the element is surrounded by less than 4 "@" else return false

    countOfAts = 0
    # Check all 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            if matrix[new_row][new_col] == '@':
                countOfAts += 1

    return countOfAts < 4

def removeTissueRolls(matrix):
    rollsRemoved = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '@' and check_8_directions(matrix,i, j):
                matrix[i][j] = 'x'
                rollsRemoved += 1

    print("Removed " + str(rollsRemoved) + " tissue rolls")
    # print("Matrix after removal:")
    # for row in matrix:
    #     print(''.join(row))

    return rollsRemoved, matrix

def countCurrentTissueRolls(matrix):
    numberOfTissueRolls = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '@':
                numberOfTissueRolls += 1
    return numberOfTissueRolls

paperRollMatrix = []

with open('input.txt', 'r') as file:
    for line in file:
        paperRollMatrix.append(list(line.strip()))

# count number of tissue rolls

numberOfTissueRolls = countCurrentTissueRolls(paperRollMatrix)
rollsRemoved = 0

i = 0
while numberOfTissueRolls > 0:
    print("Round " + str(i) + ": " + str(numberOfTissueRolls) + " tissue rolls remaining")
    removedRolls, paperRollMatrix = removeTissueRolls(paperRollMatrix)
    if removedRolls == 0:
        break
    rollsRemoved += removedRolls
    numberOfTissueRolls = countCurrentTissueRolls(paperRollMatrix)
    i += 1



            

print(numberOfTissueRolls, rollsRemoved)