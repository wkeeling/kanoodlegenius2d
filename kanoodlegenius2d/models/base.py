import os

from peewee import (Model,
                    SqliteDatabase)


database = None


def initialise():
    """Initialise the database, creating the database tables if necessary
    and establish a connection.
    """
    global database
    database = SqliteDatabase(os.path.join(os.path.expanduser('~'),
                                           '.kanoodlegenius2d.db'))


def shutdown():
    """Shutdown the database, performing any cleanup operations and
    closing the active connection.
    """
    database.close()


class BaseModel(Model):
    """Base model that all concrete model classes should inherit from."""
    class Meta:
        database = database
