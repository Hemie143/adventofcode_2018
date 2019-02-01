import pytest

from adventofcode_2018 import day12

@pytest.fixture
def data():
    return day12.load_data('''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #''')


def test_day12(data):
    initial_state, rules = data
    assert day12.life(initial_state, rules, 20)[1] == 325
