from day03 import joltage, main, read_input
from pathlib import Path


def test_12345():
    assert joltage('12345') == 45


def test_sample01():
    assert joltage('987654321111111') == 98
    assert joltage('811111111111119') == 89
    assert joltage('234234234234278') == 78
    assert joltage('818181911112111') == 92


def test_total_sample01():
    assert main(read_input(Path('03/sample01.txt')), 1) == 357
