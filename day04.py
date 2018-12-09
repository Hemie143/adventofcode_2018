import re

def load_guards(records):
    guards_sleeps = {}
    for r in sorted(records):
        if 'begins shift' in r:
            guard_id = int(re.search(r'#([0-9]+)', r).group(1))
        elif 'asleep' in r:
            sleep_start = int(re.search(r' 00:([0-9]+)', r).group(1))
        elif 'wakes up' in r:
            sleep_stop = int(re.search(r' 00:([0-9]+)', r).group(1))
            if not guard_id in guards_sleeps:
                guards_sleeps[guard_id] = [0] * 60
            for i in range(sleep_start, sleep_stop):
                guards_sleeps[guard_id][i] += 1
    return guards_sleeps

def find_sleepy_guard(sleeps):
    return max(sleeps, key=lambda g: sum(sleeps[g]))

def most_sleep_minute(sleep):
    return sleep.index(max(sleep))


if __name__ == '__main__':
    with open('input04.txt') as f:
        records = f.readlines()
    sleeps = load_guards(records)
    guard = find_sleepy_guard(sleeps)
    minute = most_sleep_minute(sleeps[guard])
    print(f'Day 04 - Part 1 - Answer: {guard} * {minute} = {guard * minute}')
    # print(f'Day 04 - Part 2 - Answer: {}')

