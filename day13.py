
dir_u, dir_d, dir_l, dir_r = (0, -1), (0, 1), (-1, 0), (1, 0)

directions = {'v': dir_d, '^': dir_u, '<': dir_l, '>': dir_r}
turn_slash = {dir_u: dir_r, dir_d: dir_l, dir_l: dir_d, dir_r: dir_u}
turn_backslash = {dir_u: dir_l, dir_d: dir_r, dir_l: dir_u, dir_r: dir_d}

dir_next = {dir_u: [dir_l, dir_u, dir_r], dir_d: [dir_r, dir_d, dir_l],
            dir_l: [dir_d, dir_l, dir_u], dir_r: [dir_u, dir_r, dir_d]}

def load_data(data):
    circuit = {}
    carts = {}      # TODO: use OrderedDict ?, namedTuple ?
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            circuit[(x, y)] = c
            if c in 'v^<>':
                carts[(x, y)] = [directions[c], 0]
    return circuit, carts


def cycle(circuit, carts):
    crash_first = None
    while len(carts) > 1:
        carts_coords = sorted(carts, key=lambda c: (c[1], c[0]))
        for cart in carts_coords:
            direction = carts[cart][0]
            turns = carts[cart][1]
            coords = (cart[0] + direction[0], cart[1] + direction[1])       # TODO: enhance
            if coords in carts or coords in carts:
                if not crash_first:
                    crash_first = coords
                if coords in carts_coords:
                    carts_coords.remove(coords)
                    del carts[coords]
                    del carts[cart]
                if coords in carts:
                    del carts[coords]
                    del carts[cart]
                continue
            if circuit[coords] == '/':
                del carts[cart]
                carts[coords] = [turn_slash[direction], turns]
            elif circuit[coords] == '\\':
                del carts[cart]
                carts[coords] = [turn_backslash[direction], turns]
            elif circuit[coords] == '+':
                del carts[cart]
                new_dir = dir_next[direction][turns % 3]
                carts[coords] = [new_dir, turns + 1]
            else:
                del carts[cart]
                carts[coords] = [direction, turns]
    last_cart = None
    if carts:
        last_cart = list(carts.keys())[0]
    return crash_first, last_cart


if __name__ == '__main__':
    with open('input13.txt') as f:
        map_data = f.read()
    circuit, carts = load_data(map_data)
    crash_coords = cycle(circuit, carts)
    print(f'Day 13 - Part 1 - Answer: {crash_coords[0]}')
    print(f'Day 13 - Part 2 - Answer: {crash_coords[1]}')
