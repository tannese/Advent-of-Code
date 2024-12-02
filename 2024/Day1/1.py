#!/usr/local/bin/python3

file = 'input.txt'
#file = 'input.test.txt'

def createLists(file):
    '''Creates 2 lists based on file input'''
    list1 = []
    list2 = []
    for pair in file:
        a = pair.split()
        list1.append(int(a[0]))
        list2.append(int(a[1]))
    return sorted(list1), sorted(list2)

def farApart(pairsa, pairsb):
    '''Creates a list of how far apart the items in the pairs are '''
    newList = []
    for i in range(0, len(pairsa)):
        newList.append(abs(pairsa.pop(0) - pairsb.pop(0)))
    return sum(newList)

if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split('\n')
    lista, listb = createLists(output)

    p1 = farApart(lista, listb)
    print(f'Part 1: {p1}')
    