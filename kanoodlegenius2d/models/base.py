import logging
import os

from peewee import (Model,
                    SqliteDatabase)

import kanoodlegenius2d.models
from .orientation import Orientation

_LOG = logging.getLogger(__name__)

database = SqliteDatabase(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))


def initialise():
    """Initialise the database, creating the database tables if they don't already
    exist, and set up initial data.
    """
    from .noodle import Noodle
    from .level import Level
    from .puzzle import Puzzle
    global database
    database.connect()

    # Create the tables if they do not already exist
    for k, v in vars(kanoodlegenius2d.models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    Noodle.create(designation='A', code='light_green',
                  part1=Orientation.SE,
                  part2=Orientation.NE,
                  part3=Orientation.E,
                  part4=Orientation.NE)
    Noodle.create(designation='B', code='yellow',
                  part1=Orientation.NE,
                  part2=Orientation.NE,
                  part3=Orientation.SE,
                  part4=Orientation.NE)
    Noodle.create(designation='C', code='dark_blue',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NE,
                  part4=Orientation.NE)
    Noodle.create(designation='D', code='light_blue',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='E', code='red',
                  part1=Orientation.NE,
                  part2=Orientation.SE,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='G', code='dark_green',
                  part1=Orientation.NE,
                  part2=Orientation.SE,
                  part3=Orientation.E,
                  part4=Orientation.NE)
    Noodle.create(designation='F', code='pink',
                  part1=Orientation.NE,
                  part2=Orientation.NW,
                  part3=Orientation.E,
                  part4=Orientation.NE)

    level1 = Level.create(number=1, name='Super Pro')
    level2 = Level.create(number=2, name='Champ')
    level3 = Level.create(number=3, name='Whiz')

    puzzle = Puzzle.create(level=level1, number=1)
    light_blue = Noodle.get(Noodle.code == 'light_blue')
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)


def shutdown():
    """Shutdown the database, performing any cleanup operations and
    closing the active connection.
    """
    database.close()


class BaseModel(Model):
    """Base model that all concrete model classes should inherit from."""
    class Meta:
        database = database


class PositionUnavailableException(Exception):
    """Indicates that a position on the board is unavailable (in use by another noodle)."""
