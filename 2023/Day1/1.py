#!/usr/local/bin/python

file = 'input.txt'
#file = 'input.test.txt'

if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")

    calibration = 0
    for calLine in output:
        calibrationTemp = ''
        for digit in calLine:
            if digit.isnumeric():
                calibrationTemp = calibrationTemp + digit
        calibrationTemp = calibrationTemp[0] + calibrationTemp[-1]
        calibration += int(calibrationTemp)
    print(calibration)
        