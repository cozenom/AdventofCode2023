data = open("day13.txt").read().strip()
data = [i.split('\n') for i in data.split('\n\n')]


def findMirror(scen, part2=False):
    x, y = len(scen), len(scen[0])
    rotated = [[scen[j][i] for j in reversed(range(x))] for i in range(y)]
    maxcol = 0
    for i, _ in enumerate(rotated):
        a = rotated[:i][::-1]
        b = rotated[i:][:i]
        m = min(len(a), len(b))
        if part2:
            if getDiff(a[:m], b[:m]) == 1:
                maxcol = i
        else:
            if a[:m] == b[:m]:
                maxcol = i

    maxrow = 0
    for i, _ in enumerate(scen):
        a = scen[:i][::-1]
        b = scen[i:][:i]
        m = min(len(a), len(b))
        if part2:
            if getDiff(a[:m], b[:m]) == 1:
                maxrow = i
        else:
            if a[:m] == b[:m]:
                maxrow = i
    return max(maxrow * 100, maxcol)


res = 0
for scen in data:
    res += findMirror(scen)

# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection;
# to that, also add 100 multiplied by the number of rows above each horizontal line of reflection.
print('Part 1: ', res)


# Part 2
def getDiff(a, b):
    diff = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]: diff += 1
    return diff


res = 0
for scen in data:
    res += findMirror(scen, True)

print('Part 2: ', res)
