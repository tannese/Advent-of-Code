#!/usr/bin/python3

# Advent of Code Puzzle 1 https://adventofcode.com/2022/day/1
# Tony Annese
# tannese@gmail.com

myfile = 'input.txt'
highelf = 0
highelfCals = 0
individualCals = []
highThreeCals = 0
elf = 0
 
with open(myfile) as input:
    elf = 1
    cals = 0
    for line in input:
        if line.strip():  # If line is not empty
            cals += int(line.strip())
        else:
            #print(f'Elf {elf} is carying {cals} calories')
            if (cals > highelfCals):
                highelfCals = cals
                highelf = elf
            individualCals.append(cals)
            elf += 1
            cals = 0
    #print(f'Elf {elf} is carying {cals} calories')
    individualCals.append(cals)
    
print(f'High Elf is Elf {highelf} with {highelfCals} calories')

individualCals.sort(reverse=True)
for ele in range(0,3):
    highThreeCals += individualCals[ele]
print(f'The top 3 elfs are carrying a total of {highThreeCals} calories')



