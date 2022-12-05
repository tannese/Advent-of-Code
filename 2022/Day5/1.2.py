#!/usr/bin/python3

file = "input.txt"

with open(file, 'r') as f:
        crates, movements = f.read().split("\n\n") # Split the file into 2 parts, the intial crate stacks and the movements

crates = crates.split("\n")  # Split the lines of crates into individual lines

# Create lists for the stacks
stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9 = ([] for i in range(10))
# Put the stacks into a list. I probably overcomplicated this.
stacks= [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

# Crate stack contents are at these positions in the file (0 indexed of course) 1 5 9 13 17 21 25 29 33
# I'm sure there was a better way of creading in the data and creating the list for each stack
# I have to manually comment out stacks4-9 to run the test input.
# I could probably get the length of the individual line and then loop through them like:
# lineLen = len(crates(0)
# stack = 1
# while x < lineLen:
#     if x == 1:
#         if the character is not a space:
#             append the character to stack numbered stack variable
#         stack += 1
#     elif x % 4 = 1:
#         if the character is not a space:
#             append the character to stack 1
#     stack += 1

i = len(crates) - 2 # We don't want the stack numbers from the file
while (i >= 0):
    if ord(crates[i][1]) != 32 :
        stack1.append(crates[i][1])
    if ord(crates[i][5]) !=32:
        stack2.append(crates[i][5])
    if ord(crates[i][9]) !=32:
        stack3.append(crates[i][9])
    # i -= 1
    if ord(crates[i][13]) !=32:
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
    i -= 1

# Now that we have the lists of crate stack we need to start moving stuff
movements = movements.split("\n") # Split the movements into individual lines
for movement in movements:
    movement = movement.split() # Create a list of the words in the movement order
    qty = int(movement[1])
    fromStack = int(movement[3])
    toStack = int(movement[5])
    while (qty > 0):
        tmp = str(stacks[fromStack].pop()) # Grab the first crate
        stacks[0].insert(0, tmp) # Using stacks[0] as a tmp holder for the crates being moved. Using insert at position 0 to maintain the order of the crates as directed in the instructions
        qty -= 1
        tmp = "" # Reset tmp for the next crate letter
    stacks[toStack].extend(stacks[0]) # Add the crates from stacks[0] to the stack indicated in the movement order
    stacks[0] = [] # Reset stacks[0] for the next movement order

stackTops = "" # Variable to hold our answer
z = 1 # Counter variable for the stacks

#while (z < 4): # Again, needed for test input 
while (z < len(stacks)):  # Loop through the stacks
    zLen = len(stacks[z]) -1 # How big is the stack to know which element to grab. I could have probably sliced the list to get the last element instead
    stackTops += stacks[z][zLen] # Add the last element of the stack list to the variable
    z += 1

print(f'Part 2: {stackTops}')



    