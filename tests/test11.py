import pytest

from adventofcode_2018 import day11

@pytest.fixture
def grid_power():
    return day11.load_points()


def test_day11():
    assert day11.cell_pwr(3, 5, 8) == 4
    assert day11.cell_pwr(122, 79, 57) == -5
    assert day11.cell_pwr(217, 196, 39) == 0
    assert day11.cell_pwr(101, 153, 71) == 4

    assert day11.cell_pwr(33, 45, 18) == 4
    assert day11.cell_pwr(34, 45, 18) == 4
    assert day11.cell_pwr(35, 45, 18) == 4
    assert day11.cell_pwr(33, 46, 18) == 3
    assert day11.cell_pwr(34, 46, 18) == 3
    assert day11.cell_pwr(35, 46, 18) == 4
    assert day11.cell_pwr(33, 47, 18) == 1
    assert day11.cell_pwr(34, 47, 18) == 2
    assert day11.cell_pwr(35, 47, 18) == 4

    assert day11.select_cell(51, 3, 18) == (33, 45, 29)
    assert day11.select_cell(70, 3, 42) == (21, 61, 30)

    assert day11.select_cellsize(300, 18) == (90, 269, 16)
