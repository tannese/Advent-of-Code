#!/usr/bin/python3

from pathlib import PurePosixPath as Path

file = 'input.txt'
#file = 'input.test.txt'

part1Max = 100000
systemStorageMax = 70000000
upgradeMinimum = 30000000

def createTree(dirInfo):
    '''
    
    '''
    dirsList = {'/':0}
    filesList = {}
    curDir = Path('/')
    for entry in dirInfo:
        entry = entry.split()
        if (entry[0] == "$"):  # Process a command
            if (entry[1] == "cd"):
                if (entry[2] == ".."):
                    curDir = curDir.parent
                else:
                    curDir/=entry[2]
        else:
            if (entry[0] == "dir"):
                dirsList[str(curDir/entry[1])]=0
            else:
                filesList[str(curDir/entry[1])] = int(entry[0])
    return(dirsList, filesList)

def sumFolders(dirs, entries):
    for d in dirs:
        for e in entries:
            if e.startswith(d):
                dirs[d] += entries[e]
    return(dirs)
    
def findSmallFolders(folders, max):
    itemSums = 0
    for value in folders.values():
        if (value <= max):
            itemSums += value
    return(itemSums)

def findFolderToDelete(folders, systemMax, upgradeMin):
    curUsage = folders["/"]
    folderSizetoDelete = curUsage
    maxSpace = systemMax - upgradeMin
    for value in folders.values():
        if (curUsage - value <= maxSpace) and (value < folderSizetoDelete):
            folderSizetoDelete = value
    return(folderSizetoDelete)


if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")
    folders, files =createTree(output)
    sumFolders(folders, files)
    print(f'Part1: {findSmallFolders(folders, part1Max)}')
    print(f'Part2: {findFolderToDelete(folders, systemStorageMax, upgradeMinimum)}')
