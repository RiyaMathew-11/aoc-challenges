maxJoltage = []


def formMaxJoltage(joltage):

    max1 = max(joltage)
    idx1 = joltage.index(max1)
    
    if idx1 == len(joltage) - 1:
        return int(str(max(joltage[:idx1])) + str(max1))
    else:
        return int(str(max1) + str(max(joltage[idx1+1:])))

     

with open("input.txt", "r") as file:
    for line in file:
        joltage = list(line.strip())
        maxJoltage.append(formMaxJoltage(joltage))

print(maxJoltage)
print(sum(maxJoltage))

# Answer: 17493


