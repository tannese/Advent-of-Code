#!/usr/bin/python3

# Advent of Code Puzzle 1 https://adventofcode.com/2022/day/1
# Tony Annese
# tannese@gmail.com

myfile = 'input.txt'
highelfCals = 0
individualCals = []
highThreeCals = 0
 
with open(myfile) as input:
    cals = 0
    for line in input:
        if line.strip():  # If line is not empty
            cals += int(line.strip())
        else:
            if (cals > highelfCals):
                highelfCals = cals
            individualCals.append(cals)
            cals = 0
    individualCals.append(cals)
    
individualCals.sort(reverse=True)
for ele in range(0,3):
    highThreeCals += individualCals[ele]

print(f'The Elf carrying the most calories is carrying {highelfCals} calories')
print(f'The top 3 elfs are carrying a total of {highThreeCals} calories')



