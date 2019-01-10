from collections import defaultdict


def generate_summed_area(grid_size, serial):
    grid_power = defaultdict(int)
    for x in range(1, grid_size + 1):
        rackId = x + 10
        for y in range(1, grid_size + 1):
            p = (int(((rackId * y + serial) * rackId / 100)) % 10) - 5
            # https://en.wikipedia.org/wiki/Summed-area_table
            grid_power[(x, y)] = p + grid_power[(x, y-1)] + grid_power[(x-1, y)] - grid_power[(x-1, y-1)]
    return grid_power


def select_square(grid_power, grid_size, select_size):
    square_powers = []
    for x in range(1, grid_size - select_size + 1):
        for y in range(1, grid_size - select_size + 1):
            x0, y0 = x-1, y-1
            x1, y1 = x+select_size-1, y+select_size-1
            sp = grid_power[(x1, y1)] + grid_power[(x0, y0)] - grid_power[(x1, y0)] - grid_power[(x0, y1)]
            square_powers.append((sp, x, y))
    return max(square_powers)

def select_squaresize(grid_power, grid_size):
    square_powers = []
    # https://en.wikipedia.org/wiki/Summed-area_table
    for size in range(1, grid_size):
        # print(f'size: {size}')
        sp = select_square(grid_power, grid_size, size)
        square_powers.append((sp, size))
    return max(square_powers)


if __name__ == '__main__':
    with open('input11.txt') as f:
        serial = int(f.read())

    grid_size = 300
    select_size = 3
    grid_power = generate_summed_area(grid_size, serial)
    _, x, y = select_square(grid_power, grid_size, select_size)
    print(f'Day 11 - Part 1 - Answer: {x},{y}')
    sp, size = select_squaresize(grid_power, grid_size)
    print(f'Day 11 - Part 2 - Answer: {sp[1]},{sp[2]},{size}')  # 236,252,12

