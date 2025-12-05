from pathlib import Path
from day04 import read_input, count_neighbours, main, draw_map
import pytest

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"


def test_count_neighbours():
    puzzle = read_input(Path("04/sample01.txt"))

    assert len(count_neighbours(puzzle)) == 13


@pytest.fixture
def sample_puzzle():
    return read_input(Path("04/sample01.txt"))


def test_main(sample_puzzle):
    assert main(sample_puzzle, SHOW=False) == 43


def test_draw_map(sample_puzzle):
    """Just test if draw_map runs without errors."""
    import pygame

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('freemono', size=20)
    size_x = 20 * len(sample_puzzle[0])
    size_y = 20 * len(sample_puzzle)
    screen = pygame.display.set_mode([size_x, size_y])

    sample_puzzle[0][0] = "x"  # Mark one cell to see if it draws differently

    draw_map(screen, font, sample_puzzle)

    pygame.quit()
