from day02 import read_input, valid_id2, main
from pathlib import Path


def test_invalid_id2s():
    assert valid_id2('12341234') == 12341234
    assert valid_id2('123123123') == 123123123
    assert valid_id2('1212121212') == 1212121212
    assert valid_id2('1111111') == 1111111


def test_start_zero_1():
    assert valid_id2('0101') == 0


def test_start_zero_2():
    assert valid_id2('101') == 0


def test_single_ranges_1():
    assert main(['11-22'], 2) == 11 + 22


def test_single_ranges_2():
    assert main(['95-115'], 2) == 99 + 111
    assert main(['998-1012'], 2) == 999 + 1010
    assert main(['1188511880-1188511890'], 2) == 1188511885
    assert main(['222220-222224'], 2) == 222222
    assert main(['1698522-1698528'], 2) == 0
    assert main(['446443-446449'], 2) == 446446
    assert main(['38593856-38593862'], 2) == 38593859
    assert main(['565653-565659'], 2) == 565656
    assert main(['824824821-824824827'], 2) == 824824824
    assert main(['2121212118-2121212124'], 2) == 2121212121


def test_sample1():
    assert main(read_input(Path('02/sample01.txt')), 2) == 4174379265
