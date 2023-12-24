data = open("day16.txt").read().strip()
data = data.split()
[print(i, j) for i, j in enumerate(data)]

# Part 1
reflections = {
    'E': {'/': 'N',
          '\\': 'S',
          '|': 'NS'},
    'S': {'/': 'W',
          '\\': 'E',
          '-': 'EW'},
    'W': {'/': 'S',
          '\\': 'N',
          '|': 'NS'},
    'N': {'/': 'E',
          '\\': 'W',
          '-': 'EW'}
}
dirdict = {'E': (1, 0), 'S': (0, 1), 'N': (0, -1), 'W': (-1, 0)}


# start 0,0
def getEnergized(queue=[(0, 0, 'E')]):
    xrange, yrange = range(0, len(data[0])), range(0, len(data))
    energized, visited = set(), set()
    while queue:
        curr = queue.pop(-1)
        energized.add((curr[0], curr[1]))
        currsym, direction = data[curr[1]][curr[0]], curr[2]
        visited.add(curr)
        if currsym in reflections[direction].keys():
            for i in reflections[direction][currsym]:
                nextpos = tuple([sum(x) for x in zip((curr[0], curr[1]), dirdict[i])] + [i])
                if nextpos[0] in xrange and nextpos[1] in yrange and nextpos not in visited: queue.append(nextpos)
        else:
            nextpos = tuple([sum(x) for x in zip((curr[0], curr[1]), dirdict[curr[2]])] + [curr[2]])
            if nextpos[0] in xrange and nextpos[1] in yrange and nextpos not in visited: queue.append(nextpos)
    return len(energized)


print('Part 1: ', getEnergized())

# Part 2
# Lazy brute force

maxEnergy = 0
for i in range(0, len(data)):
    maxEnergy = max(maxEnergy, getEnergized([(i, 0, 'S')]))
    maxEnergy = max(maxEnergy, getEnergized([(len(data) - 1, i, 'W')]))
    maxEnergy = max(maxEnergy, getEnergized([(0, i, 'E')]))
    maxEnergy = max(maxEnergy, getEnergized([(i, len(data) - 1, 'N')]))

print('Part 2: ', maxEnergy)
