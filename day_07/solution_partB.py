from collections import defaultdict

with open("input.txt", "r") as file:
    grid = [line.rstrip('\n') for line in file]

start_col = grid[0].index('S')
cols = len(grid[0])

beam_counts = defaultdict(int)
beam_counts[start_col] = 1

# Only process rows with splitters (every other row starting from row 2)
for row in range(2, len(grid), 2):
    new_beam_counts = defaultdict(int)
    for col, count in beam_counts.items():
        if col < 0 or col >= cols:
            continue
        cell = grid[row][col]
        if cell == '^':
            new_beam_counts[col - 1] += count
            new_beam_counts[col + 1] += count
        else:
            new_beam_counts[col] += count
    beam_counts = new_beam_counts

print(sum(beam_counts.values()))
