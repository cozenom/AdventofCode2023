from heapq import heappop, heappush

data = open("day17.txt").read().strip().split()
# Part 2
# ULTRA CRUCIBLE!!
# minimum of four blocks before it can turn
# maximum of ten consecutive blocks without turning
xrange, yrange = range(0, len(data[0])), range(0, len(data))


def addq(queue, heatloss: int, x: int, y: int, dx: int, dy: int, steps):
    newx, newy = x + dx, y + dy
    if newx not in xrange or newy not in yrange: return
    heappush(queue, (heatloss + int(data[newy][newx]), newx, newy, dx, dy, steps))


# heatloss, x, y, dx, dy, steps
q = [(0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 0)]
visited = set()

while q:
    heatloss, x, y, dx, dy, steps = heappop(q)

    if (x, y) == (len(data[y]) - 1, len(data) - 1) and steps >= 4:
        res = heatloss
        break

    if (x, y, dx, dy, steps) in visited: continue
    visited.add((x, y, dx, dy, steps))

    if steps < 10:  # go straight
        addq(q, heatloss, x, y, dx, dy, steps + 1)
    if steps >= 4:  # can turn
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if dir not in [(-dx, -dy), (dx, dy)]:
                addq(q, heatloss, x, y, dir[0], dir[1], 1)

print('Part 2: ', res)
