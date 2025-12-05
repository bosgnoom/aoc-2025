from pathlib import Path
import logging
import coloredlogs
from tqdm import tqdm
import pprint

coloredlogs.install(level='INFO')
logger = logging.getLogger(__name__)


def read_input(filename: Path) -> tuple[list, list]:
    """Reads from input file, strips newline characters, 
    and returns list of fresh ID ranges and available IDs

    :param filename: filename to read
    :type filename: Path
    :return: two lists: fresh ID ranges and available IDs
    :rtype: list
    """
    with open(filename, "r") as f:
        data = f.readlines()

    fresh_ID_ranges = []
    available_IDs = []
    ID_switch = False

    for line in data:
        line = line.strip()
        if line == "":
            ID_switch = True
            continue

        if not ID_switch:
            fresh_ID_ranges.append([int(i) for i in line.split('-')])
        else:
            available_IDs.append(int(line))

    logger.debug("Puzzle input:")
    logger.debug(fresh_ID_ranges)
    logger.debug(available_IDs)

    return fresh_ID_ranges, available_IDs


def check_ID(ingredient_ID: int, fresh_ID_ranges: list) -> bool:
    """Check which ID is valid based on fresh ID ranges

    :param ingredient_ID: ID to check
    :type ingredient_ID: int
    :param fresh_ID_ranges: Ranges of valid IDs
    :type fresh_ID_ranges: list
    :return: True if ID is valid, False otherwise
    :rtype: bool
    """

    # Cover all ranges in fresh_ID_ranges
    ranges = [(start, end) for start, end in fresh_ID_ranges]

    for start, end in ranges:
        if start <= ingredient_ID <= end:
            logger.debug(f"ID {ingredient_ID} is valid in range {start}-{end}")
            return True

    logger.debug(f"ID {ingredient_ID} invalid")

    return False


def part1(fresh_ID_ranges: list, available_IDs: list) -> int:
    """
    Docstring for part1

    :param fresh_ID_ranges: Ranges of valid IDs
    :type fresh_ID_ranges: list
    :param available_IDs: Available IDs to check
    :type available_IDs: list
    :return: Amount of valid IDs
    :rtype: int
    """

    # Collect valid IDs
    valid_IDs = []

    # Loop over available IDs and check if they are valid
    for ingredient_ID in tqdm(available_IDs):
        if check_ID(ingredient_ID, fresh_ID_ranges):
            valid_IDs.append(ingredient_ID)

    logger.debug(f"Valid IDs: {valid_IDs}")
    logger.debug(f"Number of valid IDs: {len(valid_IDs)}")

    return len(valid_IDs)


def part2(fresh_ID_ranges: list):
    """
    Part 2 is way more difficult. This is because we cannot check each ID within min/max range
    of fresh_ID_ranges, as that would be too slow. Believe me, I tried.

    So we need to combine overlapping ranges first, then count the total number of IDs in the combined ranges.

    First sort the ranges by their starting ID.
    Then start checking adjacent ranges for overlap.
    If they overlap, combine them into a single range.
    If they don't overlap, add the current range to the list of combined ranges.

    :param fresh_ID_ranges: Description
    :type fresh_ID_ranges: list
    """
    # Sort here
    ranges = sorted(fresh_ID_ranges)

    # Now we can start combining overlapping ranges
    # Starting with the first range (which is now the lowest starting range)
    combined_ranges = [ranges[0]]

    # Loop over the remaining ranges
    for current_range in tqdm(ranges[1:]):
        # Get the last range
        last_range = combined_ranges[-1]

        # Check if the current range overlaps with the last combined range by checking
        # if the start of the current range is less than or equal to the end of the last range
        # e.g. 10-14 and 12-18 overlap because 12 <= 14
        if current_range[0] <= last_range[1]:
            # They overlap, so combine them. In this new range, the start is still the start of the last range,
            # but the end is the max of the two ends
            new_range = [last_range[0], max(last_range[1], current_range[1])]

            # Update the last range in the combined ranges list
            combined_ranges[-1] = new_range

            logger.debug(f"Combined {last_range} and {current_range} into {new_range}")
        else:
            # They don't overlap, so add the current range to the list
            combined_ranges.append(current_range)

            logger.debug(f"No overlap between {last_range} and {current_range}. "
                         f"Added {current_range} to combined ranges.")

    logger.debug(f"Combined ranges: {combined_ranges}")

    # Now count the total number of IDs in the combined ranges
    total_IDs = 0
    for start, end in combined_ranges:
        total_IDs += end - start + 1  # +1 because ranges are inclusive (yes... messed that one up initially)

    logger.debug(f"Total number of valid IDs in combined ranges: {total_IDs}")

    return total_IDs


if __name__ == "__main__":  # pragma: no cover
    # fresh_ID_ranges, available_IDs = read_input(Path("05/sample01.txt"))
    fresh_ID_ranges, available_IDs = read_input(Path("05/input.txt"))

    logger.info(f'Valid ingredient IDs found in part 1: {part1(fresh_ID_ranges, available_IDs)}')
    logger.info(f"Total number of valid IDs in combined ranges: {part2(fresh_ID_ranges)}")
