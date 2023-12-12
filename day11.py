data = open("day11.txt").read().strip()
data = data.split('\n')

# Part 1
# Expansion
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

[print(i) for i in data]

galaxylocs = []
for y, row in enumerate(data):
    for x, _ in enumerate(row):
        if _ == '#':
            galaxylocs.append((x, y))
print(galaxylocs)
print(len(galaxylocs))




