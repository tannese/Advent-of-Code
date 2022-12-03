#!/usr/bin/python3

file = 'input.txt'

characters = {
    "a": 1, "A": 27,
    "b": 2, "B": 28,
    "c": 3, "C": 29,
    "d": 4, "D": 30,
    "e": 5, "E": 31,
    "f": 6, "F": 32,
    "g": 7, "G": 33,
    "h": 8, "H": 34,
    "i": 9, "I": 35,
    "j": 10, "J": 36,
    "k": 11, "K": 37,
    "l": 12, "L": 38,
    "m": 13, "M": 39,
    "n": 14, "N": 40,
    "o": 15, "O": 41,
    "p": 16, "P": 42,
    "q": 17, "Q": 43,
    "r": 18, "R": 44,
    "s": 19, "S": 45,
    "t": 20, "T": 46,
    "u": 21, "U": 47,
    "v": 22, "V": 48,
    "w": 23, "W": 49,
    "x": 24, "X": 50,
    "y": 25, "Y": 51,
    "z": 26, "Z": 52
}

with open(file, 'r') as f:
    data = f.read().strip().split("\n")
f.close()

wrongSum = 0
groupsSum = 0

for stuff in data:
    stuff1 = []
    stuff2 = []
    stuff1[:0] = stuff[0:len(stuff)//2]
    stuff2[:0] = stuff[len(stuff)//2:]
    for item in stuff2:
        if item in stuff1:
            wrongSum += characters[item]
            break

def divide_stuff(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

sackGroups = list(divide_stuff(data, 3))

for sacks in sackGroups:
    sack1 = []
    sack2 = []
    sack3 = []
    sack1[:0] = sacks[0]
    sack2[:0] = sacks[1]
    sack3[:0] = sacks[2]
    sack1set = set(sack1)
    sack2set = set(sack2)
    sack3set = set(sack3)
    groupsSum += characters[sack3set.intersection(sack1set, sack2set).pop()]




print(f'Total is: {wrongSum}')
print(f'Total of sack groups is: {groupsSum}')