
def cycle1(scores, recipe_indexes, recipe_count):
    while len(scores) < recipe_count + 10:
        new_recipes = list(str(sum([int(scores[e]) for e in recipe_indexes])))
        scores.extend(new_recipes)
        for i, e in enumerate(recipe_indexes):
            index = (e + 1 + int(scores[e])) % len(scores)
            recipe_indexes[i] = index
    scores_ten = ''.join(scores[recipe_count:recipe_count + 10])
    return scores_ten


def cycle2(scores, recipe_indexes, code):
    code = list(map(int, list(str(code))))
    code_len = len(code)
    while True:
        new_recipes = list(str(sum([scores[e] for e in recipe_indexes])))
        scores.extend([int(x) for x in new_recipes])
        for i, e in enumerate(recipe_indexes):                              # Time cost
            recipe_indexes[i] = (e + 1 + int(scores[e])) % len(scores)
        if scores[-code_len:] == code:
            return len(scores)-code_len
        if scores[-code_len-1:-1] == code:
            return len(scores)-code_len-1
    return


if __name__ == '__main__':
    recipes = 293801
    scores = cycle1(['3', '7'], [0, 1], recipes)
    print(f'Day 14 - Part 1 - Answer: {scores}')
    count = cycle2([3, 7], [0, 1], 293801)
    print(f'Day 14 - Part 2 - Answer: {count}')
