#!/usr/bin/python3

file = 'input.txt'
#file = 'input.test.txt'


if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")

    input = []
    x = 0
    while (x < len(output)):
        input.append(list(output[x]))
        x += 1
    
    x = 0
    for line in input:
        while (x < len(line)):
            line[x] = int(line[x])
            x += 1
        x = 0



    rows = len(input)
    cols = len(input[0])
    visible = [[0 for _ in range(cols)] for _ in range(rows)]

    lheight = rheight = 0
    uheight = [0 for _ in range(cols)]
    bheight = [0 for _ in range(cols)]

    curRow = 0
    i = 0
    while (i < cols): # Initialize First Row
        visible[curRow][i] = 1
        i += 1
    curRow += 1
    while (curRow < rows -1):
        lheight = rheight = 0
        i = 0
        while (i < cols): # Left Check
            if (i == 0):
                visible[curRow][i] = 1
                lheight = input[curRow][i]
            else:
                if input[curRow][i] > lheight:
                    visible[curRow][i] = 1
                    lheight = input[curRow][i]
            i += 1
        i -= 1
        while (i > 0): # Right Check
            if (i == cols -1): 
                visible[curRow][i] = 1
                rheight = input[curRow][i]
            else:
                if (input[curRow][i] > rheight):
                    visible[curRow][i] = 1
                    rheight = input[curRow][i]
            i -= 1       

        curRow +=1
    i = 0
    while (i < cols): # Initialize last row
        visible[curRow][i] = 1
        i += 1

    curRow = 0
    i = 0
    while (i < cols): # Initialize uheight
        uheight[i] = input[curRow][i]
        i += 1
    curRow += 1

    while (curRow < rows -1):
        i = 1
        while (i < cols): # Upper to Lower Check
            if (input[curRow][i] > uheight[i]):
                visible[curRow][i] = 1
                uheight[i] = input[curRow][i]
            i += 1
        curRow += 1
    i = 0
    while (i < cols): # Initialize bheight
        bheight[i] = input[curRow][i]
        i +=1
    curRow -= 1
    while (curRow > 0):
        i = 1
        while (i > cols): # Bottom to Top Check
            if (input[curRow][i] > bheight[i]):
                visible[curRow][i] = 1
                bheight[i] = input[curRow][i]
            i += 1
        curRow -= 1


    
    visibleSum = 0
    for visRow in visible:
        visibleSum += sum(visRow)
    
    print(f'Part 1: {visibleSum}')
