
def load_nodes(data):
    return [int(i) for i in data.split()]


def read_subnodes(tree):
    m_sum = 0
    num_childs = next(tree)
    num_metadatas = next(tree)
    subnodes = [read_subnodes(tree) for _ in range(num_childs)]
    metadata = [next(tree) for _ in range(num_metadatas)]
    return sum(metadata) + sum(subnodes)


if __name__ == '__main__':
    with open('input08.txt') as f:
        data = f.read()

    # data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    tree = load_nodes(data)
    m_sum = read_subnodes(iter(tree))
    print(f'Day 08 - Part 1 - Answer: {m_sum}')

    # print(f'Day 08 - Part 2 - Answer: {duration}')

