import pytest

from adventofcode_2018 import day06


@pytest.fixture
def coords():
    return day06.load_guards('''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''.splitlines())

def test_day06(coords):
    assert day06.find_sleepy_guard1(sleeps) == 10
