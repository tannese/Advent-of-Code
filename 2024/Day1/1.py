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
    '''Returns the sum of the difference of all the pairs '''
    newList = []
    for i in range(0, len(pairsa)):
        newList.append(abs(pairsa.pop(0) - pairsb.pop(0)))
    return sum(newList)

def computeSimilarity(pairsa, pairsb):
    '''Returns the similarity score of two lists'''
    newList = []
    for i in range(0, len(pairsa)):
        num = pairsa.pop(0)
        newList.append(pairsb.count(num) * num)
    return sum(newList)


if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split('\n')
    
    lista, listb = createLists(output)
    p1 = farApart(lista, listb)
    lista, listb = createLists(output)
    p2 = computeSimilarity(lista, listb)

    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')
    