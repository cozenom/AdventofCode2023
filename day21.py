data = open("day21.txt").read().strip()

data = data.split('\n')

garden_plots = []
rocks = []
start = []

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == '#':
            rocks.append((x, y))
        elif c == '.':
            garden_plots.append((x, y))
        elif c == 'S':
            start.append((x, y))

# Part 1

def getneighbors(coord):
    x, y = coord
    res = [i for i in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if i not in rocks]
    return res


current = start

for _ in range(64):
    new = []
    for i in current:
        new.extend(getneighbors(i))
    current = set(new)

print('Part 1: ', len(current))

# Part 2

# how many garden plots could the Elf reach in exactly 26501365 steps?

