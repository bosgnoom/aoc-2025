from pathlib import Path

import logging
import coloredlogs

coloredlogs.install(level='INFO')
logger = logging.getLogger(__name__)


def read_input(filename: Path) -> list:
    """Reads from input file, strips newline characters

    :param filename: filename to read
    :type filename: Path
    :return: list of bank data
    :rtype: list
    """
    with open(filename, "r") as f:
        data = f.readlines()

    puzzle = [
        item.strip()
        for line in data
        for item in line.replace('\n', '').split(',')
        if item.strip() != '']

    logger.debug(puzzle)

    return puzzle


def joltage(bank: str) -> int:
    """Finds 2-figure joltage, by first looking for the largest digit at bank length - 1.
    Then finding that position and looking for the second part by looking from the first-found
    value to the last of the bank.

    :param bank: battery bank data
    :type bank: str
    :return: joltage
    :rtype: int
    """
    logger.debug(f'Bank: {bank}')

    left = bank[:-1]
    digits = list(map(int, left))
    max_tens = max(digits)
    max_pos = digits.index(max_tens)

    right = bank[max_pos + 1:]
    digits = list(map(int, right))
    max_ones = max(digits)

    joltage = 10 * max_tens + max_ones
    logger.debug(f'Found tens: {max_tens} and then {max_ones}, gives {joltage}')

    return joltage


def joltage2(bank: str) -> int:
    """Determines joltage for each bank, by selecting 12 batteries.
    Each battery is selected from the bank by setting up a "moving window", looking for
    the highest value battery.

    :param bank: Battery bank
    :type bank: str
    :return: Joltage
    :rtype: int
    """

    # Start position
    i = 0
    selected_digits = []
    required_digits = 12
    bank_length = len(bank)

    logger.debug(f'Bank: {bank}, {bank_length=}')

    # Loop over the bank, each time selecting a subset of the bank.
    # The end_index is used to keep 'space' to be able to select digits
    # to keep on filling the required digit length
    for end_index in range(bank_length - required_digits, bank_length):
        # Find the maximum digit by looking in the range where we picked the last
        # digit to the last possible digit (end_index)
        # With the range function we get the indexes for the bank
        # and by using the key keyword, we're looking into the actual digit of the bank
        i = max(range(i, end_index + 1), key=bank.__getitem__)

        # Add the digit to the collection
        selected_digits.append(bank[i])

        # Increase i by 1, to step to the next digit of the bank
        i = i + 1

    joltage = int(''.join(selected_digits))
    logger.debug(f'{joltage=} {selected_digits=}')
    return joltage


def main(puzzle: list, part: int) -> int:
    if part == 1:
        joltages = [joltage(bank) for bank in puzzle]
    else:
        joltages = [joltage2(bank) for bank in puzzle]
    return sum(joltages)


if __name__ == "__main__":  # pragma: no cover
    puzzle = read_input(Path("03/input.txt"))
    logger.info(f'Total part 1: {main(puzzle, 1)}')
    logger.info(f'Total part 2: {main(puzzle, 2)}')
