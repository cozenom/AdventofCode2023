data = open("day5.txt").read().strip()
data = open("test.txt").read()
data = data.split('\n\n')

for i, row in enumerate(data):
    if row[:5] == 'seeds':
        row = row.split(': ')
        row[1] = [int(i) for i in row[1].split(' ')]
    else:
        row = row.split(':\n')
        # row[0] = row[0].split('-to-')
        row[1] = row[1].split('\n')

        for j, rec in enumerate(row[1]):
            row[1][j] = [int(i) for i in rec.split(' ')]
    data[i] = row

# Part 1
# What is the lowest location number that corresponds to any of the initial seed numbers?
start = data[0][1]
for map in data[1:]:
    pre = dict([(i, i) for i in start])
    ranges = map[1]
    # the destination range start, the source range start, and the range length.
    for r in ranges:
        dest, source, rlength = r[0], r[1], r[2]
        sourcerange = range(source, source + rlength)
        for i in pre.keys():
            if i in sourcerange:
                pre[i] = i - source + dest
    start = list(pre.values())

print('Part 1: ', min(start))


# Part 2
# the seeds: line actually describes ranges of seed numbers

def getOverlap(input, sourcerange):
    # Range
    x1, x2, y1, y2 = input[0], input[-1] + 1, sourcerange[0], sourcerange[-1] + 1
    r = [y1 < x1, y1 < x2, y2 < x1, y2 < x2]
    print(r)
    res = []
    if sum(r) == 1:
        # R
        res = [range(x1, y1), range(y1, x2), 1]
    elif sum(r) == 2:
        # Both
        if r[1] and r[3]:
            res = [range(x1,y1), range(y1,y2), range(y2,x2),1]
        if r[0] and r[1]:
            res = [input, 0]
    elif sum(r) == 3:
        # L
        res = [range(x1, y2), range(y2, x2), 0]
    else:
        # Neither
        res = [input]
    return res


start = []

for i in range(len(data[0][1]) // 2):
    a, b = data[0][1][2 * i], data[0][1][2 * i + 1]
    start.append([a, b])

ranges = []
for pair in start:
    ranges.append(range(pair[0], pair[0] + pair[1]))

start = ranges
print(start)
for mapping in data[1:]:
    pre = start
    post = []
    ranges = mapping[1]
    # the destination range start, the source range start, and the range length.
    print(mapping, pre)
    for r in ranges:
        dest, source, rlength = r[0], r[1], r[2]
        sourcerange = range(source, source + rlength)
        topop = []
        for i in range(len(pre)):
            print(i, pre[i], sourcerange)
            o = getOverlap(pre[i], sourcerange)
            if len(o) > 1:
                # Overlapped
                print('o', o)
                p = o[-1]
                res = o[:-1]
                # res[p] = range(dest - source + res[p][0], dest + (res[p][1] - res[p][0]))
                print(pre, post)
                print(dest-source, pre[i][0], pre[i][1])
                [pre.append(res[b]) if b != p else post.append(
                    range(dest-source+pre[i][0], dest - source + pre[i][-1])) for b in range(len(res))]
                print(pre, post)
                topop.append(i)
        for i in sorted(topop, reverse=True): pre.pop(i)
        print('pp', pre, post, topop)

    start = pre + post
print(start)