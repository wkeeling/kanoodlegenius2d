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
    Noodle.create(designation='A', colour='#00e600', image='light_green_sphere.png',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='B', colour='#ffff00', image='yellow_sphere.png',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.SE,
                  part4=orientation.NE)
    Noodle.create(designation='C', colour='#000099', image='dark_blue_sphere.png',
                  part1=orientation.E,
                  part2=orientation.E,
                  part3=orientation.NE,
                  part4=orientation.NE)
    Noodle.create(designation='D', colour='#00ccff', image='light_blue_sphere.png',
                  part1=orientation.E,
                  part2=orientation.E,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='E', colour='#e60000', image='red_sphere.png',
                  part1=orientation.NE,
                  part2=orientation.SE,
                  part3=orientation.NE,
                  part4=orientation.SE)
    Noodle.create(designation='F', colour='#ff00ff', image='pink_sphere.png',
                  part1=orientation.E,
                  part2=orientation.NE,
                  part3=orientation.SE,
                  part4=orientation.E)
    Noodle.create(designation='G', colour='#004d00', image='dark_green_sphere.png',
                  part1=orientation.NE,
                  part2=orientation.SE,
                  part3=orientation.E,
                  part4=orientation.NE)

    level1 = Level.create(number=1, name='Super Pro')
    level2 = Level.create(number=2, name='Champ')
    level3 = Level.create(number=3, name='Whiz')

    # Puzzle 1/1 ######################################

    puzzle = Puzzle.create(
        level=level1,
        number=1,
        solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;2,17,NE,E,NW,E'
    )

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

    puzzle = Puzzle.create(
        level=level1,
        number=2,
        solution='6,31,E,NE,SE,E;1,30,NE,NW,NW,E;7,24,SW,NW,W,SW')

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

    puzzle = Puzzle.create(
        level=level1,
        number=3,
        solution='3,13,SW,SW,SE,SE;4,33,NW,NW,NE,W;2,14,SW,SE,W,SE')

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

    puzzle = Puzzle.create(
        level=level1,
        number=4,
        solution='1,22,SE,E,E,SW;7,14,NW,SW,W,NW;5,23,NE,SE,NE,SE'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=5,
        solution='4,31,E,E,NE,SE;7,25,SW,NW,W,SW;5,8,SE,W,SE,W'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=6,
        solution='7,32,NE,SE,E,NE;2,22,NW,W,NE,W;5,20,E,SW,E,SW'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=7,
        solution='6,31,E,NE,SE,E;7,21,SE,NE,E,SE;5,18,E,SW,E,SW',
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=8,
        solution='1,11,NE,E,E,NW;2,14,W,SW,NW,SW;5,19,SE,W,SE,W'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=9,
        solution='3,14,NW,NW,W,W;2,32,E,NE,SE,NE;5,25,W,NE,W,NE'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=10,
        solution='1,11,NE,E,E,NW;7,25,SW,NW,W,SW;5,14,SW,NW,SW,NW'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=11,
        solution='3,14,NW,NW,W,W;6,25,NW,W,NE,NW;5,23,E,SW,E,SW'
    )
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=9)

    yellow = Noodle.yellow()
    yellow.rotate(increment=1)
    puzzle.place(yellow, position=20)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=4)
    puzzle.place(light_blue, position=33)

    # Puzzle 12/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=12,
        solution='3,14,NW,NW,W,W;1,18,SW,SE,SE,W;2,13,SE,SW,E,SW'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=13,
        solution='3,32,E,E,NE,NE;4,29,NE,NE,NW,E;5,28,NW,E,NW,E'
    )
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=5)
    puzzle.place(pink, position=20)

    light_green = Noodle.light_green()
    puzzle.place(light_green, position=11)

    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=16)

    # Puzzle 14/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=14,
        solution='1,22,SE,E,E,SW;2,25,W,NW,SW,NW;5,7,E,SW,E,SW'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=15,
        solution='6,17,SE,E,SW,SE;4,16,SE,SE,SW,E;5,20,E,SW,E,SW'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=16,
        solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;2,31,NE,E,NW,E'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=17,
        solution='3,14,NW,NW,W,W;6,25,NW,W,NE,NW;5,30,SW,NW,SW,NW'
    )
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=9)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=24)

    yellow = Noodle.yellow()
    yellow.rotate()
    puzzle.place(yellow, position=20)

    # Puzzle 18/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=18,
        solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;1,23,SW,W,W,SE'
    )
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
    puzzle = Puzzle.create(
        level=level1,
        number=19,
        solution='3,20,SE,SE,E,E;7,34,NE,W,NW,NE;2,15,SE,E,SW,E'
    )
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

    # Puzzle 20/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=20,
        solution='7,32,NE,SE,E,NE;2,22,NW,W,NE,W;5,20,E,SW,E,SW'
    )
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=4)
    puzzle.place(dark_blue, position=14)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=4)
    puzzle.place(light_blue, position=7)

    pink = Noodle.pink()
    pink.rotate()
    puzzle.place(pink, position=11)

    # Puzzle 21/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=21,
        solution='4,16,SE,SE,SW,E;7,34,NE,W,NW,NE;5,20,E,SW,E,SW'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=15)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=3)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=8)

    # Puzzle 22/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=22,
        solution='6,31,E,NE,SE,E;7,21,SE,NE,E,SE;2,13,SE,SW,E,SW'
    )
    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=7)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=4)
    puzzle.place(dark_blue, position=14)

    red = Noodle.red()
    puzzle.place(red, position=16)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=1)
    puzzle.place(light_green, position=26)

    # Puzzle 23/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=23,
        solution='3,32,E,E,NE,NE;4,29,W,W,SW,NW;2,24,W,NW,SW,NW'
    )
    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=3)

    light_green = Noodle.light_green()
    light_green.rotate(increment=2)
    puzzle.place(light_green, position=4)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=10)

    red = Noodle.red()
    red.rotate(increment=2)
    puzzle.place(red, position=8)

    # Puzzle 24/1 ######################################
    puzzle = Puzzle.create(
        level=level1,
        number=24,
        solution='3,20,SE,SE,E,E;6,17,SE,E,SW,SE;2,15,SE,E,SW,E'
    )
    red = Noodle.red()
    red.rotate(increment=2)
    puzzle.place(red, position=0)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=5)
    puzzle.place(light_blue, position=16)

    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=2)
    puzzle.place(dark_green, position=3)

    light_green = Noodle.light_green()
    light_green.rotate(increment=5)
    puzzle.place(light_green, position=30)

    # Puzzle 1/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=1,
        solution='6,20,NE,NW,E,NE;1,22,E,SE,SE,NE;4,26,NE,NE,E,NW;5,31,NE,SE,NE,SE'
    )
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=2)
    puzzle.place(dark_blue, position=3)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=1)
    puzzle.place(yellow, position=25)

    # Puzzle 2/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=2,
        solution='1,22,SE,E,E,SW;4,10,E,E,SE,NE;7,25,NW,SW,W,NW;2,14,NW,W,NE,W'
    )
    red = Noodle.red()
    puzzle.place(red, position=4)

    pink = Noodle.pink()
    pink.rotate()
    puzzle.place(pink, position=9)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=1)
    puzzle.place(dark_blue, position=20)

    # Puzzle 3/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=3,
        solution='6,24,NW,W,NE,NW;1,22,E,SE,SE,NE;7,15,E,SW,SE,E;2,25,NW,NE,W,NE'
    )
    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=0)

    red = Noodle.red()
    puzzle.place(red, position=9)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=1)
    puzzle.place(dark_blue, position=20)

    # Puzzle 4/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=4,
        solution='1,11,NE,E,E,NW;4,21,E,E,NE,SE;7,14,SW,NW,W,SW;2,25,SW,W,SE,W'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=5)

    red = Noodle.red()
    red.rotate(increment=3)
    puzzle.place(red, position=28)

    # Puzzle 5/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=5,
        solution='3,31,NE,NE,NW,NW;6,14,SW,SE,W,SW;4,8,SW,SW,W,SE;7,32,NE,SE,E,NE'
    )
    light_green = Noodle.light_green()
    light_green.flip()
    puzzle.place(light_green, position=12)

    red = Noodle.red()
    red.rotate(increment=3)
    puzzle.place(red, position=3)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=4)
    puzzle.place(yellow, position=9)

    # Puzzle 6/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=6,
        solution='3,32,E,E,NE,NE;6,20,E,NE,SE,E;4,29,W,W,SW,NW;5,24,NW,E,NW,E'
    )
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=3)
    puzzle.place(yellow, position=1)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=9)

    # Puzzle 7/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=7,
        solution='6,31,NE,NW,E,NE;4,18,SW,SW,SE,W;2,19,NW,W,NE,W;5,34,NW,E,NW,E'
    )
    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=4)
    puzzle.place(dark_green, position=0)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=4)
    puzzle.place(dark_blue, position=14)

    light_green = Noodle.light_green()
    light_green.rotate(increment=5)
    light_green.flip()
    puzzle.place(light_green, position=26)

    # Puzzle 8/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=8,
        solution='1,11,NE,E,E,NW;4,12,SW,SW,W,SE;2,23,NE,E,NW,E;5,34,NW,E,NW,E'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=5)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    puzzle.place(dark_green, position=33)

    # Puzzle 9/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=9,
        solution='3,32,E,E,NE,NE;4,29,W,W,SW,NW;2,24,NE,NW,E,NW;5,18,SW,NW,SW,NW'
    )
    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=3)

    light_green = Noodle.light_green()
    light_green.rotate(increment=2)
    puzzle.place(light_green, position=4)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=10)

    # Puzzle 10/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=10,
        solution='1,11,NE,E,E,NW;4,32,NE,NE,E,NW;7,14,SW,NW,W,SW;2,25,SW,W,SE,W'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=2)
    puzzle.place(pink, position=5)

    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=31)

    # Puzzle 11/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=11,
        solution='3,34,NE,NE,NW,NW;1,16,SE,E,E,SW;4,1,SE,SE,SW,E;2,14,NW,W,NE,W'
    )
    red = Noodle.red()
    red.rotate(increment=4)
    puzzle.place(red, position=11)

    pink = Noodle.pink()
    pink.rotate(increment=4)
    puzzle.place(pink, position=27)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    puzzle.place(dark_green, position=33)

    # Puzzle 12/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=12,
        solution='6,14,W,SW,NW,W;4,5,E,E,NE,SE;7,25,NW,SW,W,NW;5,30,SW,NW,SW,NW'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=10)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=16)

    # Puzzle 13/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=13,
        solution='3,32,E,E,NE,NE;6,7,SW,SE,W,SW;1,31,NE,E,E,NW;2,24,NE,NW,E,NW'
    )
    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=9)

    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=26)

    # Puzzle 14/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=14,
        solution='6,14,SW,SE,W,SW;1,23,W,SW,SW,NW;7,32,NE,SE,E,NE;5,2,E,SW,E,SW'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=5)
    puzzle.place(yellow, position=20)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=5)
    puzzle.place(dark_blue, position=21)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=4)
    puzzle.place(light_blue, position=1)

    # Puzzle 15/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=15,
        solution='3,20,SE,SE,E,E;6,7,SE,E,SW,SE;4,27,E,E,SE,NE;5,24,W,NE,W,NE'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=0)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=1)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=5)

    # Puzzle 16/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=16,
        solution='6,14,SW,SE,W,SW;7,32,NE,SE,E,NE;2,18,NE,NW,E,NW;5,6,SE,W,SE,W'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=2)
    puzzle.place(light_blue, position=5)

    light_green = Noodle.light_green()
    light_green.rotate(increment=3)
    puzzle.place(light_green, position=23)

    # Puzzle 17/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=17,
        solution='3,14,NW,NW,W,W;6,11,SE,E,SW,SE;4,34,W,W,NW,SW;2,13,SE,SW,E,SW'
    )
    light_green = Noodle.light_green()
    light_green.rotate(increment=1)
    puzzle.place(light_green, position=0)

    red = Noodle.red()
    red.rotate(increment=4)
    puzzle.place(red, position=16)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=20)

    # Puzzle 18/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=18,
        solution='6,27,NE,NW,E,NE;1,11,NE,E,E,NW;2,23,NE,E,NW,E;5,34,NW,E,NW,E'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=2)
    puzzle.place(light_blue, position=5)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    puzzle.place(dark_green, position=33)

    # Puzzle 19/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=19,
        solution='6,23,NW,W,NE,NW;1,22,SE,E,E,SW;4,27,NW,NW,NE,W;2,12,SE,E,SW,E'
    )
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    red = Noodle.red()
    red.rotate(increment=4)
    puzzle.place(red, position=14)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=1)
    puzzle.place(dark_blue, position=20)

    # Puzzle 20/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=20,
        solution='6,5,SW,SE,W,SW;4,34,W,W,NW,SW;7,23,SW,NW,W,SW;5,19,SE,W,SE,W'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=5)
    puzzle.place(yellow, position=3)

    light_green = Noodle.light_green()
    puzzle.place(light_green, position=17)

    # Puzzle 21/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=21,
        solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;1,23,SW,W,W,SE;2,17,NE,E,NW,E'
    )
    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    dark_green = Noodle.dark_green()
    puzzle.place(dark_green, position=9)

    red = Noodle.red()
    puzzle.place(red, position=20)

    # Puzzle 22/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=22,
        solution='3,20,SE,SE,E,E;1,34,NW,W,W,NE;2,14,SW,SE,W,SE;5,18,NW,E,NW,E'
    )
    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=3)

    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=4)
    puzzle.place(light_blue, position=23)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=1)
    puzzle.place(dark_green, position=21)

    # Puzzle 23/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=23,
        solution='3,32,E,E,NE,NE;1,7,SW,SE,SE,W;4,29,W,W,SW,NW;5,11,SE,W,SE,W'
    )
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=4)
    puzzle.place(yellow, position=3)

    pink = Noodle.pink()
    pink.rotate(increment=5)
    puzzle.place(pink, position=20)

    # Puzzle 24/2 ######################################
    puzzle = Puzzle.create(
        level=level2,
        number=24,
        solution='6,7,SE,E,SW,SE;1,23,W,SW,SW,NW;4,30,NW,NW,W,NE;5,32,NE,SE,NE,SE'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=5)
    puzzle.place(yellow, position=20)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=5)
    puzzle.place(dark_blue, position=21)

    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    dark_green.flip()
    puzzle.place(dark_green, position=1)

    # Puzzle 1/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=1,
        solution='3,20,SE,SE,E,E;1,22,SE,E,E,SW;4,27,NW,NW,NE,W;2,12,SE,E,SW,E;5,14,W,NE,W,NE'
    )
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    pink = Noodle.pink()
    pink.rotate(increment=4)
    puzzle.place(pink, position=23)

    # Puzzle 2/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=2,
        solution='3,20,SE,SE,E,E;1,8,SE,SW,SW,E;4,27,E,E,SE,NE;7,13,NW,SW,W,NW;5,18,SW,NW,SW,NW'
    )
    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=3)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=1)
    puzzle.place(yellow, position=21)

    # Puzzle 3/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=3,
        solution='3,20,SE,SE,E,E;1,22,SE,E,E,SW;4,1,SE,SE,E,SW;7,25,NW,SW,W,NW;2,14,NW,W,NE,W'
    )
    red = Noodle.red()
    red.rotate(increment=4)
    puzzle.place(red, position=11)

    pink = Noodle.pink()
    pink.rotate(increment=1)
    puzzle.place(pink, position=9)

    # Puzzle 4/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=4,
        solution='3,32,E,E,NE,NE;1,4,SW,SE,SE,W;7,31,NW,E,NE,NW;2,19,SW,W,SE,W;5,14,W,NE,W,NE'
    )
    pink = Noodle.pink()
    pink.rotate(increment=4)
    puzzle.place(pink, position=17)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=1)
    puzzle.place(light_blue, position=18)

    # Puzzle 5/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=5,
        solution='3,14,NW,NW,W,W;6,27,NW,W,NE,NW;1,29,NW,NE,NE,W;7,33,NW,SW,W,NW;2,34,NE,NW,E,NW'
    )
    light_blue = Noodle.light_blue()
    light_blue.flip()
    puzzle.place(light_blue, position=7)

    red = Noodle.red()
    red.rotate(increment=1)
    puzzle.place(red, position=10)

    # Puzzle 6/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=6,
        solution='6,17,NE,NW,E,NE;1,24,W,SW,SW,NW;7,16,SE,W,SW,SE;2,25,SW,W,SE,W;5,8,SE,W,SE,W'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=2)
    puzzle.place(light_blue, position=20)

    # Puzzle 7/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=7,
        solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;1,23,SW,W,W,SE;7,20,NE,SE,E,NE;5,3,SE,W,SE,W'
    )
    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=9)

    light_blue = Noodle.light_blue()
    light_blue.flip()
    light_blue.rotate(increment=5)
    puzzle.place(light_blue, position=2)

    # Puzzle 8/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=8,
        solution='3,14,NW,NW,W,W;6,31,E,NE,SE,E;4,11,SE,SE,E,SW;7,13,SW,E,SE,SW;5,16,SE,W,SE,W'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=5)
    puzzle.place(yellow, position=20)

    light_green = Noodle.light_green()
    light_green.rotate(increment=1)
    puzzle.place(light_green, position=0)

    # Puzzle 9/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=9,
        solution='6,31,E,NE,SE,E;1,3,SW,W,W,SE;4,12,SW,SW,W,SE;2,25,NW,NE,W,NE;5,30,W,NE,W,NE'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=2)
    puzzle.place(dark_green, position=10)

    # Puzzle 10/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=10,
        solution='3,20,SE,SE,E,E;1,8,SE,SW,SW,E;4,27,E,E,SE,NE;7,13,NW,SW,W,NW;2,21,E,NE,SE,NE'
    )
    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=3)

    red = Noodle.red()
    red.rotate(increment=4)
    puzzle.place(red, position=16)

    # Puzzle 11/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=11,
        solution='3,32,E,E,NE,NE;6,7,SW,SE,W,SW;1,23,SW,W,W,SE;4,29,NE,NE,NW,E;7,1,SE,NE,E,SE'
    )
    red = Noodle.red()
    red.rotate(increment=2)
    puzzle.place(red, position=0)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=5)
    puzzle.place(yellow, position=11)

    # Puzzle 12/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=12,
        solution='3,32,E,E,NE,NE;1,4,SW,SE,SE,W;4,29,W,W,SW,NW;7,24,NW,SW,W,NW;2,3,SE,SW,E,SW'
    )
    pink = Noodle.pink()
    pink.rotate(increment=4)
    puzzle.place(pink, position=17)

    red = Noodle.red()
    red.rotate(increment=1)
    puzzle.place(red, position=1)

    # Puzzle 13/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=13,
        solution='6,31,E,NE,SE,E;1,30,NE,NW,NW,E;4,5,E,E,NE,SE;7,24,SW,NW,W,SW;2,10,E,SE,NE,SE'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=26)

    # Puzzle 14/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=14,
        solution='6,14,SW,SE,W,SW;1,18,SW,W,W,SE;4,2,SW,SW,SE,W;7,32,NE,SE,E,NE;5,3,SE,W,SE,W'
    )
    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=9)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=2)
    puzzle.place(dark_blue, position=10)

    # Puzzle 15/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=15,
        solution='3,14,NW,NW,W,W;6,25,NW,W,NE,NW;4,31,E,E,NE,SE;7,22,SE,NE,E,SE;5,27,W,NE,W,NE'
    )
    light_green = Noodle.light_green()
    light_green.rotate(increment=4)
    puzzle.place(light_green, position=12)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=3)
    puzzle.place(yellow, position=9)

    # Puzzle 16/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=16,
        solution='3,14,NW,NW,W,W;6,25,NW,W,NE,NW;4,34,W,W,NW,SW;7,20,SE,NE,E,SE;2,17,SE,E,SW,E'
    )
    red = Noodle.red()
    red.rotate(increment=2)
    puzzle.place(red, position=0)

    light_green = Noodle.light_green()
    puzzle.place(light_green, position=15)

    # Puzzle 17/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=17,
        solution='6,14,W,SW,NW,W;1,22,SE,E,E,SW;4,5,E,E,NE,SE;7,25,NW,SW,W,NW;2,33,W,NW,SW,NW'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    red = Noodle.red()
    red.rotate(increment=2)
    puzzle.place(red, position=10)

    # Puzzle 18/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=18,
        solution='3,20,SE,SE,E,E;6,3,SW,SE,W,SW;1,8,SE,SW,SW,E;4,27,E,E,SE,NE;7,21,NE,SE,E,NE'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=0)

    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=11)

    # Puzzle 19/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=19,
        solution='3,32,E,E,NE,NE;6,20,E,NE,SE,E;1,18,NW,NE,NE,W;4,29,W,W,SW,NW;2,24,NE,NW,E,NW'
    )
    red = Noodle.red()
    puzzle.place(red, position=4)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=9)

    # Puzzle 20/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=20,
        solution='6,20,NE,NW,E,NE;1,16,NE,E,E,NW;4,32,NE,NE,NW,E;2,25,SW,W,SE,W;5,31,NW,E,NW,E'
    )
    dark_green = Noodle.dark_green()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=2)

    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=5)
    puzzle.place(dark_blue, position=24)

    # Puzzle 21/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=21,
        solution='3,32,E,E,NE,NE;1,31,NE,E,E,NW;4,22,NE,NE,E,NW;7,24,NW,E,NE,NW;2,9,SE,SW,E,SW'
    )
    pink = Noodle.pink()
    pink.rotate(increment=3)
    puzzle.place(pink, position=3)

    red = Noodle.red()
    red.rotate(increment=1)
    puzzle.place(red, position=4)

    # Puzzle 22/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=22,
        solution='3,20,SE,SE,E,E;6,9,SE,E,SW,SE;1,22,SE,E,E,SW;2,25,W,NW,SW,NW;5,7,E,SW,E,SW'
    )
    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    puzzle.place(dark_green, position=12)

    # Puzzle 23/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=23,
        solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;1,23,SW,W,W,SE;4,13,W,W,SW,NW;7,20,NE,SE,E,NE'
    )
    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=2)
    puzzle.place(yellow, position=9)

    red = Noodle.red()
    puzzle.place(red, position=6)

    # Puzzle 24/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=24,
        solution='3,31,NE,NE,NW,NW;6,7,SE,E,SW,SE;4,32,NE,NE,NW,E;2,9,SE,SW,E,SW;5,24,SE,W,SE,W'
    )
    light_green = Noodle.light_green()
    light_green.flip()
    puzzle.place(light_green, position=12)

    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=3)
    puzzle.place(dark_green, position=1)

    # Puzzle 25/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=25,
        solution='3,32,E,E,NE,NE;6,6,SW,SE,W,SW;1,23,W,SW,SW,NW;7,19,W,SE,SW,W;5,12,NE,SE,NE,SE'
    )
    light_blue = Noodle.light_blue()
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)

    yellow = Noodle.yellow()
    yellow.rotate(increment=5)
    puzzle.place(yellow, position=20)

    # Puzzle 26/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=26,
        solution='3,14,NW,NW,W,W;6,31,NE,NW,E,NE;4,18,SW,SW,SE,W;2,19,NW,W,NE,W;5,34,NW,E,NW,E'
    )
    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=4)
    puzzle.place(dark_green, position=0)

    light_green = Noodle.light_green()
    light_green.flip()
    light_green.rotate(increment=1)
    puzzle.place(light_green, position=26)

    # Puzzle 27/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=27,
        solution='6,14,SW,SE,W,SW;1,27,NE,NW,NW,E;4,5,E,E,NE,SE;7,32,NE,SE,E,NE;5,23,NW,E,NW,E'
    )
    dark_blue = Noodle.dark_blue()
    dark_blue.rotate(increment=3)
    puzzle.place(dark_blue, position=2)

    yellow = Noodle.yellow()
    yellow.flip()
    yellow.rotate(increment=1)
    puzzle.place(yellow, position=31)

    # Puzzle 28/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=28,
        solution='3,3,SW,SW,SE,SE;4,2,SW,SW,SE,W;6,27,NW,W,NE,NW;7,33,NW,SW,W,NW;1,22,E,SE,SE,NE;2,25,NW,NE,W,NE'
    )
    red = Noodle.red()
    red.rotate(increment=5)
    puzzle.place(red, position=10)

    # Puzzle 29/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=29,
        solution='3,14,NW,NW,W,W;4,25,NW,NW,W,NE;5,16,W,NE,W,NE;7,18,SW,E,SE,SW;1,21,E,SE,SE,NE;2,20,SE,E,SW,E'
    )
    pink = Noodle.pink()
    pink.rotate(1)
    puzzle.place(pink, position=0)

    # Puzzle 30/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=30,
        solution='3,20,SE,SE,E,E;4,9,SE,SE,E,SW;5,18,E,SW,E,SW;6,34,NW,W,NE,NW;1,13,W,NW,NW,SW;2,14,NW,W,NE,W'
    )
    dark_green = Noodle.dark_green()
    dark_green.flip()
    dark_green.rotate(increment=1)
    puzzle.place(dark_green, position=16)

    # Puzzle 31/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=31,
        solution='3,20,SE,SE,E,E;4,27,E,E,SE,NE;5,9,E,SW,E,SW;6,22,E,NE,SE,E;7,14,SW,NW,W,SW;1,11,NE,E,E,NW'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=3)
    puzzle.place(yellow, position=2)

    # Puzzle 32/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=32,
        solution='3,13,SW,SW,SE,SE;4,4,SE,SE,E,SW;6,27,NW,W,NE,NW;7,33,NW,SW,W,NW;1,11,E,NE,NE,SE;2,14,SW,SE,W,SE;'
    )
    red = Noodle.red()
    red.rotate(increment=3)
    puzzle.place(red, position=2)

    # Puzzle 33/3 ######################################
    puzzle = Puzzle.create(
        level=level3,
        number=33,
        solution='3,14,NW,NW,W,W;4,31,E,E,NE,SE;5,27,W,NE,W,NE;6,25,NW,W,NE,NW;7,22,SE,NE,E,SE;1,17,W,NW,NW,SW;'
    )
    yellow = Noodle.yellow()
    yellow.rotate(increment=1)
    puzzle.place(yellow, position=0)
