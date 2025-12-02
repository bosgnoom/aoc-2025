from day02 import valid_id, main, read_input
from pathlib import Path


def test_invalid_ids():
    assert valid_id('55') == 55
    assert valid_id('6464') == 6464
    assert valid_id('123123') == 123123


def test_start_zero():
    assert valid_id('0101') == 101
    assert valid_id('101') == 0


def test_sample1():
    assert main(read_input(Path('02/sample01.txt')), 1) == 1227775554
