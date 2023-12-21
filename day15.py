data = open("day15.txt").read().strip()
data = data.split(',')

# Part 1

def HASH(input):
    cur = 0
    for i in input:
        cur += ord(i)
        cur = (17 * cur) % 256
    return cur

res = []
for seq in data:
    res.append(HASH(seq))

print('Part 1: ', sum(res))

# Part 2
# - remove
# = put

labels = {i: [] for i in range(256)}
lenses = {i: [] for i in range(256)}

for seq in data:
    if '=' in seq:
        split = seq.split('=')
        hash = HASH(split[0])
        if split[0] in labels[hash]:  # replace
            lenses[hash][labels[hash].index(split[0])] = int(split[1])
        else:  # add
            labels[hash].append(split[0])
            lenses[hash].append(int(split[1]))
    elif '-' in seq:
        split = seq[:-1]
        hash = HASH(split)
        if split in labels[hash]:
            lenses[hash].pop(labels[hash].index(split))
            labels[hash].pop(labels[hash].index(split))

res = []
for i in range(256):
    for j in range(len(lenses[i])):
        res.append((i + 1) * (j + 1) * lenses[i][j])

print('Part 2: ', sum(res))
