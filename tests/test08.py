import pytest

from adventofcode_2018 import day08


@pytest.fixture
def nodes():
    return day08.load_nodes('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2')


def test_day08(nodes):
    assert day08.read_subnodes(iter(nodes))[0] == 138
    assert day08.read_subnodes(iter(nodes))[1] == 66
