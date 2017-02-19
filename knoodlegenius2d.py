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
        for part in self.parts:
            if part.orientation:
                part.rotate()
                part.rotate()
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
        self._neighbours = {}

    def add_neighbour(self, hole, orientation):
        self._neighbours[orientation] = hole

    def neighbour_at(self, orientation):
        """Get the neighbouring hole at the specified orientation.

        Args:
            orientation:
                The orientation to get the neighbour for.
        Returns:
            The neighbouring hole, or None if no neighbouring hole
            at the specified orientation.

        """
        self._neighbours.get(orientation)


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
