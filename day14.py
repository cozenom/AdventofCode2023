data = open("day14.txt").read().strip()
data = data.split()
# [print(i) for i in data]


def getLocs(data, symb):
    res = []
    for y, row in enumerate(data):
        for x, _ in enumerate(row):
            if data[y][x] == symb: res.append((x, y))
    return sorted(res)


def rollNorth(data):
    rollingstones = getLocs(data, 'O')
    blocks = getLocs(data, '#')
    newpositions = []

    for stone in rollingstones:
        x, y = stone[0], stone[1]
        filtered = list(filter(lambda b: b[0] == x and b[1] < y, blocks))
        if len(filtered) == 0:  # No blocks above rock
            blocks.append((x, 0))
            newpositions.append((x, 0))
        else:  # blocks above rock
            newy = filtered[-1][1] + 1
            blocks.append((x, newy))
            newpositions.append((x, newy))
        # print(stone, filtered)
        blocks.sort()
    return newpositions


def getLoad(data, maxload):
    load = 0
    for stone in data:
        load += (maxload - stone[1])
    return load


res = rollNorth(data)
print('Part 1: ', getLoad(res, len(data)))
