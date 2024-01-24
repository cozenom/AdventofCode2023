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

print(module_dict)
print('CONJ', conj_modules)
print('FF', ff_modules)
print()

# False = lo, True = hi
for _ in range(1000):
    queue = [[i, False, None] for i in broadcaster[1]]
    lo += 1
    while queue:
        current_module, hi_pulse, parent_module = queue.pop(0)
        print('----------------------------')
        print(current_module, hi_pulse, queue)
        if hi_pulse: hi +=1
        else: lo +=1
        if current_module not in module_dict.keys():continue
        switch_type = module_dict[current_module]['type']
        print(current_module, module_dict[current_module], switch_type)
        if switch_type == '%':
            if hi_pulse:
                print('ignore')
                continue
            else:
                ff_modules[current_module] = not ff_modules[current_module]
                if ff_modules[current_module]:  # Turns ON -> send hi
                    print('send hi')
                    [queue.append([i, True, current_module]) for i in module_dict[current_module]['connected']]
                else:  # Turns OFF -> send lo
                    print('send lo')
                    [queue.append([i, False, current_module]) for i in module_dict[current_module]['connected']]
        elif switch_type == '&':
            conj_modules[current_module][parent_module] = hi_pulse  # Update memory
            print(conj_modules[current_module], conj_modules[current_module].values())
            if all(conj_modules[current_module].values()): # All inputs hi -> send hi
                [queue.append([i, False, current_module]) for i in module_dict[current_module]['connected']]
                print('send hi')
            else:
                [queue.append([i, True, current_module]) for i in module_dict[current_module]['connected']]
                print('send lo')
print('============================')

print(module_dict)
print('CONJ', conj_modules)
print('FF', ff_modules)
print()
print(lo, hi)
print(lo*hi)