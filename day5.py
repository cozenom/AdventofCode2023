data = open("day5.txt").read().strip()
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
data = open("day5.txt").read().strip().split('\n\n')

seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]

mappings = []
for l in data[1:]:
    l = l.split('\n')
    cur = []
    for i in l[1:]:
        cur.append([int(i) for i in i.split()])
    mappings.append(cur)


res = 2 ** 64
for seed, r in zip(seeds[::2], seeds[1::2]):
    ranges = [(seed, seed + r - 1)]
    for typemappings in mappings:
        newranges = []
        for l, h in ranges:
            found = False
            for md, ms, mo in typemappings:
                if l >= ms and h < ms + mo:
                    newranges.append((l - ms + md, h - ms + md))
                    found = True
                elif l < ms and h >= ms and h < ms + mo:
                    ranges.append((l, ms - 1))
                    newranges.append((md, md + h - ms))
                    found = True
                elif l < ms + mo and h >= ms + mo and l >= ms:
                    ranges.append((ms + mo, h))
                    newranges.append((md + l - ms, md + mo - 1))
                    found = True
                elif l < ms and h >= ms + mo:
                    ranges.append((l, ms - 1))
                    newranges.append((md, md + mo - 1))
                    ranges.append((ms + mo, h))
                    found = True
                if found == True:
                    break
            if found == False:
                newranges.append((l, h))
        ranges = newranges.copy()
    res = min(res, min(ranges)[0])

print('Part 2: ', res)
