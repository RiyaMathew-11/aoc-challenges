import math
from itertools import combinations

with open("input.txt", "r") as file:
    coordinatesOfJunctionBoxes = [line.rstrip('\n') for line in file]

def straightLineDistance(c1, c2):
    x1, y1, z1 = map(int, c1.split(','))
    x2, y2, z2 = map(int, c2.split(','))
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

parent = {}
rank = {}

def findRoot(x):
    """Find the root of x with"""
    if parent[x] != x:
        parent[x] = findRoot(parent[x])
    return parent[x]

def unifyCircuits(x, y):
    """
    Unify two circuits by rank
    Returns True if circuits were merged, False if already same circuit
    """
    rootX = findRoot(x)
    rootY = findRoot(y)
    if rootX == rootY:
        return False  # Already in same circuit

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1
    return True 

for box in coordinatesOfJunctionBoxes:
    parent[box] = box
    rank[box] = 0

# Find distances between each pair of junction boxes
allPairs = []
for box1, box2 in combinations(coordinatesOfJunctionBoxes, 2):
    distance = straightLineDistance(box1, box2)
    allPairs.append((distance, box1, box2))

allPairs.sort(key=lambda x: x[0])

# Keep connecting until all boxes are in one circuit
# exactly (N-1) successful merges to connect N boxes
totalBoxes = len(coordinatesOfJunctionBoxes)
mergeCount = 0
lastBox1 = None
lastBox2 = None

for distance, box1, box2 in allPairs:
    if unifyCircuits(box1, box2):
        mergeCount += 1
        lastBox1 = box1
        lastBox2 = box2

        if mergeCount == totalBoxes - 1:
            break

x1, x2 = int(lastBox1.split(',')[0]), int(lastBox2.split(',')[0])

print(f"Last connection: {lastBox1} and {lastBox2}")
print(f"Answer: {x1 * x2}")