with open("input.txt", "r") as file:
    grid = [line.rstrip('\n') for line in file]

# Find starting position S
start_col = grid[0].index('S')

rows = len(grid)
cols = len(grid[0])

# Active beams: set of column positions (all beams move together row by row)
beam_cols = {start_col}
split_count = 0

for row in range(1, rows):
    new_beam_cols = set()
    for col in beam_cols:
        if col < 0 or col >= cols:
            continue 
        cell = grid[row][col]
        if cell == '^':
            split_count += 1
            # new beams at immediate left and right - use set to avoid duplicates
            new_beam_cols.add(col - 1)
            new_beam_cols.add(col + 1)
        else:
            new_beam_cols.add(col)
    beam_cols = new_beam_cols

print(split_count)