data = open("day18.txt").read().strip()
data = [[i.split(' ')[0], int(i.split(' ')[1]), i.split(' ')[2][1:-1]] for i in data.split('\n')]

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


def draw(dug):  # draw for fun
    pic = []

    for y in range(ymin, ymax + 1):
        row = [i[0] for i in sorted(list(dug)) if i[1] == y]
        # Drawing lava pit
        rows = ''
        for i in range(xmin, xmax + 1):
            if i == 0 and y == 0:
                rows += '0'
            elif i in row:
                rows += '#'
            else:
                rows += '.'
        pic.append(rows)
        print(rows)


# draw(dug)

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

# res = inside + outline
print('Part 1: ', len(inside) + len(dug))
