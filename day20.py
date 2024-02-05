data = open("day20.txt").read().strip()

data = data.split('\n')
data = [[j[0], j[1].split(', ')] for j in [i.split(' -> ') for i in data]]

broadcaster = [i for i in data if i[0] == 'broadcaster'][0]
module_dict = {k[1:]: {'type': k[0], 'connected': v} for k, v in data if k != 'broadcaster'}
# Flipflop modules
ff_modules = {i: False for i in module_dict.keys() if module_dict[i]['type'] == '%'}
# Get conjunction module inputs
conj_modules = {i: {} for i in module_dict.keys() if module_dict[i]['type'] == '&'}
for i in conj_modules.keys():
    t=[]
    for j in module_dict.keys():
        if i in module_dict[j]['connected']:
            t.append(j)
    conj_modules[i] = {x:False for x in t}

lo, hi = 0, 0
# False = lo, True = hi
for _ in range(1000):
    queue = [[i, False, None] for i in broadcaster[1]]
    lo += 1
    while queue:
        current_module, hi_pulse, parent_module = queue.pop(0)
        if hi_pulse: hi +=1
        else: lo +=1
        if current_module not in module_dict.keys():continue
        switch_type = module_dict[current_module]['type']
        if switch_type == '%':
            if hi_pulse:
                continue
            else:
                ff_modules[current_module] = not ff_modules[current_module]
                if ff_modules[current_module]:  # Turns ON -> send hi
                    [queue.append([i, True, current_module]) for i in module_dict[current_module]['connected']]
                else:  # Turns OFF -> send lo
                    [queue.append([i, False, current_module]) for i in module_dict[current_module]['connected']]
        elif switch_type == '&':
            conj_modules[current_module][parent_module] = hi_pulse  # Update memory
            if all(conj_modules[current_module].values()): # All inputs hi -> send hi
                [queue.append([i, False, current_module]) for i in module_dict[current_module]['connected']]
            else:
                [queue.append([i, True, current_module]) for i in module_dict[current_module]['connected']]
print('Part 1: ', lo*hi)

# Part 2

end = False
button_presses = 0
final_layer = [i for i in module_dict.keys() if 'lg' in module_dict[i]['connected']]
loop_sizes = []

while not end:
    queue = [[i, False, None] for i in broadcaster[1]]
    button_presses += 1
    while queue:
        current_module, hi_pulse, parent_module = queue.pop(0)
        if current_module in final_layer and not hi_pulse:
            loop_sizes.append(button_presses)
            final_layer.remove(current_module)
        if len(final_layer) == 0:
            end = True
            break
        if not hi_pulse and current_module == 'rx':
            end = True
            break
        if current_module not in module_dict.keys(): continue
        switch_type = module_dict[current_module]['type']
        if switch_type == '%':
            if hi_pulse:
                continue
            else:
                ff_modules[current_module] = not ff_modules[current_module]
                if ff_modules[current_module]:  # Turns ON -> send hi
                    [queue.append([i, True, current_module]) for i in module_dict[current_module]['connected']]
                else:  # Turns OFF -> send lo
                    [queue.append([i, False, current_module]) for i in module_dict[current_module]['connected']]
        elif switch_type == '&':
            conj_modules[current_module][parent_module] = hi_pulse  # Update memory
            if all(conj_modules[current_module].values()):  # All inputs hi -> send hi
                [queue.append([i, False, current_module]) for i in module_dict[current_module]['connected']]
            else:
                [queue.append([i, True, current_module]) for i in module_dict[current_module]['connected']]

import math
print('Part 2: ', math.lcm(*loop_sizes))
