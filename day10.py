import re


def load_points(data):
    points = []
    for l in data.splitlines():
        r = re.findall(r'(-?[0-9]+)', l)
        points.append(tuple([int(i) for i in r]))
    return points


def limits(points):
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    return min_x, max_x, min_y, max_y


def display(points):
    min_x, max_x, min_y, max_y = limits(points)
    rows = []
    for y in range(min_y, max_y + 1):
        row2 = ['#' if (x, y) in points else '.' for x in range(min_x, max_x + 1)]
        rows.append(''.join(row2))
    return '\n'.join(rows)


def area(points):
    min_x, max_x, min_y, max_y = limits(points)
    return (max_x - min_x) * (max_y - min_y)

def play(points):
    t = 0
    prev_area = area(points)
    while True:
        t += 1
        snapshot = [(p[0] + t*p[2], p[1] + t*p[3]) for p in points]
        snap_area = area(snapshot)
        if snap_area > prev_area:
            message_time = t - 1
            break
        prev_area = snap_area
    return [(p[0] + message_time*p[2], p[1] + message_time*p[3]) for p in points], message_time


if __name__ == '__main__':
    with open('input10.txt') as f:
        data = f.read()

    points = load_points(data)
    msg, duration = play(points)
    print(f'Day 10 - Part 1 - Answer:\n{display(msg)}')
    print(f'Day 10 - Part 2 - Answer: {duration}')
