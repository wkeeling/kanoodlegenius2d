import itertools

from .models.orientation import Orientation


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
        self._parts = parts
        self.colour = colour
        self._sides = itertools.cycle([Side.A, Side.B])
        self.side = next(self._sides)

    @property
    def root_part(self):
        """The root part of the parts that comprise us."""
        return self._parts[0]

    def rotate(self):
        """Rotate the puzzle piece clockwise by one degree."""
        for part in self._parts:
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
        for part in self._parts:
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
        for part in self._parts:
            part.orientation = y_conversions.get(part.orientation)


class Part:

    def __init__(self):
        # Our child parts.
        self.children = []
        # Reference to our parent.
        self.parent = None
        # Our orientation relative to our parent.
        self.orientation = None

    def link(self, part, orientation):
        """Link a child part to this part with the given orientation
        relative to us.

        Args:
            part:
                The child part to link.
            orientation:
                The orientation of the child part relative to us.
        """
        self.children.append(part)
        part.parent = self
        part.orientation = orientation

    def rotate(self):
        """Rotate ourselves clockwise by one degree relative to our parent."""
        if self.orientation:
            self.orientation = Orientation.rotate(self.orientation)

    def __iter__(self):
        """Return an iterator over the children of this part."""
        return iter(self.children)


class Side:

    A = 'A'
    B = 'B'
