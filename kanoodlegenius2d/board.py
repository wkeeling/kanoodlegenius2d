from .orientation import Orientation


class Hole:

    def __init__(self):
        self.empty = True
        self.neighbours = {}  # Add a neighbour with Orientation key, Hole val


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

    holes[8].neighbours[Orientation.SE] = holes[14]
    holes[8].neighbours[Orientation.SW] = holes[13]
    holes[8].neighbours[Orientation.W] = holes[7]
    holes[8].neighbours[Orientation.NW] = holes[3]

    holes[9].neighbours[Orientation.E] = holes[10]
    holes[9].neighbours[Orientation.SE] = holes[15]
    holes[9].neighbours[Orientation.NE] = holes[4]

    holes[10].neighbours[Orientation.E] = holes[11]
    holes[10].neighbours[Orientation.SE] = holes[16]
    holes[10].neighbours[Orientation.SW] = holes[15]
    holes[10].neighbours[Orientation.W] = holes[9]
    holes[10].neighbours[Orientation.NW] = holes[4]
    holes[10].neighbours[Orientation.NE] = holes[5]

    holes[11].neighbours[Orientation.E] = holes[12]
    holes[11].neighbours[Orientation.SE] = holes[17]
    holes[11].neighbours[Orientation.SW] = holes[16]
    holes[11].neighbours[Orientation.W] = holes[10]
    holes[11].neighbours[Orientation.NW] = holes[5]
    holes[11].neighbours[Orientation.NE] = holes[6]

    holes[12].neighbours[Orientation.E] = holes[13]
    holes[12].neighbours[Orientation.SE] = holes[18]
    holes[12].neighbours[Orientation.SW] = holes[17]
    holes[12].neighbours[Orientation.W] = holes[11]
    holes[12].neighbours[Orientation.NW] = holes[6]
    holes[12].neighbours[Orientation.NE] = holes[7]

    holes[13].neighbours[Orientation.E] = holes[14]
    holes[13].neighbours[Orientation.SE] = holes[19]
    holes[13].neighbours[Orientation.SW] = holes[18]
    holes[13].neighbours[Orientation.W] = holes[12]
    holes[13].neighbours[Orientation.NW] = holes[7]
    holes[13].neighbours[Orientation.NE] = holes[9]

    holes[14].neighbours[Orientation.SW] = holes[19]
    holes[14].neighbours[Orientation.W] = holes[13]
    holes[14].neighbours[Orientation.NW] = holes[8]

    holes[15].neighbours[Orientation.E] = holes[16]
    holes[15].neighbours[Orientation.SE] = holes[21]
    holes[15].neighbours[Orientation.SW] = holes[20]
    holes[15].neighbours[Orientation.NW] = holes[9]
    holes[15].neighbours[Orientation.NE] = holes[10]

    holes[16].neighbours[Orientation.E] = holes[17]
    holes[16].neighbours[Orientation.SE] = holes[22]
    holes[16].neighbours[Orientation.SW] = holes[21]
    holes[16].neighbours[Orientation.W] = holes[15]
    holes[16].neighbours[Orientation.NW] = holes[10]
    holes[16].neighbours[Orientation.NE] = holes[11]

    holes[17].neighbours[Orientation.E] = holes[18]
    holes[17].neighbours[Orientation.SE] = holes[23]
    holes[17].neighbours[Orientation.SW] = holes[22]
    holes[17].neighbours[Orientation.W] = holes[16]
    holes[17].neighbours[Orientation.NW] = holes[11]
    holes[17].neighbours[Orientation.NE] = holes[12]

    holes[18].neighbours[Orientation.E] = holes[19]
    holes[18].neighbours[Orientation.SE] = holes[24]
    holes[18].neighbours[Orientation.SW] = holes[23]
    holes[18].neighbours[Orientation.W] = holes[17]
    holes[18].neighbours[Orientation.NW] = holes[12]
    holes[18].neighbours[Orientation.NE] = holes[13]

    holes[19].neighbours[Orientation.SE] = holes[25]
    holes[19].neighbours[Orientation.SW] = holes[24]
    holes[19].neighbours[Orientation.W] = holes[18]
    holes[19].neighbours[Orientation.NW] = holes[13]
    holes[19].neighbours[Orientation.NE] = holes[14]

    holes[20].neighbours[Orientation.E] = holes[21]
    holes[20].neighbours[Orientation.SE] = holes[26]
    holes[20].neighbours[Orientation.NE] = holes[15]

    holes[21].neighbours[Orientation.E] = holes[22]
    holes[21].neighbours[Orientation.SE] = holes[27]
    holes[21].neighbours[Orientation.SW] = holes[26]
    holes[21].neighbours[Orientation.W] = holes[20]
    holes[21].neighbours[Orientation.NW] = holes[15]
    holes[21].neighbours[Orientation.NE] = holes[16]

    holes[22].neighbours[Orientation.E] = holes[23]
    holes[22].neighbours[Orientation.SE] = holes[28]
    holes[22].neighbours[Orientation.SW] = holes[27]
    holes[22].neighbours[Orientation.W] = holes[21]
    holes[22].neighbours[Orientation.NW] = holes[16]
    holes[22].neighbours[Orientation.NE] = holes[17]

    holes[23].neighbours[Orientation.E] = holes[24]
    holes[23].neighbours[Orientation.SE] = holes[29]
    holes[23].neighbours[Orientation.SW] = holes[28]
    holes[23].neighbours[Orientation.W] = holes[22]
    holes[23].neighbours[Orientation.NW] = holes[17]
    holes[23].neighbours[Orientation.NE] = holes[18]

    holes[24].neighbours[Orientation.E] = holes[25]
    holes[24].neighbours[Orientation.SE] = holes[30]
    holes[24].neighbours[Orientation.SW] = holes[29]
    holes[24].neighbours[Orientation.W] = holes[23]
    holes[24].neighbours[Orientation.NW] = holes[18]
    holes[24].neighbours[Orientation.NE] = holes[19]

    holes[25].neighbours[Orientation.SW] = holes[30]
    holes[25].neighbours[Orientation.W] = holes[24]
    holes[25].neighbours[Orientation.NW] = holes[19]

    holes[26].neighbours[Orientation.E] = holes[27]
    holes[26].neighbours[Orientation.SE] = holes[31]
    holes[26].neighbours[Orientation.NW] = holes[20]
    holes[26].neighbours[Orientation.NE] = holes[21]

    holes[27].neighbours[Orientation.E] = holes[28]
    holes[27].neighbours[Orientation.SE] = holes[32]
    holes[27].neighbours[Orientation.SW] = holes[31]
    holes[27].neighbours[Orientation.W] = holes[26]
    holes[27].neighbours[Orientation.NW] = holes[21]
    holes[27].neighbours[Orientation.NE] = holes[22]

    holes[28].neighbours[Orientation.E] = holes[29]
    holes[28].neighbours[Orientation.SE] = holes[33]
    holes[28].neighbours[Orientation.SW] = holes[32]
    holes[28].neighbours[Orientation.W] = holes[27]
    holes[28].neighbours[Orientation.NW] = holes[22]
    holes[28].neighbours[Orientation.NE] = holes[23]

    holes[29].neighbours[Orientation.E] = holes[30]
    holes[29].neighbours[Orientation.SE] = holes[34]
    holes[29].neighbours[Orientation.SW] = holes[33]
    holes[29].neighbours[Orientation.W] = holes[28]
    holes[29].neighbours[Orientation.NW] = holes[23]
    holes[29].neighbours[Orientation.NE] = holes[24]

    holes[30].neighbours[Orientation.SW] = holes[34]
    holes[30].neighbours[Orientation.W] = holes[29]
    holes[30].neighbours[Orientation.NW] = holes[24]
    holes[30].neighbours[Orientation.NE] = holes[25]

    holes[31].neighbours[Orientation.E] = holes[32]
    holes[31].neighbours[Orientation.NW] = holes[26]
    holes[31].neighbours[Orientation.NE] = holes[27]

    holes[32].neighbours[Orientation.E] = holes[33]
    holes[32].neighbours[Orientation.W] = holes[31]
    holes[32].neighbours[Orientation.NW] = holes[27]
    holes[32].neighbours[Orientation.NE] = holes[28]

    holes[33].neighbours[Orientation.E] = holes[34]
    holes[33].neighbours[Orientation.W] = holes[32]
    holes[33].neighbours[Orientation.NW] = holes[28]
    holes[33].neighbours[Orientation.NE] = holes[29]

    holes[34].neighbours[Orientation.W] = holes[33]
    holes[34].neighbours[Orientation.NW] = holes[29]
    holes[34].neighbours[Orientation.NE] = holes[30]

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