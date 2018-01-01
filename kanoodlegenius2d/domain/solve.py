from collections import namedtuple


position = namedtuple('position', 'noodle part hole')


class NoodleManipulator:
    """Keeps track of the state of a noodle as its orientation is manipulated for each of its parts
    across a set of unoccupied board holes.
    """

    def __init__(self, noodle, symmetrical=False):
        """Initialise a new instance of a NoodleManipulator.

        Args:
            noodle: The Noodle instance being manipulated.
            symmetrical: Whether the Noodle is a symmetrical shape.
        """
        self._noodle = noodle
        self._symmetrical = symmetrical

        self._rotation_count = 0
        self._part_count = 0
        self._current_hole = None
        self._holes_tried = set()

    def manipulate(self, unoccupied_holes):
        """Manipulate the noodle based on a sequence of unoccupied board holes.

        Args:
            unoccupied_holes: A list of unoccupied board holes.
        """
        if self._current_hole is None:
            self._current_hole = self._next_unoccupied_hole(unoccupied_holes)
            if self._current_hole is None:
                return None  # Tried all holes

        if self._rotation_count > 0:
            if self._rotation_count % 6 == 0:
                self._noodle.flip()
            if self._rotation_count % 12 == 0:
                self._part_count += 1
            if self._rotation_count == 60:  # All rotations (x12) per part (x5) tried
                self._rotation_count = 0
                self._part_count = 0
                self._holes_tried.add(self._current_hole)
                self._current_hole = self._next_unoccupied_hole(unoccupied_holes)

        self._noodle.rotate(increment=1)
        self._rotation_count += 1
        pos = position(noodle=self._noodle, part=self._part_count, hole=self._current_hole)

        return pos

    def _next_unoccupied_hole(self, unoccupied_holes):
        for hole in unoccupied_holes:
            if hole not in self._holes_tried:
                return hole

        return None  # Tried all holes

