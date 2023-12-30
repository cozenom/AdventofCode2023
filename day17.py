from heapq import heappop, heappush
data = open("day17.txt").read().strip().split()
xrange, yrange = range(0, len(data[0])), range(0, len(data))


def addq(queue, heatloss: int, x: int, y: int, dx: int, dy: int, steps):
    newx, newy = x + dx, y + dy
    if newx not in xrange or newy not in yrange: return
    heappush(queue, (heatloss + int(data[newy][newx]), newx, newy, dx, dy, steps))


q = [(0, 0, 0, 0, 0, 0)]
visited = set()

while q:
    heatloss, x, y, dx, dy, steps = heappop(q)

    if (x, y) == (len(data[y]) - 1, len(data) - 1):
        res = heatloss
        break

    if (x, y, dx, dy, steps) in visited: continue
    visited.add((x, y, dx, dy, steps))

    if steps < 3 and (dx, dy) != (0, 0):  # same dir
        addq(q, heatloss, x, y, dx, dy,  steps + 1)

    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # other dirs
        if dir not in [(-dx, -dy), (dx, dy)]:
            addq(q, heatloss, x, y, dir[0], dir[1], 1)

print('Part 1: ', res)

