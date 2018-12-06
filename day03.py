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


def find_claim(grid):
    elves_all = set()
    for elves_cell in grid.values():
        elves_all.update(elves_cell)
    for elves_cell in grid.values():
        if len(elves_cell) > 1:
            elves_all.difference_update(elves_cell)
    return elves_all.pop()


if __name__ == '__main__':
    with open('input03.txt') as f:
        claims = f.readlines()
    grid = load_grid(claims)
    overlap = fabric_overlap(grid)
    id_no_overlap = find_claim(grid)
    print(f'Day 03 - Part 1 - Answer: {overlap}')
    print(f'Day 03 - Part 2 - Answer: {id_no_overlap}')


