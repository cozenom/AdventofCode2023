data = open("day10.txt").read().strip()
data = data.split('\n')

# Part 1
"""
| is a vertical pipe connecting north and south. |
- is a horizontal pipe connecting east and west. ─
L is a 90-degree bend connecting north and east. ┕
J is a 90-degree bend connecting north and west. ┘
7 is a 90-degree bend connecting south and west. ┑  
F is a 90-degree bend connecting south and east. ┌
. is ground; there is no pipe in this tile.
S is the starting position of the animal
"""
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'S':
            Spos = [y, x]
            break
y, x = Spos[0], Spos[1]
# All coordinates are [Y,X]
dirs = {'N': ['|', 'F', '7'], 'S': ['|', 'L', 'J'], 'E': ['-', '7', 'J'], 'W': ['-', 'L', 'F']}
n = [[y - 1, x], [y + 1, x], [y, x + 1], [y, x - 1]]
startend = []

for i in range(4):
    if data[n[i][0]][n[i][1]] in dirs[list(dirs.keys())[i]]: startend.append(n[i])
start, end = startend[0], startend[1]
maxx, maxy = len(data[0]), len(data)


def findnext(current, last):
    y, x = current[0], current[1]
    currsym = data[y][x]
    # print(currsym, data[last[0]][last[1]])
    if currsym == '|':
        nextpos = [[current[0] - 1, current[1]], [current[0] + 1, current[1]]]
    elif currsym == '-':
        nextpos = [[current[0], current[1] + 1], [current[0], current[1] - 1]]
    elif currsym == 'L':
        nextpos = [[current[0] - 1, current[1]], [current[0], current[1] + 1]]
    elif currsym == 'J':
        nextpos = [[current[0] - 1, current[1]], [current[0], current[1] - 1]]
    elif currsym == '7':
        nextpos = [[current[0] + 1, current[1]], [current[0], current[1] - 1]]
    elif currsym == 'F':
        nextpos = [[current[0] + 1, current[1]], [current[0], current[1] + 1]]
    for i in nextpos:
        if i != last: return i


visited = [Spos, start]

while end not in visited:
    visited.append(findnext(visited[-1], visited[-2]))
print('Part 1: ', len(visited) // 2)

# Part 2
# How many tiles are enclosed by the loop?

data[Spos[0]] = data[Spos[0]].replace('S', '|')
inside = ['|', 'J', 'L']

res = 0
for y, row in enumerate(data):
    isinside = False
    for x, val in enumerate(row):
        if [y, x] not in visited and not isinside: continue
        if [y, x] in visited and str(val) in inside and not isinside:
            isinside = True
        elif [y, x] in visited and str(val) in inside and isinside:
            isinside = False
        if [y, x] not in visited and isinside:
            res += 1

print('Part 2: ', res)
