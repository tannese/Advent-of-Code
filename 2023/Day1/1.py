#!/usr/local/bin/python

file = 'input.txt'
#file = 'input1.test.txt'
#file = 'input2.test.txt'


def part1(inFile):
    calibration = 0
    for calLine in inFile:
        calibrationTemp = ''
        for digit in calLine:
            if digit.isnumeric():
                calibrationTemp = calibrationTemp + digit
        calibrationTemp = calibrationTemp[0] + calibrationTemp[-1]
        calibration += int(calibrationTemp)
    return(calibration)

def part2(inFile):
    calibration = 0

    for calLine in inFile:
        digits = []
        for i,c in enumerate(calLine):
            if c.isdigit():
                    digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if calLine[i:].startswith(val):
                            digits.append(str(d+1))
        calibration += int(digits[0]+digits[-1])
    return(calibration)




if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")

    p1 = part1(output)
    p2 = part2(output)
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')


        