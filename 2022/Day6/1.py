#!/usr/bin/pyton3

#file = 'input.test.txt'
file = 'input.txt'

def _findStartOf(signal, msgLen):
    '''
    Creates a message of length msgLen and returns the position of the last character
    in which the message contains all unique items
    '''
    x = 0  # Counter
    tmp = []  # List to hold the working message
    while ( x < len(signal)):  # Work through the input stream
        if (x < (msgLen -1)):  # Pre-fill the working list buffer
            tmp.append(signal[x])
        else:
            tmp.append(signal[x])  # Add the next character to the working list
            if(len(set(tmp)) == len(tmp)):  # Check if the number of items in the working buffer is a set(unique)
                return(x + 1)  # Return the position +1 because of zero index
            else:
                del tmp[0]  # If they aren't unique remove the first item in the list 
        x += 1
    return(-1)  # Return a neg number to indicate an error

with open(file, 'r') as f:
    transmission = f.read().strip().split("\n")

i = 0
while (i < len(transmission)):  # Loop through the input file however many times there are lines
    print(f'Transmission {i+1}:\nPart 1: ', _findStartOf(transmission[i],4))
    print('Part 2: ', _findStartOf(transmission[i],14))
    i += 1