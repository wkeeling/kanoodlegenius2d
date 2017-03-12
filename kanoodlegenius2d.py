import collections
import itertools


class KanoodleGenius2D:
    pass


class Hole:

    def __init__(self):
        self.empty = True
        self.neighbours = {}  # Add a neighbour with Orientation key, Hole val


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


class Board:
    """Manually wire up each hole on the board adding its neighbours."""
    holes = [Hole() for _ in range(35)]

    holes[0].neighbours[Orientation.E] = holes[1]
    holes[0].neighbours[Orientation.SE] = holes[5]
    holes[0].neighbours[Orientation.SW] = holes[4]

    holes[1].neighbours[Orientation.E] = holes[2]
    holes[1].neighbours[Orientation.SE] = holes[6]
    holes[1].neighbours[Orientation.SW] = holes[5]
    holes[1].neighbours[Orientation.W] = holes[0]

    holes[2].neighbours[Orientation.E] = holes[3]
    holes[2].neighbours[Orientation.SE] = holes[7]
    holes[2].neighbours[Orientation.SW] = holes[6]
    holes[2].neighbours[Orientation.W] = holes[1]

    holes[3].neighbours[Orientation.SE] = holes[8]
    holes[3].neighbours[Orientation.SW] = holes[7]
    holes[3].neighbours[Orientation.W] = holes[2]

    holes[4].neighbours[Orientation.E] = holes[5]
    holes[4].neighbours[Orientation.SE] = holes[10]
    holes[4].neighbours[Orientation.SW] = holes[9]
    holes[4].neighbours[Orientation.NE] = holes[0]

    holes[5].neighbours[Orientation.E] = holes[6]
    holes[5].neighbours[Orientation.SE] = holes[11]
    holes[5].neighbours[Orientation.SW] = holes[10]
    holes[5].neighbours[Orientation.W] = holes[4]
    holes[5].neighbours[Orientation.NW] = holes[0]
    holes[5].neighbours[Orientation.NE] = holes[1]

    holes[6].neighbours[Orientation.E] = holes[7]
    holes[6].neighbours[Orientation.SE] = holes[12]
    holes[6].neighbours[Orientation.SW] = holes[11]
    holes[6].neighbours[Orientation.W] = holes[5]
    holes[6].neighbours[Orientation.NW] = holes[1]
    holes[6].neighbours[Orientation.NE] = holes[2]

    holes[7].neighbours[Orientation.E] = holes[8]
    holes[7].neighbours[Orientation.SE] = holes[13]
    holes[7].neighbours[Orientation.SW] = holes[12]
    holes[7].neighbours[Orientation.W] = holes[6]
    holes[7].neighbours[Orientation.NW] = holes[2]
    holes[7].neighbours[Orientation.NE] = holes[3]


    def place(self, piece, hole_pos):
        """Place a puzzle piece on the board in the specified hole.

        Hole numbering starts at 0 and runs to 34. If a piece does not fit
        given its current orientation, then return False.

        Args:
            piece:
                The puzzle piece to place.
            hole_pos:
                The hole position, an integer between 0 - 34.
        Returns:
            True if the puzzle piece was successfully placed in the specified
            position given its orientation, False otherwise.
        """
        pass

    def empties(self):
        """Return an iterator over the empty holes on the board.

        Returns:
            An iterator over all of the empty holes.
        """
        return (hole for hole in self.holes if hole.empty)

    def __iter__(self):
        """Return an iterator over all the holes on the board.

        Returns:
            An iterator over all the holes.
        """
        return iter(self.holes)

    def __getitem__(self, i):
        """Return the hole at the specified index.

        Args:
            i:
                The index.
        Returns:
            The hole.
        Raises:
            IndexError: If no hole exists at the specified index.

        """
        return self.holes[i]


class PuzzlePiece:

    LIGHT_BLUE = 1
    DARK_BLUE = 2
    LIGHT_GREEN = 3
    DARK_GREEN = 4
    RED = 5
    YELLOW = 6
    PINK = 7

    def __init__(self, colour, *parts):
        """Initialise a new PuzzlePiece with a colour and one or more linked
        parts that constitute it.

        Args:
            colour:
                The colour of this PuzzlePiece.
            parts:
                One or more linked parts that make up this PuzzlePiece.
        """
        self.parts = parts
        self.colour = colour
        self._sides = itertools.cycle([Side.A, Side.B])
        self.side = next(self._sides)

    def rotate(self):
        for part in self.parts:
            part.rotate()

    def flip_x(self):
        """Flip the puzzle piece over on the x axis."""
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
        """Flip the puzzle piece over on the y axis."""
        self.side = next(self._sides)
        y_conversions = {
            Orientation.SE: Orientation.SW,
            Orientation.NE: Orientation.NW,
            Orientation.NW: Orientation.NE,
            Orientation.SW: Orientation.SE,
            Orientation.E: Orientation.W,
            Orientation.W: Orientation.E
        }
        for part in self.parts:
            part.orientation = y_conversions.get(part.orientation)

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


class Side:

    A = 'A'
    B = 'B'
