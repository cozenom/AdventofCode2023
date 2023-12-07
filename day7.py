data = open("day7.txt").read().strip()
data=[i.split(' ') for i in data.split('\n')]

vals = {'A':14, 'K':13, 'Q':12, 'J':11, 'T': 10}
for i in '98765432':vals[i] = int(i)

# Part 1
# Find the rank of every hand in your set. What are the total winnings?
# Get hand values
def getHandVals(data, vals = vals):
    processed = []
    for i, row in enumerate(data):
        data[i][1] = int(data[i][1])
        hand, counts = row[0], []
        Jcount = row[0].count('J')
        for card in hand:
            counts.append(hand.count(card))
        #print(row, counts,Jcount)

        if 'J' in hand:
            m = max(counts)
        else:
            m = max(counts)

        if m==5:
            # Five of a kind
            res = [7]
        elif m==4:
            #  Four of a kind
            res = [6]
        elif m==3:
            if 2 in counts:
                # Full house
                res = [5]
            else:
                # Three of a kind
                res = [4]
        elif m==2:
            if counts.count(2)==4:
                # Two pair
                res = [3]
            else:
                # One pair
                res = [2]
        else:
            # High card
            res = [1]

        [res.append(vals[v]) for v in hand]
        res.append([hand, data[i][1]])
        processed.append(res)
    return processed

processed = getHandVals(data)
# V useful https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
processed = sorted(processed, key= lambda processed: (processed[0],processed[1],processed[2],processed[3],processed[4],processed[5]), reverse=True)
res = 0
for i, row in enumerate(processed):
    res += row[-1][-1] * (len(processed)-i)
print('Part 1: ',res)


# Part 2
vals['J'] = 1
print(vals)
processed = getHandVals(data, vals)
print(processed)

