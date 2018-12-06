import pytest

from adventofcode_2018 import day02


def test_day02():
    assert day02.scan23('abcdef') == (0, 0)
    assert day02.scan23('bababc') == (1, 1)
    assert day02.scan23('abbcde') == (1, 0)
    assert day02.scan23('abcccd') == (0, 1)
    assert day02.scan23('aabcdd') == (1, 0)
    assert day02.scan23('abcdee') == (1, 0)
    assert day02.scan23('ababab') == (0, 1)

    assert day02.correctIDs(['abcde',
                                'fghij',
                                'klmno',
                                'pqrst',
                                'fguij',
                                'axcye',
                                'wvxyz',
                                 ]) == 'fgij'