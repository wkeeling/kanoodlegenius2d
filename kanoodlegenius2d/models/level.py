from peewee import (CharField,
                    ForeignKeyField,
                    IntegerField)

from .base import BaseModel
from .game import Game


class Level(BaseModel):
    """Represents a level within the game."""
    game = ForeignKeyField(Game, related_name='levels')
    number = IntegerField()
    name = CharField(max_length=20)

    def __str__(self):
        return '<Level: {} ({})>'.format(self.number, self.name)
