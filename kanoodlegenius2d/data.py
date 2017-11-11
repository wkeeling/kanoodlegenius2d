import logging

from kanoodlegenius2d import orientation

_LOG = logging.getLogger(__name__)


def setup():
    # To avoid circular dependency
    from kanoodlegenius2d import models
    from kanoodlegenius2d.models import (BaseModel,
                                         Level,
                                         Noodle,
                                         Puzzle)
    # Create the tables if they do not already exist
    for k, v in vars(models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    Noodle.create(designation='A', colour='light_green',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='B', colour='yellow',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.SE,
                  part4=orientation.NE)
    Noodle.create(designation='C', colour='dark_blue',
                  part1=orientation.E,
                  part2=orientation.E,
                  part3=orientation.NE,
                  part4=orientation.NE)
    Noodle.create(designation='D', colour='light_blue',
                  part1=orientation.E,
                  part2=orientation.E,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='E', colour='red',
                  part1=orientation.NE,
                  part2=orientation.SE,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='F', colour='pink',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.SE,
                  part4=orientation.E)
    Noodle.create(designation='G', colour='dark_green',
                  part1=orientation.NE,
                  part2=orientation.SE,
                  part3=orientation.E,
                  part4=orientation.NE)

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


