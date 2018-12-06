import re

def load_grid(claims):
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
    return grid

def fabric_overlap(grid):
    overlap = 0
    for elves in grid.values():
        if len(elves) > 1:
            overlap += 1
    return overlap

def test(claims):
    for k, cell in grid.items():
        print(f'{k}:{cell}')
        # pass
    return


if __name__ == '__main__':
    with open('input03.txt') as f:
        claims = f.readlines()
    grid = load_grid(claims)
    overlap = fabric_overlap(grid)
    test(claims)
    print(f'Day 03 - Part 1 - Answer: {overlap}')

    print(load_grid(['#1 @ 1,3: 4x4',
                                 '#2 @ 3,1: 4x4',
                                 '#3 @ 5,5: 2x2']))

