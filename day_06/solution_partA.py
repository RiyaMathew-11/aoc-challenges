# Splitting the input into number and symbols

homework = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        homework.append(line.split(" "))

# Process homework

numeralsDict = {
    0: [],
    1: [],
    2: [],
    3: [],
}

for i in range(len(homework) - 1):
    for j in homework[i]:
        if j.isdigit():
            numeralsDict[i].append(int(j))

symbols = [s for s in homework[4] if s != ""]
print(len(symbols)) 

grandTotal = 0
for i in range(len(symbols)):
    if symbols[i] == "*":
        grandTotal += numeralsDict[0][i] * numeralsDict[1][i] * numeralsDict[2][i] * numeralsDict[3][i]
    elif symbols[i] == "+":
        grandTotal += numeralsDict[0][i] + numeralsDict[1][i] + numeralsDict[2][i] + numeralsDict[3][i]
        

print(grandTotal)