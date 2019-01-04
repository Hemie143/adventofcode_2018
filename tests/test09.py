import pytest

from adventofcode_2018 import day09


@pytest.fixture
def data():
    return day09.load_data('9 players; last marble is worth 25 points')


def test_day08(data):
    num_players, high_marble = data
    assert day09.play(num_players, high_marble) == 32
    assert day09.play(10, 1618) == 8317
    assert day09.play(13, 7999) == 146373
    assert day09.play(17, 1104) == 2764
    assert day09.play(21, 6111) == 54718
    assert day09.play(30, 5807) == 37305
