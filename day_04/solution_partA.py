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

paperRollMatrix = []

with open('input.txt', 'r') as file:
    for line in file:
        paperRollMatrix.append(list(line.strip()))
    

for i in range(len(paperRollMatrix)):
    for j in range(len(paperRollMatrix[0])):
        if paperRollMatrix[i][j] == '@' and check_8_directions(paperRollMatrix,i, j):
            countOfForklifts += 1
            

print(countOfForklifts)