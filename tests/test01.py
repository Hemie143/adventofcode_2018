import pytest

from adventofcode_2018 import day01


def test_day01():
    assert day01.run_day01([+1, -2, +3, +1])[0] == 3
    assert day01.run_day01([+1, +1, +1])[0] == 3
    assert day01.run_day01([+1, +1, -2])[0] == 0
    assert day01.run_day01([-1, -2, -3])[0] == -6

    assert day01.run_day01([+1, -2, +3, +1])[1] == 2
    assert day01.run_day01([+1, -1])[1] == 0
    assert day01.run_day01([+3, +3, +4, -2, -4])[1] == 10
    assert day01.run_day01([-6, +3, +8, +5, -6])[1] == 5
    assert day01.run_day01([+7, +7, -2, -7, -4])[1] == 14
