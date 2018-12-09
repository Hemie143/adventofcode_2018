import pytest

from adventofcode_2018 import day05


def test_day05():
    assert day05.react('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'
    assert day05.optimize('dabAcCaCBAcCcaDA') == 4
