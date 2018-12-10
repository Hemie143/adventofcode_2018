import re


def react(polymer):
    polymer = list(polymer)
    i = 1
    while i < len(polymer):
        if polymer[i] == polymer[i-1].swapcase():
            del(polymer[i], polymer[i-1])
            i -= 2
        i = max(i+1, 1)
    return ''.join(polymer)


def optimize(polymer):
    optimal_length = len(polymer)
    units = {s.lower() for s in polymer}
    for u in units:
        test_polymer = re.sub(u, '', polymer, flags=re.IGNORECASE)
        result = len(react(test_polymer))
        if result < optimal_length:
            optimal_length = result
    return optimal_length


if __name__ == '__main__':
    with open('input05.txt') as f:
        polymer = f.read()
    polymer_reacted = react(polymer)
    print(f'Day 05 - Part 1 - Answer: {len(polymer_reacted)}')
    print(f'Day 05 - Part 2 - Answer: {optimize(polymer)}')


