data = open("day12.txt").read().strip()
data = [[i.split(' ')[0], [int(j) for j in i.split(' ')[1].split(',')]] for i in data.split('\n')]


# Part 1
# operational (.) or damaged (#)


def DP(line, nums, part2=False):
    if part2:
        line = ((line + '?') * 5)[:-1]
        nums = nums * 5
    seen = {}

    def sub(idx, nidx, b):
        if (idx, nidx, b) in seen: return seen[(idx, nidx, b)]
        if idx == len(line):
            return int(nidx == len(nums) and b == 0 or nidx == len(nums) - 1 and b == nums[-1])

        res = 0
        if line[idx] in '.?':
            if b == 0:
                res += sub(idx + 1, nidx, 0)
            else:
                if nidx == len(nums): return 0
                if b == nums[nidx]:
                    res += sub(idx + 1, nidx + 1, 0)

        if line[idx] in '?#':
            res += sub(idx + 1, nidx, b + 1)
        seen[(idx, nidx, b)] = res
        return res

    return sub(0, 0, 0)


res = 0
for line in data:
    res += DP(line[0], line[1])

print('Part 1: ', res)

res = 0
for line in data:
    res += DP(line[0], line[1], True)
print('Part 2: ', res)
