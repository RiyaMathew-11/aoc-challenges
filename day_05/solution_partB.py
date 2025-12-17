fresh_ranges = []

with open("freshIDRange.txt", "r") as f:
    for line in f:
        range_str = line.strip()
        if "-" in range_str:
            start, end = map(int, range_str.split("-"))
            fresh_ranges.append((start, end))

fresh_ranges.sort()
print(f"Sorted fresh ranges: {fresh_ranges}")

# Merge overlapping ranges - reduces time complexity
merged_ranges = []
for start, end in fresh_ranges:
    if not merged_ranges or merged_ranges[-1][1] < start - 1:
        merged_ranges.append((start, end))
    else:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))

print(f"Merged ranges: {merged_ranges}")


totalFreshIngredients = 0
for start, end in merged_ranges:
    totalFreshIngredients += end - start + 1

print(f"Total fresh ingredients: {totalFreshIngredients}")







