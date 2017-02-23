import collections
import itertools


class Knoodle:

    LIGHT_BLUE = 1
    DARK_BLUE = 2
    LIGHT_GREEN = 3
    DARK_GREEN = 4
    RED = 5
    YELLOW = 6
    PINK = 7

    def __init__(self, colour, *parts):
        """Initialise a new Knoodle with a colour and one or more linked
        parts that constitute it.

        Args:
            colour:
                The colour of this Knoodle.
            parts:
                One or more linked parts that make up this Knoodle.
        """
        self.parts = parts
        self.colour = colour
        self._sides = itertools.cycle([Side.A, Side.B])
        self.side = next(self._sides)

    def rotate(self):
        for part in self.parts:
            part.rotate()

    def flip_x(self):
        """Flip the knoodle over on the x axis."""
        x_conversions = {
            Orientation.SE: Orientation.NE,
            Orientation.NE: Orientation.SE,
            Orientation.NW: Orientation.SW,
            Orientation.SW: Orientation.NW,
            Orientation.E: Orientation.E,
            Orientation.W: Orientation.W
        }
        for part in self.parts:
            part.orientation = x_conversions.get(part.orientation)
        self.side = next(self._sides)

    def flip_y(self):
        """Flip the knoodle over on the y axis."""
        self.side = next(self._sides)

    def __iter__(self):
        return iter(self.parts)


class Part:

    def __init__(self):
        # A child part linked to us.
        self.part = None
        # Our orientation relative to our parent.
        self.orientation = None

    def link(self, part, orientation):
        self.part = part
        self.part.orientation = orientation

    def rotate(self):
        """Rotate ourselves clockwise by one degree relative to our parent."""
        if self.orientation:
            self.orientation = Orientation.rotate(self.orientation)


class Hole:

    def __init__(self):
        self.filled = False
        self.neighbours = {}  # Add a neighbour with Orientation key, Hole val


class Board:
    """Manually wire up each hole on the board adding its neighbours."""


class Orientation:

    E = 'E'
    SE = 'SE'
    SW = 'SW'
    W = 'W'
    NW = 'NW'
    NE = 'NE'

    @staticmethod
    def rotate(start):
        orientations = collections.deque([Orientation.NE,
                                          Orientation.NW,
                                          Orientation.W,
                                          Orientation.SW,
                                          Orientation.SE,
                                          Orientation.E])

        if start not in orientations:
            raise ValueError('Invalid orientation %s' % start)

        while True:
            orientations.rotate()
            if orientations[1] == start:
                break

        return orientations[0]


class Side:

    A = 'A'
    B = 'B'
