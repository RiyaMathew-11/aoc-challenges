import math

def processCephalopodMath(lines: list[str]):

    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    matrices = {}
    matrix_count = 0
    start_col = 0
    col = 0

    while col < max_len:
        # Check if current column is all spaces (separator)
        is_separator = all(lines[row][col] == ' ' for row in range(5))

        if is_separator:
            # Save current matrix if there is one
            if col > start_col:
                matrix = [list(lines[row][start_col:col]) for row in range(4)]
                matrices[matrix_count] = matrix
                matrix_count += 1

            # Skip all consecutive space columns
            while col < max_len and all(lines[row][col] == ' ' for row in range(5)):
                col += 1
            start_col = col
        else:
            col += 1

    if start_col < max_len:
        matrix = [list(lines[row][start_col:max_len]) for row in range(4)]
        matrices[matrix_count] = matrix

    return matrices


def applyOperation(symbol: str, matrix: list[list[str]]):

    # Transpose the matrix
    transposed = list(zip(*matrix))
    print(transposed)

    if symbol == "+":
        return sum(int(''.join(row)) for row in transposed)
    elif symbol == "*":
        return math.prod(int(''.join(row)) for row in transposed)
    

with open("input.txt", 'r') as f:
    lines = [line.rstrip('\n') for line in f]  
    matrices = processCephalopodMath(lines)
    symbols = [symbol for symbol in lines[4] if symbol != " "]


grandTotal = 0

for i in range(len(symbols)):
    grandTotal += applyOperation(symbols[i], matrices[i])


        
print(grandTotal)