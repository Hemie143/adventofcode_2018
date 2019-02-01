
def load_data(data):
    init_line, _, *rule_lines = data.splitlines()
    initial_state = init_line.split()[2]
    rules = dict([r.split(' => ') for r in rule_lines])
    return initial_state, rules


def life(state, rules, generations):
    null_index = 0
    for gen in range(1, generations+1):
        state = '....' + state + '....'
        next_state = []
        for i in range(0, len(state)):
            sample = state[i-2:i+3]
            next_state.append(rules.get(sample, '.'))
        state = ''.join(next_state)
        null_index += state.index('#') - 4
        state = state.strip('.')
    pot_sum = sum([i + null_index for i, p in enumerate(state) if p == '#'])
    return state, pot_sum


if __name__ == '__main__':
    with open('input12.txt') as f:
        data = f.read()

    initial_state, rules = load_data(data)
    state, pot_sum = life(initial_state, rules, 20)
    print(f'Day 12 - Part 1 - Answer: {pot_sum}')
    print(f'Day 12 - Part 1 - Answer: {pot_sum}')
    _, pot_sum_142 = life(initial_state, rules, 142)
    _, pot_sum_143 = life(initial_state, rules, 143)
    pot_sum = pot_sum_143 + (50000000000 - 143) * (pot_sum_143 - pot_sum_142)
    print(f'Day 12 - Part 2 - Answer: {pot_sum}')

