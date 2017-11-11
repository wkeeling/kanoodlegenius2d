import logging

from .orientation import Orientation

_LOG = logging.getLogger(__name__)


def setup():
    # To avoid circular dependency
    from kanoodlegenius2d import models
    from kanoodlegenius2d.models import (BaseModel,
                                         Level,
                                         Noodle,
                                         Puzzle,
                                         PuzzleNoodle)
    # Create the tables if they do not already exist
    for k, v in vars(models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    Noodle.create(designation='A', colour='light_green',
                  part1=Orientation.E,
                  part2=Orientation.NE,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='B', colour='yellow',
                  part1=Orientation.E,
                  part2=Orientation.NE,
                  part3=Orientation.SE,
                  part4=Orientation.NE)
    Noodle.create(designation='C', colour='dark_blue',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NE,
                  part4=Orientation.NE)
    Noodle.create(designation='D', colour='light_blue',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='E', colour='red',
                  part1=Orientation.NE,
                  part2=Orientation.SE,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='F', colour='pink',
                  part1=Orientation.E,
                  part2=Orientation.NE,
                  part3=Orientation.SE,
                  part4=Orientation.E)
    Noodle.create(designation='G', colour='dark_green',
                  part1=Orientation.NE,
                  part2=Orientation.SE,
                  part3=Orientation.E,
                  part4=Orientation.NE)

    level1 = Level.create(number=1, name='Super Pro')
    level2 = Level.create(number=2, name='Champ')
    level3 = Level.create(number=3, name='Whiz')

    puzzle = Puzzle.create(level=level1, number=1)

    light_blue = Noodle.get(Noodle.colour == 'light_blue')
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    dark_green = Noodle.get(Noodle.colour == 'dark_green')
    puzzle.place(dark_green, position=9)

    light_green = Noodle.get(Noodle.colour == 'light_green')
    light_green.flip()
    light_green.rotate(increment=3)
    puzzle.place(light_green, position=15)

    red = Noodle.get(Noodle.colour == 'red')
    red.rotate()
    puzzle.place(red, position=20)


