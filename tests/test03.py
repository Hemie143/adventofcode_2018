import pytest

from adventofcode_2018 import day03


def test_day02():
    assert day03.fabric_overlap(['#1 @ 1,3: 4x4',
                                 '#2 @ 3,1: 4x4',
                                 '#3 @ 5,5: 2x2']) == 4
