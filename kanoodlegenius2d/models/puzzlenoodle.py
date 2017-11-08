from peewee import (FixedCharField,
                    ForeignKeyField,
                    IntegerField)

from .base import BaseModel
from .noodle import Noodle
from .puzzle import Puzzle


class PuzzleNoodle(BaseModel):
    """Represents an instance of a Noodle preconfigured on a
    puzzle board.
    """
    puzzle = ForeignKeyField(Puzzle, related_name='noodles')
    noodle = ForeignKeyField(Noodle)
    # The position of the root part on the puzzle board
    position = IntegerField()
    # The orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)
