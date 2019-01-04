import re

def load_data(data):
    r = re.match(r'([0-9]+) players; last marble is worth ([0-9]+) points', data)
    return int(r.group(1)), int(r.group(2))

# TODO: Refactor, it's too slow
# rewrite with deque or with new class
def play(num_players, high_marble):
    circle = [0]
    players = [0] * num_players
    current_index = 0
    current_player = 0
    for m in range(1, high_marble + 1):
        if m % 23 == 0:
            current_index = (current_index - 7) % len(circle)
            m7 = circle.pop(current_index)
            players[current_player] = players[current_player] + m + m7
        else:
            current_index = (current_index + 2) % (len(circle))
            if current_index == 0:
                current_index = len(circle)
            circle.insert(current_index, m)
        current_player = (current_player + 1) % num_players
    return max(players)

if __name__ == '__main__':
    with open('input09.txt') as f:
        data = f.read()
    num_players, high_marble = load_data(data)
    high_score = play(num_players, high_marble)
    print(f'Day 09 - Part 1 - Answer: {high_score}')
    high_score = play(num_players, high_marble*100)
    print(f'Day 09 - Part 2 - Answer: {high_score}')

