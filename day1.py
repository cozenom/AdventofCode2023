data = open("day1.txt").read().strip()
data = data.split('\n')

nums = [str(i) for i in range(0,10)]

## Part 1:
res = 0
for line in data:
    toadd = ''
    for i in line:
        if i in nums:
            toadd += i
            break
    for i in line[::-1]:
        if i in nums:
            toadd += i
            break
    res += int(toadd)
print("Part 1 answer: ")
print(res)

## Part 2

# Create dict
numsl = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numsdict = {}
for idx,i in enumerate(nums):
    numsdict[i] = str(idx)
for idx,i in enumerate(numsl):
    numsdict[i] = str(idx+1)

#Evaluate
res = 0
for line in data:
    print(line)
    minpos = len(line)
    curmin = -1
    maxpos = 0
    curmax = -1
    for i in numsdict.keys():
        findfront = line.find(i)
        if findfront <= minpos and findfront != -1:
            minpos = findfront
            curmin = numsdict[i]

        findback = line.rfind(i)
        if findback >= maxpos and findback != -1:
            maxpos = findback
            curmax = numsdict[i]
    res += int(curmin+curmax)

print("Part 2 answer: ")
print(res)