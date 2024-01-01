data = open("day18.txt").read().strip()
data = [[i.split(' ')[0], int(i.split(' ')[1]), i.split(' ')[2][2:-1]] for i in data.split('\n')]

# Part 1
pos = [0, 0]
dug = set()
digdir = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
for direction, length, color in data:
    for _ in range(length):
        pos = (pos[0] + digdir[direction][0], pos[1] + digdir[direction][1])
        dug.add(pos)

xmin, xmax = min([i[0] for i in sorted(list(dug))]), max([i[0] for i in sorted(list(dug))])
ymin, ymax = min([i[1] for i in sorted(list(dug))]), max([i[1] for i in sorted(list(dug))])

# Flood fill
start = (1, 1)
q = [start]
inside = set()
while q:
    x, y = q.pop()
    inside.add((x, y))
    for new in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)]:
        if new not in dug and new not in inside and new[0] in range(xmin, xmax + 1) and new[1] in range(ymin, ymax + 1):
            q.append(new)

print('Part 1: ', len(inside) + len(dug))

# Part 2
dd = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
p2dat = [[dd[int(i[2][5])], int(i[2][:5], 16)] for i in data]

# Get vertices
pos = [0, 0]
vertices = [pos]
for direction, distance in p2dat:
    newpos = [vertices[-1][0] + distance * digdir[direction][0], vertices[-1][1] + distance * digdir[direction][1]]
    vertices.append(newpos)

# Shoelace - https://en.wikipedia.org/wiki/Shoelace_formula
area = 0
for [x1, y1], [x2, y2], [x3, y3] in zip(vertices, vertices[1:], vertices[2:]):
    area += y2*(x1-x3)
area = area*0.5

# Picks Theorem - https://en.wikipedia.org/wiki/Pick%27s_theorem
exterior = sum([i[1] for i in p2dat])
interior = area - (exterior//2) + 1
res = int(interior + exterior)

print('Part 2: ', res)
