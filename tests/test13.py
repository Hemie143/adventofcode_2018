import pytest

from adventofcode_2018 import day13

@pytest.fixture
def data1():
    map_data = '''/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/'''

    return day13.load_data(map_data)

@pytest.fixture
def data2():
    map_data = '''/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/'''

    return day13.load_data(map_data)


def test_day13(data1):
    circuit, carts = data1
    assert day13.cycle(circuit, carts)[0] == (7, 3)


def test_day13_2(data2):
    circuit, carts = data2
    assert day13.cycle(circuit, carts)[1] == (6, 4)
