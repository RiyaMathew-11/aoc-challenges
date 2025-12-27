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
    """find the root of x with path compression"""
    if parent[x] != x:
        parent[x] = findRoot(parent[x])
    return parent[x]

def unifyCircuits(x, y):
    """
    Unify two circuits by rank
    """
    rootX = findRoot(x)
    rootY = findRoot(y)
    if rootX == rootY:
        return  # Already in same circuit

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

for box in coordinatesOfJunctionBoxes:
    parent[box] = box
    rank[box] = 0

# Find distances between each pair of junction boxes
allPairs = []
for box1, box2 in combinations(coordinatesOfJunctionBoxes, 2):
    distance = straightLineDistance(box1, box2)
    allPairs.append((distance, box1, box2))

allPairs.sort(key=lambda x: x[0])

N = 1000
for i in range(N):
    distance, box1, box2 = allPairs[i]
    unifyCircuits(box1, box2)

for box, root in parent.items():
    print(f"{box} -> {root}")

circuitSizes = {}
for box in coordinatesOfJunctionBoxes:
    root = findRoot(box)
    circuitSizes[root] = circuitSizes.get(root, 0) + 1

sizes = sorted(circuitSizes.values(), reverse=True)
print("Product of top 3:", sizes[0] * sizes[1] * sizes[2] if len(sizes) >= 3 else 'Not enough circuits')

