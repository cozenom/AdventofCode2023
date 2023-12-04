data = open("day4.txt").read().strip()
data = data.split('\n')

# data = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53','Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19','Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1','Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83','Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36','Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
# a list of winning numbers and then a list of numbers you have
for i, line in enumerate(data):
    line = line.split(': ')
    line[0] = int(line[0].split()[-1])
    line[1] = line[1].split('|')
    line[1][0] = [int(j) for j in line[1][0].split(' ') if j != '']
    line[1][1] = [int(j) for j in line[1][1].split(' ') if j != '']
    data[i] = line

# Part 1
# As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear
# in the list of winning numbers. The first match makes the card worth one point and each match after the first
# doubles the point value of that card.

res = 0
for card in data:
    numbers, mycard = card[1][0], card[1][1]
    count = 0
    found = []
    for number in numbers:
        if number in mycard:
            count += mycard.count(number)
            found.append(number)
    if count > 0:
        res += pow(2, count - 1)

print('Part 1: ', res)

# Part 2
# scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.
# how many total scratchcards do you end up with?

res = 0
l = [i[0] for i in data]
scratchboards = {}
for i in l: scratchboards[i] = 0

for card in data:
    cardnr, numbers, mycard = card[0], card[1][0], card[1][1]
    scratchboards[cardnr] += 1
    found = []
    for number in numbers:
        if number in mycard:
            found.append(number)
    if len(found)>0:
        for i in range(cardnr+1, cardnr + len(found)+1):
            if i in scratchboards.keys():
                scratchboards[i] += scratchboards[cardnr]

print('Part 2: ', sum(scratchboards.values()))
