data = open("day14.txt").read().strip()
data = data.split()


# [print(i) for i in data]

# Part 1
def getLocs(d, symb):
    res = []
    for y, row in enumerate(d):
        for x, _ in enumerate(row):
            if d[y][x] == symb: res.append((x, y))
    return sorted(res)


def rollNorth(rollingstones, b):
    rollingstones.sort()
    allblocks = b.copy()
    newpositions = []
    for stone in rollingstones:
        x, y = stone[0], stone[1]
        filtered = sorted(list(filter(lambda b: b[0] == x and b[1] < y, allblocks)))
        if len(filtered) == 0:  # No blocks above rock
            allblocks.append((x, 0))
            newpositions.append((x, 0))
        else:  # blocks above rock
            newy = filtered[-1][1] + 1
            allblocks.append((x, newy))
            newpositions.append((x, newy))
            # print(stone, (x, newy), 'newy')
        allblocks.sort()
    return sorted(newpositions)


def getLoad(d, maxload):
    load = 0
    for stone in d:
        load += (maxload - stone[1])
    return load


stones = getLocs(data, 'O')
blocks = getLocs(data, '#')
res = rollNorth(stones, blocks)
print('Part 1: ', getLoad(res, len(data)))

# Part 2
# Cycle = north, then west, then south, then east
# Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?

# Rotate array or make roll E S W
start = data
stones = getLocs(data, 'O')
blocks = getLocs(data, '#')
xlen, ylen = len(data[0]), len(data)


def rotate90(data, ylen):  # clockwise
    res = []
    for stone in data:
        res.append((ylen - (stone[1] + 1), stone[0]))
    return res


seen = []
loads = []
for i in range(1000000000):
    for j in range(4):
        stones = rollNorth(stones, blocks)
        stones, blocks = rotate90(stones, ylen), rotate90(blocks, ylen)
        xlen, ylen = ylen, xlen

    if set(stones) in seen:
        repleft = seen.index(set(stones))
        break
    else:
        seen.append(set(stones))
        loads.append(getLoad(stones, ylen))

t = (1000000000 - repleft) % (i - repleft)

print('Part 2: ', loads[repleft + t - 1])
