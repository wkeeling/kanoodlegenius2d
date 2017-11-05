from peewee import ForeignKeyField

from .base import BaseModel
from .board import Board
from .noodle import Noodle


class PlayerNoodle(BaseModel):
    """Represents an instance of a noodle on a player's board."""
    board = ForeignKeyField(Board)
    noodle = ForeignKeyField(Noodle)
