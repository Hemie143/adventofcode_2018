import pytest

from adventofcode_2018 import day11

@pytest.fixture
def grid_power():
    return day11.generate_grid(300, 8)


def test_day11(grid_power):

    assert grid_power[(3, 5)] == 4
    assert day11.generate_grid(300, 57)[(122, 79)] == -5
    assert day11.generate_grid(300, 39)[(217, 196)] == 0
    assert day11.generate_grid(300, 71)[(101, 153)] == 4

    assert day11.select_square(day11.generate_grid(300, 18), 300, 3) == (29, 33, 45)
    assert day11.select_square(day11.generate_grid(300, 42), 300, 3) == (30, 21, 61)
    '''
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
    '''