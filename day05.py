import re
import string

def react(polymer):
    polymer = list(polymer)
    i = 1
    while i < len(polymer):
        if polymer[i] == polymer[i-1].swapcase():
            del(polymer[i], polymer[i-1])
            i -= 2
        i += 1
    return ''.join(polymer)

def optimize(polymer):
    optimal_length = len(polymer)
    units = {s.lower() for s in polymer}
    for u in units:
        test_polymer = re.sub(u, '', polymer, flags=re.IGNORECASE)
        result = len(react(test_polymer))
        # print(f'char: {u} - len: {result}')
        if result < optimal_length:
            optimal_length = result
    return optimal_length

def test(line):
    original = line
    best = len(line)
    for j in range(0, 26):
        line = original
        line = line.replace(chr(ord("a") + j), "")
        line = line.replace(chr(ord("A") + j), "")

        oldline = None
        while oldline != line:
            oldline = line
            for i in range(0, 26):
                line = line.replace(chr(ord("a") + i) + chr(ord("A") + i), "")
                line = line.replace(chr(ord("A") + i) + chr(ord("a") + i), "")

        # line = react(line)
        best = len(line) if len(line) < best else best
        print(f'best: {best}: char={chr(ord("a") + j)}')
    print("Part2:")
    print(best)

if __name__ == '__main__':
    with open('input05.txt') as f:
        polymer = f.read()
    polymer_reacted = react(polymer)
    print(f'Day 05 - Part 1 - Answer: {len(polymer_reacted)}')
    # print(f'Day 05 - Part 2 - Answer: {optimize(polymer)}')
    test(polymer)


