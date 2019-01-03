import re
from collections import defaultdict


def load_steps(data):
    steps = set()
    deps = defaultdict(set)
    for instruction in data:
        r = re.match(r'.*Step ([A-Z]) must .* step ([A-Z]) can begin.', instruction)
        prev, step = r.group(1, 2)
        steps.update(prev, step)
        if step in deps:
            deps[step].add(prev)
        else:
            deps[step] = set(prev)
    return (steps, deps)


def time_sorting(steps, deps, num_workers=2, step_duration=0):
    seconds = 0
    chain = []
    queue = []
    workers = {i:['', 0] for i in range(num_workers)}
    while len(chain) < len(steps):
        for worker_id in range(num_workers):
            worker_step, worker_keep = workers[worker_id]
            if not worker_step:
                # Select the next step
                candidates = [x for x in steps if x not in queue and deps[x] <= set(chain)]
                if candidates:
                    worker_step = min(candidates)
                    worker_keep = ord(worker_step) - ord('A') + 1 + step_duration
                    queue.append(worker_step)
                workers[worker_id] = [worker_step, worker_keep]
            else:
                worker_keep -= 1
                if worker_keep <= 0:
                    # Step completed and select a new one
                    chain.append(worker_step)
                    candidates = [x for x in steps if x not in queue and deps[x] <= set(chain)]
                    if candidates:
                        worker_step = min(candidates)
                        worker_keep = ord(worker_step) - ord('A') + 1 + step_duration
                        queue.append(worker_step)
                    else:
                        worker_step = ''
                        worker_keep = 0
                    workers[worker_id] = [worker_step, worker_keep]
                else:
                    workers[worker_id] = [worker_step, worker_keep]
        seconds += 1
    return ''.join(chain), (seconds-1)


if __name__ == '__main__':
    with open('input07.txt') as f:
        data = f.readlines()
    steps, deps = load_steps(data)
    chain, duration = time_sorting(steps, deps, 1, 0)
    print(f'Day 07 - Part 1 - Answer: {chain}')
    chain, duration = time_sorting(steps, deps, 6, 60)
    print(f'Day 07 - Part 2 - Answer: {duration}')
