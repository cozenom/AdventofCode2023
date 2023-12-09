data = open("day9.txt").read().strip()
data = data.split('\n')
data = [[int(j) for j in i.split()] for i in data]


# Part 1
def getNext(l: list):
    diffs = [l[i + 1] - l[i] for i, j in enumerate(l[:-1])]
    # base case
    if sum(diffs) == 0:
        return l[0]
    return getNext(diffs) + l[-1]


res = 0
for seq in data:
    res += getNext(seq)

print('Part 1: ', res)


# Part 2
def getPrev(l: list):
    diffs = [l[i + 1] - l[i] for i, j in enumerate(l[:-1])]
    # base case
    if sum(diffs) == 0:
        return l[0]

    return l[0] - getPrev(diffs)


res = 0
for seq in data:
    res += getPrev(seq)

print('Part 2: ', res)
