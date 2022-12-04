#!/usr/bin/python3

file = 'input.test.txt'

dupeCount = 0
overlappingPairs = 0

with open(file, 'r') as f:
    data = f.read().strip().split("\n")

for pairs in data:
    pair = pairs.split(",")
    range1 = pair[0].split("-")
    range2 = pair[1].split("-")
    print(range1, range2)
    sectors1 = set(range(int(range1[0]),int(range1[1])+1))
    sectors2 = set(range(int(range2[0]),int(range2[1])+1))
    print(sectors1, sectors2)
    if (sectors1.issubset(sectors2)) or (sectors2.issubset(sectors1)):
        dupeCount += 1
    if sectors1.intersection(sectors2):
        overlappingPairs += 1

print(f'Number of sectors for part 1: {dupeCount}')
print(f'Number for part 2: {overlappingPairs}')