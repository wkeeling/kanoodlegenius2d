from peewee import (ForeignKeyField,
                    IntegerField)

from .base import BaseModel
from .level import Level
from .puzzlenoodle import PuzzleNoodle


class Puzzle(BaseModel):
    """Represents a Kanoodle Genius puzzle, which is basically a
    board preconfigured with some noodles.
    """
    level = ForeignKeyField(Level, 'puzzles')
    number = IntegerField()

    def place(self, noodle, position):
        """Place a noodle onto the puzzle in the specified position.

        Args:
            noodle:
                The noodle instance to place on the puzzle.
            position:
                The position of the root part of the noodle on the puzzle.
        """
        PuzzleNoodle.create(puzzle=self, noodle=noodle, position=position, part1=noodle.part1,
                            part2=noodle.part2, part3=noodle.part3, part4=noodle.part4)
