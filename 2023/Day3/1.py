#!/usr/local/bin/python3

#file = 'input.txt'
file = 'input.test.txt'

def findSymbols(inFile):
    symbols = []
    for line in output:
        for char in line:
            if not char.isdigit() and char != '.' and char not in symbols:
                symbols.append(char)
    return symbols  

def part1(symbols, inFile):
    for line in inFile:
        for char in line:
            if char.isdigit():
                print(char.index())
    return

if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")


    symbols = findSymbols(output)
    p1 = part1(symbols, output)


