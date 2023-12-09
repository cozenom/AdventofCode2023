import re

data = open("day8.txt").read().strip()
data = data.split('\n\n')
instructions = data[0]
data = sorted([re.findall('\w\w\w', i) for i in data[1].split('\n')])
# format FGF = (HTC, DTX)

datadict = {i[0]: [i[1], i[2]] for i in data}
# Part 1
steps = 0
current = 'AAA'

while current != 'ZZZ':
    currentLR = datadict[current]
    instr = instructions[steps % len(instructions)]
    if instr == 'L':
        current = currentLR[0]
    else:
        current = currentLR[1]
    steps += 1

print('Part 1: ', steps)

# Part 2
# Simultaneously start on every node that ends with A.
# How many steps does it take before you're only on nodes that end with Z?

starts = [i[0] for i in data if i[0][2] == 'A']
steps = 0
found = False

# Find cycles - answer is LCM
starts = [i[0] for i in data if i[0][2] == 'A']
cycles = []
for start in starts:
    current = start
    visited = []
    steps = 0
    zpos = -1
    cycle = False
    while not cycle:
        visited.append(current)
        instr = instructions[steps % len(instructions)]
        if instr == 'L':current = datadict[current][0]
        else: current = datadict[current][1]
        steps += 1
        if current[-1]=='Z':
            zpos = steps
        if current == datadict[start][0] and zpos!=-1:
            cycle = True
    cycles.append([steps, zpos, visited.index(current)])

import math # lazy

print('Part 2: ',math.lcm(*[i[1] for i in cycles]))
