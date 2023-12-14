data = open("day13.txt").read().strip()

data = [i.split('\n') for i in data.split('\n\n')]

res = 0
for scen in data:
    x, y = len(scen), len(scen[0])
    rotated = [[scen[j][i] for j in reversed(range(x))] for i in range(y)]
    maxcol = 0
    for i, _ in enumerate(rotated):
        a = rotated[:i][::-1]
        b = rotated[i:][:i]
        m = min(len(a), len(b))
        if a[:m] == b[:m]:
            maxcol = i

    maxrow = 0
    for i, _ in enumerate(scen):
        a = scen[:i][::-1]
        b = scen[i:][:i]
        m = min(len(a), len(b))
        if a[:m] == b[:m]:
            maxrow = i
    res += max(maxrow * 100, maxcol)

# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection;
# to that, also add 100 multiplied by the number of rows above each horizontal line of reflection.
print('Part 1: ', res)
