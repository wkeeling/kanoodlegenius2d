import logging

from kanoodlegenius2d.domain import orientation

_LOG = logging.getLogger(__name__)


def setup():
    # To avoid circular dependency
    from kanoodlegenius2d.domain import models
    from kanoodlegenius2d.domain.models import (BaseModel,
                                                Level,
                                                Noodle,
                                                Puzzle)
    # Create the tables if they do not already exist
    for k, v in vars(models).items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    Noodle.create(designation='A', colour='#00e600',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='B', colour='#ffff00',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.SE,
                  part4=orientation.NE)
    Noodle.create(designation='C', colour='#000099',
                  part1=orientation.E,
                  part2=orientation.E,
                  part3=orientation.NE,
                  part4=orientation.NE)
    Noodle.create(designation='D', colour='#00ccff',
                  part1=orientation.E,
                  part2=orientation.E,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='E', colour='#e60000',
                  part1=orientation.NE,
                  part2=orientation.SE,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='F', colour='#ff00ff',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.SE,
                  part4=orientation.E)
    Noodle.create(designation='G', colour='#004d00',
                  part1=orientation.NE,
                  part2=orientation.SE,
                  part3=orientation.E,
                  part4=orientation.NE)

    level1 = Level.create(number=1, name='Super Pro')
    level2 = Level.create(number=2, name='Champ')
    level3 = Level.create(number=3, name='Whiz')

    # Puzzle 1/1 ######################################

    puzzle = Puzzle.create(level=level1, number=1)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=9)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=3)
    puzzle.place(light_green, position=15)

    red = Noodle.red()
    red.rotate()
    puzzle.place(red, position=20)

    # Puzzle 2/1 ######################################

    puzzle = Puzzle.create(level=level1, number=2)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    light_blue = Noodle.light_blue()
    puzzle.place(light_blue, position=5)

    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=10)

    red = Noodle.red()
    puzzle.place(red, position=16)

    # Puzzle 3/1 ######################################

    puzzle = Puzzle.create(level=level1, number=3)

    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    light_green = Noodle.light_green()
    puzzle.place(light_green, position=11)

    pink = Noodle.pink()
    pink.rotate(increment=5)
    puzzle.place(pink, position=20)

    red = Noodle.red()
    red.rotate(increment=4)
    puzzle.place(red, position=32)

    # Puzzle 4/1 ######################################

    puzzle = Puzzle.create(level=level1, number=4)
    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=0)

    yellow = Noodle.yellow()
    yellow.rotate(increment=4)
    puzzle.place(yellow, position=17)

    pink = Noodle.pink()
    pink.rotate(increment=1)
    puzzle.place(pink, position=9)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=1)
    puzzle.place(dark_blue, position=20)

    # Puzzle 5/1 ######################################
    puzzle = Puzzle.create(level=level1, number=5)
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=5)
    puzzle.place(light_green, position=3)

    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=10)

    pink = Noodle.pink()
    pink.rotate(increment=5)
    puzzle.place(pink, position=27)

    # Puzzle 6/1 ######################################
    puzzle = Puzzle.create(level=level1, number=6)
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=4)
    puzzle.place(dark_blue, position=14)

    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=1)
    puzzle.place(light_blue, position=11)

    pink = Noodle.pink()
    pink.rotate(increment=4)
    puzzle.place(pink, position=25)

    # Puzzle 7/1 ######################################
    puzzle = Puzzle.create(level=level1, number=7)
    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=7)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=4)
    puzzle.place(dark_blue, position=14)

    yellow = Noodle.yellow()
    yellow.rotate(increment=3)
    puzzle.place(yellow, position=13)

    light_green = Noodle.light_green()
    light_green.rotate(increment=5)
    light_green.flip()
    puzzle.place(light_green, position=26)

    # Puzzle 8/1 ######################################
    puzzle = Puzzle.create(level=level1, number=8)
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=5)

    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=23)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=34)

    # Puzzle 9/1 ######################################
    puzzle = Puzzle.create(level=level1, number=9)
    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=7)

    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=12)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=20)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=5)
    puzzle.place(light_green, position=23)

    # Puzzle 10/1 ######################################
    puzzle = Puzzle.create(level=level1, number=10)
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=5)

    yellow = Noodle.yellow()
    yellow.rotate(increment=1)
    yellow.flip()
    puzzle.place(yellow, position=17)

    light_blue = Noodle.light_blue()
    puzzle.place(light_blue, position=31)

    # Puzzle 11/1 ######################################
    puzzle = Puzzle.create(level=level1, number=11)
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=17)

    yellow = Noodle.yellow()
    yellow.rotate(increment=1)
    puzzle.place(yellow, position=20)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=4)
    puzzle.place(light_blue, position=33)

    # Puzzle 12/1 ######################################
    puzzle = Puzzle.create(level=level1, number=12)
    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=7)

    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=12)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=20)

    red = Noodle.red()
    red.rotate(increment=3)
    puzzle.place(red, position=28)

    # Puzzle 13/1 ######################################
    puzzle = Puzzle.create(level=level1, number=13)
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=5)
    puzzle.place(pink, position=5)

    light_green = Noodle.light_green()
    puzzle.place(light_green, position=11)

    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=16)

    # Puzzle 14/1 ######################################
    puzzle = Puzzle.create(level=level1, number=14)
    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    puzzle.place(dark_green, position=12)

    pink = Noodle.pink()
    pink.rotate()
    puzzle.place(pink, position=9)

    dark_blue = Noodle.dark_blue()
    dark_blue.flip()
    puzzle.place(dark_blue, position=33)

    # Puzzle 15/1 ######################################
    puzzle = Puzzle.create(level=level1, number=15)
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=15)

    dark_green = Noodle.dark_green()
    dark_green.rotate(2)
    puzzle.place(dark_green, position=3)

    light_green = Noodle.light_green()
    light_green.rotate(increment=5)
    puzzle.place(light_green, position=30)

    # Puzzle 16/1 ######################################
    puzzle = Puzzle.create(level=level1, number=16)
    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=0)

    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=15)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=11)

    light_green = Noodle.light_green()
    light_green.rotate(increment=3)
    puzzle.place(light_green, position=17)

    # Puzzle 17/1 ######################################
    puzzle = Puzzle.create(level=level1, number=17)
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=17)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=24)

    yellow = Noodle.yellow()
    yellow.rotate()
    puzzle.place(yellow, position=20)

    # Puzzle 18/1 ######################################
    puzzle = Puzzle.create(level=level1, number=18)
    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=0)

    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=15)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=11)

    yellow = Noodle.yellow()
    puzzle.place(yellow, position=20)

    # Puzzle 19/1 ######################################
    puzzle = Puzzle.create(level=level1, number=19)
    red = Noodle.red()
    red.rotate(increment=2)
    puzzle.place(red, position=0)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=5)
    puzzle.place(light_blue, position=16)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=3)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=8)