"""This module houses the logic for auto-solving a Kanoodle Genius puzzle."""

from kanoodlegenius2d.domain.models import Noodle


def solve(board):
    """Solve the puzzle using the Board instance supplied.

    Once solved, all the noodles will have been successfully
    placed on the board (the board will indicate it has been
    completed).

    Args:
        board: The Board instance.
    """
    noodles = set(Noodle.select()) - set([noodle.noodle for noodle in board.puzzle.noodles])