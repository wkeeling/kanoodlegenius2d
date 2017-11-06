import logging
import os

from peewee import (Model,
                    SqliteDatabase)

import kanoodlegenius2d.models

_LOG = logging.getLogger(__name__)

database = SqliteDatabase(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))


def initialise():
    """Initialise the database, creating the database tables if necessary
    and establish a connection.
    """
    global database
    database.connect()
    for k, v in vars(kanoodlegenius2d.models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            v.create_table(fail_silently=True)  # Don't error if the tables already exist


def shutdown():
    """Shutdown the database, performing any cleanup operations and
    closing the active connection.
    """
    database.close()


class BaseModel(Model):
    """Base model that all concrete model classes should inherit from."""
    class Meta:
        database = database
