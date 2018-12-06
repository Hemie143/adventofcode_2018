from difflib import SequenceMatcher


def scan23(ID):
    count2 = 0
    count3 = 0
    for c in ID:
        if ID.count(c) == 2:
            count2 = 1
        if ID.count(c) == 3:
            count3 = 1
    return count2, count3

def checksum(IDs):
    counts = [scan23(i) for i in IDs]
    count2 = sum([c[0] for c in counts])
    count3 = sum([c[1] for c in counts])
    return count2*count3


def correctIDs(IDs):
    best_score = 0
    for i, idA in enumerate(IDs):
        for idB in IDs[:i]:
            score = sum(list(map(lambda x,y: 1 if x==y else 0, idA, idB)))
            if score > best_score:
                id1 = idA
                id2 = idB
                best_score = score
    return ''.join([c for i, c in enumerate(id1) if id1[i]==id2[i] ])


if __name__ == '__main__':
    with open('input02.txt') as f:
        IDs = f.readlines()
    checksum = checksum(IDs)
    correctID = correctIDs(IDs)
    print(f'Day 02 - Part 1 - Answer: {checksum}')
    print(f'Day 02 - Part 2 - Answer: {correctID}')
