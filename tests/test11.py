import pytest

from adventofcode_2018 import day11

@pytest.fixture
def grid_power():
    return day11.generate_summed_area(300, 8)


def test_day11(grid_power):

    assert day11.select_square(day11.generate_summed_area(300, 18), 300, 3) == (29, 33, 45)
    assert day11.select_square(day11.generate_summed_area(300, 42), 300, 3) == (30, 21, 61)

    assert day11.select_squaresize(day11.generate_summed_area(300, 18), 300) == ((113, 90, 269), 16)
    assert day11.select_squaresize(day11.generate_summed_area(300, 42), 300) == ((119, 232, 251), 12)
