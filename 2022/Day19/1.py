#!/usr/bin/python3

#file = 'input.txt'
file = 'input.test.txt'


def parseBlueprints(blueprints):
    requirements = []
    for blueprint in blueprints:
        blueprint = blueprint.split()
        bp = blueprint[1].strip(":")
        ore = blueprint[6]
        clay = blueprint[12]
        obsidian = [blueprint[18], blueprint[21]]
        robot = [blueprint[27], blueprint[30]]
        requirements.append([bp, ore, clay, obsidian, robot])
    return(requirements)

def calcScores(robotreqs):
    bpscores = [""]
    for robotreq in robotreqs:
        timer = 1
        ore, clay, obsidian, robot = 0, 0, 0, 0
        
        while (timer < 25):
            timer += 1
        bpscores.append(robotreqs[0])
        timer = 1

    return(bpscores)



if __name__ == '__main__':
    with open(file, 'r') as f:
        output = f.read().strip().split("\n")
    print("Blueprint, OreRobot, ClayRobot, ObsidianRobot[Ore,Clay], GeodeRobot[Ore,Obsidian]")
    robotRequirements = parseBlueprints(output)
    scores = calcScores(robotRequirements)
    print(scores)
