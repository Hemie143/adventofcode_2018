
def scan23(ID):
    count2 = 0
    count3 = 0
    for c in ID:
        if ID.count(c) == 2:
            count2 = 1
        if ID.count(c) == 3:
            count3 = 1
    return count2, count3

def run_day02(IDs):
    counts = [scan23(i) for i in IDs]
    count2 = sum([c[0] for c in counts])
    count3 = sum([c[1] for c in counts])
    return count2*count3


if __name__ == '__main__':

    with open('input02.txt') as f:
        checksum = run_day02(f)
    print(f'Day 02 - Part 1 - Answer: {checksum}')
    # print(f'Day 01 - Part 2 - Answer: {}')

