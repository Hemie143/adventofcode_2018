'''
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----
'''
def load_nodes(data):
    return [int(i) for i in data.split()]


def read_subnodes(tree):
    num_childs = next(tree)
    num_metadatas = next(tree)
    subnodes = [read_subnodes(tree) for _ in range(num_childs)]
    metadata = [next(tree) for _ in range(num_metadatas)]
    if num_childs == 0:
        node_value = sum(metadata)
    else:
        node_value = sum([subnodes[i-1][1] for i in metadata if 1 <= i <= len(subnodes)])
    return (sum(metadata) + sum([x[0] for x in subnodes]), node_value)


if __name__ == '__main__':
    with open('input08.txt') as f:
        data = f.read()

    tree = load_nodes(data)
    result = read_subnodes(iter(tree))
    print(f'Day 08 - Part 1 - Answer: {result[0]}')
    print(f'Day 08 - Part 2 - Answer: {result[1]}')

