import re
from collections import defaultdict

def load_steps(data):
    steps = set()
    deps = defaultdict(set)
    for instruction in data:
        r = re.match(r'Step ([A-Z]) must .* step ([A-Z]) can begin.', instruction)
        prev, step = r.group(1, 2)
        steps.update(prev, step)
        if step in deps:
            deps[step].add(prev)
        else:
            deps[step] = set(prev)
    return (steps, deps)

def find_correct_order(steps, deps):
    chain = []
    for s in steps:
        # min for first letter in alphabetical order
        # add if not in chain already and if dependencies are already in chain
        chain.append(min([x for x in steps if x not in chain and deps[x] <= set(chain)]))
    return ''.join(chain)

if __name__ == '__main__':
    with open('input07.txt') as f:
        data = f.readlines()
    steps, deps = load_steps(data)
    chain = find_correct_order(steps, deps)
    print(f'Day 07 - Part 1 - Answer: {chain}')
    # print(f'Day 07 - Part 2 - Answer: {dist_area}')

