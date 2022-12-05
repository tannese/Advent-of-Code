#!/usr/bin/python3

file = "input.test.txt"

with open(file, 'r') as f:
        crates, movements = f.read().split("\n\n")

crates = crates.split("\n")
stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 = ([] for i in range(10))
stacks= [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

# Crate contents are at these positions in the file (0 indexed of course) 1 5 9 13 17 21 25 29 33 37
i = len(crates) - 2 # We don't want the sack numbers from the file
while (i >= 0):
    if ord(crates[i][1]) != 32 :
        stack1.append(crates[i][1])
    if ord(crates[i][5]) !=32:
        stack2.append(crates[i][5])
    if ord(crates[i][9]) !=32:
        stack3.append(crates[i][9])
    i -= 1
"""     if ord(crates[i][13]) !=32:
        stack4.append(crates[i][13])
    if ord(crates[i][17]) !=32:
        stack5.append(crates[i][17])
    if ord(crates[i][21]) !=32:
        stack6.append(crates[i][21])
    if ord(crates[i][25]) !=32:
        stack7.append(crates[i][25])
    if ord(crates[i][29]) !=32:
        stack8.append(crates[i][29])
    if ord(crates[i][33]) !=32:
        stack9.append(crates[i][33])
    i -= 1 """


movements = movements.split("\n")
for movement in movements:
    movement = movement.split()
    qty = int(movement[1])
    fromStack = int(movement[3])
    toStack = int(movement[5])
    while (qty > 0):
        stacks[toStack].append(stacks[fromStack].pop())
        qty -= 1

stackTops = ""
z = 1
#while (z < len(stacks)):
while (z < 4):
    zLen = len(stacks[z]) -1
    stackTops += stacks[z][zLen]
    z += 1

print(f'Part 1: {stackTops}')



    