import re

def fabric_overlap(claims):
    grid = {}
    for c in claims:
        r = re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', c)
        if r:
            elf, col, row, width, height = (int(x) for x in r.group(1, 2, 3, 4, 5))
            for i in range(col, col+width):
                for j in range(row, row+height):
                    elves = grid.get((i, j), set())
                    elves.add(elf)
                    grid[(i, j)] = elves

    overlap = 0
    for elves in grid.values():
        if len(elves) > 1:
            overlap += 1
    return overlap


if __name__ == '__main__':
    with open('input03.txt') as f:
        claims = f.readlines()
    overlap = fabric_overlap(claims)
    print(f'Day 03 - Part 1 - Answer: {overlap}')

