import pytest

from adventofcode_2018 import day07


@pytest.fixture
def steps_deps():
    return day07.load_steps('''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''.splitlines())


def test_day07(steps_deps):
    steps, deps = steps_deps
    assert day07.find_correct_order(steps, deps) == 'CABDFE'

