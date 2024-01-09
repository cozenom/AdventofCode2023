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

# Part 2

processed_workflows = {}
for w in data[0].split():
    name, matches = w.split("{")
    matches = matches.split("}")[0]
    matches = matches.split(",")
    processed_workflows[name] = []
    for match in matches:
        parts = match.split(":")
        if len(parts) == 2:
            processed_workflows[name].append((parts[0], parts[1]))
        else:
            processed_workflows[name].append(("True", parts[0]))

def process_criteria(criteria):
    vals = {
        "x": [0] + [1] * 4000,
        "m": [0] + [1] * 4000,
        "a": [0] + [1] * 4000,
        "s": [0] + [1] * 4000,
    }
    for c in criteria:
        if c != "True":
            if c[0] == "!":
                c = c[1:]
                var, c, limit = c[0], c[1], int(c[2:])
                if c == "<":  # >= limit is okay
                    for i in range(1, limit):
                        vals[var][i] = 0
                else:  # <= limit is okay
                    for i in range(limit + 1, 4001):
                        vals[var][i] = 0
            else:
                var, c, limit = c[0], c[1], int(c[2:])
                if c == "<":  # < limit is okay
                    for i in range(limit, 4001):
                        vals[var][i] = 0
                else:  # > limit is okay
                    for i in range(1, limit + 1):
                        vals[var][i] = 0
    subtotal = 1
    for var, valid in vals.items():
        subtotal *= sum(valid)
    return subtotal


def process_rule(name, previous_crit, previous_rules):
    total = 0
    inverted_criteria = []
    for criteria, rule in processed_workflows[name]:
        if rule == "A":
            total += process_criteria(previous_crit + inverted_criteria + [criteria])
            inverted_criteria += ["!" + criteria]
        else:
            if rule != "R":
                total += process_rule(rule, previous_crit + inverted_criteria + [criteria], previous_rules + [name])
            inverted_criteria += ["!" + criteria]
    return total

res = process_rule("in", [], [])
print('Part 2: ', res)