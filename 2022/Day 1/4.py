#!/usr/bin/python3

# Advent of Code Puzzle 1 https://adventofcode.com/2022/day/1
# Answer from geekagog 
# https://www.reddit.com/r/adventofcode/comments/z9ezjb/comment/iygvd37/?utm_source=share&utm_medium=web2x&context=3

with open('input.txt', 'r') as f:
    data = f.read().strip().split("\n\n")
f.close()

elf_totals = []  
for elf_calories in data:  
    elf_totals.append(sum(int(number) for number in elf_calories.split("\n")))  

elf_totals.sort()  

print(f'Part 1: {elf_totals[-1]}')    
print(f'Part 2: {sum(elf_totals[-3:])}')