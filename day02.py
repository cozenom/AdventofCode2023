data = open("day02.txt").read().strip()
data = data.split('\n')

for i, cur in enumerate(data):
    cur = cur.split(': ')
    cur[0] = int(cur[0][5:])
    cur1 = cur[1].split('; ')
    for j, curs in enumerate(cur1):
        cur1[j] = cur1[j].split(', ')

    cur[1] = cur1
    data[i] = cur
for round in data:
    for game in round[1]:
        for i, s in enumerate(game):
            game[i] = s.split(' ')
            game[i][0] = int(game[i][0])

# Part 1

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes,
# and 14 blue cubes. What is the sum of the IDs of those games?

bag = {'red': 12, 'green': 13, 'blue': 14}
res = 0
for round in data:
    possible = True
    for game in round[1]:
        for grab in game:
            if bag[grab[1]] < grab[0]:
                possible = False
                break
    if possible:
        res += round[0]
    # print(round[0], possible, round[1])
print('Part 1: ', res)

# Part 2
# what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
import math
res = 0
mingames = []
for round in data:
    least = {}
    for game in round[1]:
        for grab in game:
            color = grab[1]
            if color in least.keys():
                least[color] = max(grab[0], least[color])
            else:
                least[color] = grab[0]
    mingames.append(least)
    res += math.prod(least.values())
print('Part 2: ', res)