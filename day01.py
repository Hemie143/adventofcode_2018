def run_day01(changes):
    loop_max = 1000
    loop_count = 0
    frequency = 0
    frequency_list = set([0])
    frequency_dupe = None
    frequency_dupe_found = False
    frequency_end_found = False
    changes = [int(change) for change in changes]
    while not (frequency_dupe_found and frequency_end_found):
        for l in changes:
            frequency += int(l)
            if frequency not in frequency_list and not frequency_dupe_found:
                frequency_list.add(frequency)
            elif not frequency_dupe_found:
                frequency_dupe = frequency
                frequency_dupe_found = True
        if not frequency_end_found:
            frequency_end = frequency
            frequency_end_found = True
        loop_count += 1
        if loop_count > loop_max:
            break
    return frequency_end, frequency_dupe

if __name__ == '__main__':

    with open('input01.txt') as f:
        frequency_result, frequency_rep = run_day01(f)
    print(f'Day 01 - Part 1 - Answer: {frequency_result}')
    print(f'Day 01 - Part 2 - Answer: {frequency_rep}')
