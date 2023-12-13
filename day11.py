datao = open("day11.txt").read().strip()
datao = datao.split('\n')
# [print(i) for i in data]

# Part 1
# Expansion
data = datao.copy()

rows, cols = [], []
for i in range(len(data)):
    if data[i].count('#') == 0: rows.append(i)
    empty = True
    for j in range(len(data[i])):
        if data[j][i] == '#': empty = False
    if empty: cols.append(i)
for r in sorted(rows, reverse=True):
    data.insert(r, data[r])
for i, row in enumerate(data):
    for c in sorted(cols, reverse=True):
        row = row[:c] + '.' + row[c:]
    data[i] = row

# Solving

galaxylocs = []
for y, row in enumerate(data):
    for x, _ in enumerate(row):
        if _ == '#':
            galaxylocs.append((x, y))


def getDist(a, b):
    x1, y1, x2, y2 = a[0], a[1], b[0], b[1]
    return (abs(x1 - x2) + abs(y1 - y2))


res = 0
for y, a in enumerate(galaxylocs):
    for x, b in enumerate(galaxylocs):
        res += getDist(a, b)

print('Part 1: ', res // 2)

# Part 2
data = datao.copy()

rows, cols = [], []
for i in range(len(data)):
    if data[i].count('#') == 0:
        rows.append(i)

for i in range(len(data[0])):
    c = [row[i] for row in data]
    if c.count('#') == 0:
        cols.append(i)

galaxylocs = []
for y, row in enumerate(data):
    for x, _ in enumerate(row):
        if _ == '#':
            galaxylocs.append((x, y))


def getDist2(a, b):
    x1, y1, x2, y2 = min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])
    e = [i for i in cols if i in range(x1, x2)]
    f = [i for i in rows if i in range(y1, y2)]
    additional = len(e + f)
    # if additional > 0: print(a, b, additional, e, f)
    return x2 - x1 + y2 - y1 + (additional * 999999)


res = 0
for y, a in enumerate(galaxylocs):
    for x, b in enumerate(galaxylocs):
        if x > y:
            r = getDist2(a, b)
            res += r

print('Part 2: ', res)
