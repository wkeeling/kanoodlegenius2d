from peewee import ForeignKeyField

from .base import BaseModel
from .level import Level


class Puzzle(BaseModel):
    """Represents a Kanoodle Genius puzzle, which is basically a
    board preconfigured with some noodles.
    """
    level = ForeignKeyField(Level)
