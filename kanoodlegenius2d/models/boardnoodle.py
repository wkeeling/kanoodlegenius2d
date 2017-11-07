from peewee import ForeignKeyField

from .base import BaseModel
from .board import Board
from .noodle import Noodle


class BoardNoodle(BaseModel):
    """Represents an instance of a noodle on a player's board."""
    board = ForeignKeyField(Board, related_name='noodles')
    noodle = ForeignKeyField(Noodle)
