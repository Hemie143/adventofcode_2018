import pytest

from adventofcode_2018 import day03


@pytest.fixture
def grid():
    return day03.load_grid(['#1 @ 1,3: 4x4',
                            '#2 @ 3,1: 4x4',
                            '#3 @ 5,5: 2x2'])


def test_day02(grid):
    assert day03.fabric_overlap(grid) == 4
    assert day03.find_claim(grid) == 3