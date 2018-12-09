import pytest

from adventofcode_2018 import day04


@pytest.fixture
def sleeps():
    return day04.load_guards('''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''.splitlines())

def test_day04(sleeps):
    assert day04.find_sleepy_guard1(sleeps) == 10
    assert day04.most_sleep_minute(sleeps[10]) == 24
    assert day04.find_sleepy_guard2(sleeps) == 99
    assert day04.most_sleep_minute(sleeps[99]) == 45
