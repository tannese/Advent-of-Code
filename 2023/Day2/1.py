#!/usr/local/bin/python3

file = 'input.txt'
#file = 'input.test.txt'

def part1(inFile):
    validGames = []
    maxCubes = {'red':12, 'green':13, 'blue':14}
    for line in inFile:
        blocks = {'red':0, 'blue':0, 'green':0}
        gameset = line.split(':')
        game = int(gameset[0].split()[1])
        sets = gameset[1].split(';')
        for set in sets:
            elements = set.split(',')
            for element in elements:
                color = element.split()[1]
                quantity = int(element.split()[0])
                if blocks[color] < quantity:
                    blocks[color] = quantity
        validGame = True
        for color in blocks:
            if blocks[color] > maxCubes[color]:
                validGame = False
        if validGame:
            validGames.append(game)
    return sum(validGames)

def part2(inFile):
    totalPower = 0
    for line in inFile:
        blocks = {'red':0, 'blue':0, 'green':0}
        gameset = line.split(':')
        sets = gameset[1].split(';')
        for set in sets:
            elements = set.split(',')
            for element in elements:
                color = element.split()[1]
                quantity = int(element.split()[0])
                if blocks[color] < quantity:
                    blocks[color] = quantity
        gamePower = blocks['red'] * blocks['green'] * blocks['blue']
        totalPower += gamePower
    return totalPower

if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")

p1 = part1(output)
p2 = part2(output)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')