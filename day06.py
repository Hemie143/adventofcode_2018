import re


def load_coords(data):
    coords = []
    for c in data:
        r = re.match(r'([0-9]+), ([0-9]+)', c)
        x, y = r.group(1, 2)
        coords.append((int(x), int(y)))
    return coords


def find_grid_size(coords):
    minx = min([c[0] for c in coords]) - 1
    maxx = max([c[0] for c in coords]) + 1
    miny = min([c[1] for c in coords]) - 1
    maxy = max([c[1] for c in coords]) + 1
    return minx, maxx, miny, maxy


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_largest_area(coords):
    minx, maxx, miny, maxy = find_grid_size(coords)
    grid = {}       # No need to store the coordinates, a dict isn't necessary.
    blacklist = set()
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            dist_list = []
            loc = (x, y)
            for c in coords:
                dist_list.append(manhattan_distance(loc, c))
            min_dist = min(dist_list)
            nearest_coords = [i for i, d in enumerate(dist_list) if d == min_dist]
            if (x == minx or x == maxx or y == miny or y == maxy) and len(nearest_coords) == 1:
                blacklist.add(nearest_coords[0])
            if len(nearest_coords) == 1:
                grid[loc] = nearest_coords[0]
    counts = [sum([1 if x == i else 0 for x in grid.values()]) for i in range(len(coords)) if i not in blacklist]
    return max(counts)

if __name__ == '__main__':
    with open('input06.txt') as f:
        data = f.readlines()
    coords = load_coords(data)
    area = find_largest_area(coords)
    print(f'Day 06 - Part 1 - Answer: {area}')
    # print(f'Day 05 - Part 2 - Answer: {optimize(polymer)}')
