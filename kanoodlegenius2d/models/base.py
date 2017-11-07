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
    global database
    database.connect()

    # Create the tables if they do not already exist
    for k, v in vars(kanoodlegenius2d.models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    light_green = Noodle.create(name='light_green', part1=Orientation.SE, part2=Orientation.NE, part3=Orientation.E,
                                part4=Orientation.NE)
    dark_green = Noodle.create(name='dark_green', part1=Orientation.NE, part2=Orientation.SE, part3=Orientation.E,
                               part4=Orientation.NE)
    light_blue = Noodle.create(name='light_blue', part1=Orientation.SE, part2=Orientation.NE, part3=Orientation.E,
                               part4=Orientation.E)
    dark_blue = Noodle.create(name='dark_blue', part1=Orientation.E, part2=Orientation.E, part3=Orientation.NE,
                              part4=Orientation.NE)
    yellow = Noodle.create(name='yellow', part1=Orientation.NE, part2=Orientation.NE, part3=Orientation.SE,
                           part4=Orientation.NE)
    red = Noodle.create(name='red', part1=Orientation.NE, part2=Orientation.SE, part3=Orientation.NE,
                        part4=Orientation.SE)
    pink = Noodle.create(name='pink', part1=Orientation.NE, part2=Orientation.NW, part3=Orientation.E,
                         part4=Orientation.NE)


def shutdown():
    """Shutdown the database, performing any cleanup operations and
    closing the active connection.
    """
    database.close()


class BaseModel(Model):
    """Base model that all concrete model classes should inherit from."""
    class Meta:
        database = database
