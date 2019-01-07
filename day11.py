

def cell_pwr(x, y, serial):
    rackId = x + 10
    power = (int(((rackId * y + serial) * rackId / 100)) % 10) - 5
    return power

def square_pwr(grid_power, x, y, select_size):
    return sum([grid_power[x + i][y + j] for i in range(select_size) for j in range(select_size)])

def select_cell(grid_size, select_size, serial):
    grid_power = [[0] * grid_size for _ in range(grid_size)]
    for x in range(1, grid_size - select_size):
        for y in range(1, grid_size - select_size):
            grid_power[x][y] = cell_pwr(x, y, serial)
    max_cell_power = sum([grid_power[1+i][1+j] for i in range(select_size) for j in range(select_size)])
    for x in range(1, grid_size - select_size):
        for y in range(1, grid_size - select_size):
            cell_power = square_pwr(grid_power, x, y, select_size)
            if cell_power > max_cell_power:
                max_cell_power = cell_power
                cell_x, cell_y = x, y
    return cell_x, cell_y, max_cell_power

def select_cellsize(grid_size, serial):
    max_cell_power = 0
    for size in range(1, grid_size):
        x, y, cell_power = select_cell(grid_size, size, serial)
        print('size: {} - power: {}'.format(size, cell_power))
        if cell_power > max_cell_power:
            best_x, best_y, max_cell_power = x, y, cell_power
    return x, y, size

if __name__ == '__main__':
    with open('input11.txt') as f:
        serial = f.read()

    # TODO: generate grid only once
    x, y, _ = select_cell(300, 3, int(serial))
    print(f'Day 11 - Part 1 - Answer: {x}, {y}')


