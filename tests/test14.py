import pytest

from adventofcode_2018 import day14

def test_day14():
    assert day14.cycle1([3, 7], [0, 1], 9) == '5158916779'
    assert day14.cycle1([3, 7], [0, 1], 5) == '0124515891'
    assert day14.cycle1([3, 7], [0, 1], 18) == '9251071085'
    assert day14.cycle1([3, 7], [0, 1], 2018) == '5941429882'

    assert day14.cycle2([3, 7], [0, 1], 5) == 9
    assert day14.cycle2([3, 7], [0, 1], 9) == 13
    assert day14.cycle2([3, 7], [0, 1], 18) == 48
    assert day14.cycle2([3, 7], [0, 1], 2018) == 86764
