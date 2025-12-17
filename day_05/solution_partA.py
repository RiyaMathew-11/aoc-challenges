available_ids = []

with open("availableIDs.txt", "r") as f:
    for line in f:
        available_ids.append(int(line.strip()))


# fresh id range

fresh_ranges = []

with open("freshIDRange.txt", "r") as f:
    for line in f:
        range_str = line.strip()
        if "-" in range_str:
            start, end = map(int, range_str.split("-"))
            fresh_ranges.append((start, end))

fresh_ranges.sort()
available_ids.sort()

countOfFreshIngredients = 0

# for each available ID, check if it's covered by any fresh range
for available_id in available_ids:
    for start, end in fresh_ranges:
        if start <= available_id <= end:
            countOfFreshIngredients += 1
            break

print(f"Count of fresh ingredients: {countOfFreshIngredients}")
        
