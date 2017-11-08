from peewee import (CharField,
                    IntegerField)

from .base import BaseModel


class Level(BaseModel):
    """Represents a level within the game."""
    number = IntegerField()
    name = CharField(max_length=20)

    def __str__(self):
        return '<Level: {} ({})>'.format(self.number, self.name)
