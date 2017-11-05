from peewee import (CharField,
                    ForeignKeyField)

from .base import BaseModel
from .game import Game


class Player(BaseModel):
    """Represents a player playing the game."""
    game = ForeignKeyField(Game)
    name = CharField(max_length=10)
