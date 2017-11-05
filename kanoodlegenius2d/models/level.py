from peewee import ForeignKeyField

from .base import BaseModel
from .game import Game


class Level(BaseModel):
    """Represents a level within the game."""
    game = ForeignKeyField(Game)
