data = open("day3.txt").read().strip()
data = data.split('\n')


# data = ['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.','...$.*....','.664.598..']


# Part 1
# There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a
# symbol, even diagonally, is a "part number" and should be included in your sum.
def findnumber(row, x, y, symbols={'#', '%', '@', '-', '$', '/', '*', '=', '&', '+', '.'}):
    left, right = row[:x], row[x + 1:]
    numminx, nummaxx = 0, len(row)
    for i in symbols:
        if left.rfind(i) != -1:
            numminx = max(numminx, left.rfind(i) + 1)
        if right.find(i) != -1:
            nummaxx = min(nummaxx, right.find(i) + 1)
    num = row[numminx: x + nummaxx]
    numl = len(num)

    row = row[:numminx] + '.' * numl + row[x + nummaxx:]
    return int(num), row


maxy = len(data)
maxx = len(data[0])
partlocations = []
notparts = [str(i) for i in range(0, 10)]
tocheck = []
notparts.append('.')
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val not in notparts:
            partlocations.append([x, y])
            l = [[x - 1, y + 1], [x - 1, y], [x - 1, y - 1], [x, y + 1], [x, y - 1], [x + 1, y + 1], [x + 1, y],
                 [x + 1, y - 1]]
            tocheck.extend(l)

resa = []
res = 0
for y, row in enumerate(data):
    for x, val in enumerate(row):
        val = row[x]
        if [x, y] in tocheck and val != '.':
            num, row = findnumber(row, x, y)
            res += num
            resa.append(num)

print('Part 1: ', res)
# print(resa)


# Part 2
data = open("day3.txt").read().strip()
data = data.split('\n')

gear = '*'
resproduct = 0
symbols = {'#', '%', '@', '-', '$', '/', '*', '=', '&', '+', '.'}

for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == gear:
            #print('Gear found: ', [x, y])
            check = [[x - 1, y + 1], [x - 1, y], [x - 1, y - 1], [x, y + 1], [x, y - 1], [x + 1, y + 1], [x + 1, y],
                     [x + 1, y - 1]]
            numlist = []
            for x2, y2 in check:
                if x2 < 0 or x2 > 140 or y2 < 0 or y2 > 140: continue
                curr = data[y2][x2]
                if curr not in symbols:
                    num, data[y2] = findnumber(data[y2], x2, y2)
                    if y2==y: row = data[y2]
                    numlist.append(num)
            if len(numlist) == 2:
                #print('Criteria matched: ', numlist)
                resproduct += numlist[0] * numlist[1]


print('Part 2: ', resproduct)
