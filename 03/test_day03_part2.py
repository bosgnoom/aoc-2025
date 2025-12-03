from day03 import joltage2, main, read_input
from pathlib import Path


def test_sample01_1():
    assert joltage2('987654321111111') == 987654321111


def test_sample01_2():
    assert joltage2('811111111111119') == 811111111119


def test_sample01_3():
    assert joltage2('234234234234278') == 434234234278


def test_sample01_4():
    assert joltage2('818181911112111') == 888911112111


def test_total_sample01():
    assert main(read_input(Path('03/sample01.txt')), 2) == 3121910778619
