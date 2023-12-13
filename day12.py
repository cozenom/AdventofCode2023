data = open("day12.txt").read().strip()
data = [[i.split(' ')[0], [int(j) for j in i.split(' ')[1].split(',')]] for i in data.split('\n')]
[print(i) for i in data]

# Part 1
# operational (.) or damaged (#)


