from peewee import ForeignKeyField

from .base import BaseModel
from .noodle import Noodle
from .puzzle import Puzzle


class PuzzleNoodle(BaseModel):
    """Represents an instance of a Noodle preconfigured on a
    puzzle board.
    """
    puzzle = ForeignKeyField(Puzzle)
    noodle = ForeignKeyField(Noodle)