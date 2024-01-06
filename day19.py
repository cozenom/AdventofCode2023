import re

data = open("day19.txt").read().strip()
data = data.split('\n\n')
workflows = dict()
for w in data[0].split():
    workflows[w[:-1].split('{')[0]] = w[:-1].split('{')[1].split(',')
parts = [{j.split('=')[0]: int(j.split('=')[1]) for j in i[1:-1].split(',')} for i in data[1].split()]


# Part 1

res = 0
for part in parts:
    w = 'in'
    while True:
        if w == 'R':
            break
        if w == 'A':
            res += sum(part.values())
            break

        current = workflows[w]
        for i, step in enumerate(current):
            if i == len(current) - 1:  # End of step
                w = step
                break
            if eval(str(part[step[0]]) + re.findall('[<>][0-9]+', step)[0]):
                w = step.split(':')[1]
                break

print('Part 1: ', res)
