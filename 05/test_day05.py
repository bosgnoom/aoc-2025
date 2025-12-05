from pathlib import Path
from day05 import read_input, check_ID, part1, part2
import pytest


@pytest.fixture
def puzzle():
    return read_input(Path("05/sample01.txt"))


cases = {
    1: False,
    5: True,
    8: False,
    11: True,
    17: True,
    32: False,
}


@pytest.mark.parametrize("id_value, expected", cases.items())
def test_IDs(puzzle, id_value, expected):
    assert check_ID(id_value, puzzle[0]) is expected


def test_part1(puzzle):
    assert part1(puzzle[0], puzzle[1]) == 3


def test_part2(puzzle):
    assert part2(puzzle[0]) == 14
