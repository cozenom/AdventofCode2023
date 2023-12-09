data = open("day6.txt").read().strip()
# data = "Time:      7  15   30\nDistance:  9  40  200"

data = data.split()
timedist = []
for i in range(len(data) // 2 - 1):
    td = [int(data[i + 1]), int(data[i + len(data) // 2 + 1])]
    timedist.append(td)

# Part 1
# Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend
# at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.
res = []
for race in timedist:
    time, record = race[0], race[1]
    timedict = {}
    for i in range(time):
        timedict[i] = i * (time - i)

    count = sum(1 if timedict[i] > record else 0 for i in timedict)
    res.append(count)

r = 1
for i in res: r *= i
print('Part 1:', r)

# Part 2
# There's really only one race - ignore the spaces between the numbers on each line.
t, d = '', ''
for i in range(1, len(data) // 2):
    t += data[i]
    d += data[len(data) // 2 + i]

t, d = int(t), int(d)

# Faster approach, start in the middle and go outwards
# ~5s
mid = (t + 1) / 2
if int(mid) != mid:
    test = 1
else:
    test = 0
# 30077773
for i in range(int(mid) + 1, t):
    # print(i*(t-i),d, 'a')
    if i * (t - i) < d: break
    test += 2
print('Part 2:', test)

# Slow iterative method as p1
# ~25s
"""
res = []
timedict = {}
for i in range(t):
    timedict[i]=i* (t-i)

count = sum(1 if timedict[i]> d else 0 for i in timedict)
res.append(count)

r = 1
for i in res: r*=i
print('Part 2:' , r)
"""
