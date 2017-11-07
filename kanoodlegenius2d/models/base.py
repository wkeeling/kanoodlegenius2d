import logging
import os

from peewee import (Model,
                    SqliteDatabase)

import kanoodlegenius2d.models
from .noodle import Noodle

_LOG = logging.getLogger(__name__)

database = SqliteDatabase(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))


def initialise():
    """Initialise the database, creating the database tables if they don't already
    exist, and set up initial data.
    """
    global database
    database.connect()

    # Create the tables if they do not already exist
    for k, v in vars(kanoodlegenius2d.models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    light_green = Noodle.create(name='light_green')
    dark_green = Noodle.create(name='dark_green')
    light_blue = Noodle.create(name='light_blue')
    dark_blue = Noodle.create(name='dark_blue')
    yellow = Noodle.create(name='yellow')
    red = Noodle.create(name='red')
    pink = Noodle.create(name='pink')



def shutdown():
    """Shutdown the database, performing any cleanup operations and
    closing the active connection.
    """
    database.close()


class BaseModel(Model):
    """Base model that all concrete model classes should inherit from."""
    class Meta:
        database = database
