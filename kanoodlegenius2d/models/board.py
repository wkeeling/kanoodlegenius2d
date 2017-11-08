from peewee import ForeignKeyField

from .base import BaseModel
from .player import Player
from .puzzle import Puzzle


class Board(BaseModel):
    """Represents the board that a player is solving a puzzle on."""
    player = ForeignKeyField(Player, related_name='boards')
    puzzle = ForeignKeyField(Puzzle)

    def setup(self, puzzle):
        # Create a BoardNoodle based on each PuzzleNoode
        pass
