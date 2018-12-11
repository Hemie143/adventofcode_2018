
def load_coords(data):
    coords = []
    for d in data:
        r = re.match(r'[0-9]+, [0-9]+', d)
        x, y = r.group(1, 2)
        coords.append(x, y)
    return coords



if __name__ == '__main__':
    with open('input06.txt') as f:
        data = f.readlines()
    coords = load_coords(data)
    # polymer_reacted = react(polymer)
    # print(f'Day 05 - Part 1 - Answer: {len(polymer_reacted)}')
    # print(f'Day 05 - Part 2 - Answer: {optimize(polymer)}')


