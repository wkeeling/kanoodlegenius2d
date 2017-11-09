from .orientation import Orientation
"""Helper functions for determining hole positions."""


class _Hole:
    """Represents a hold on the board and knows about its surrounding _holes,
    or immediate neighbours.
    """
    def __init__(self):
        self.neighbours = {}  # Add a neighbour with Orientation key, Hole val

    
# Manually wire up each hole on the board adding its neighbours.
_holes = [_Hole() for _ in range(35)]

_holes[0].neighbours[Orientation.E] = _holes[1]
_holes[0].neighbours[Orientation.SE] = _holes[5]
_holes[0].neighbours[Orientation.SW] = _holes[4]

_holes[1].neighbours[Orientation.E] = _holes[2]
_holes[1].neighbours[Orientation.SE] = _holes[6]
_holes[1].neighbours[Orientation.SW] = _holes[5]
_holes[1].neighbours[Orientation.W] = _holes[0]

_holes[2].neighbours[Orientation.E] = _holes[3]
_holes[2].neighbours[Orientation.SE] = _holes[7]
_holes[2].neighbours[Orientation.SW] = _holes[6]
_holes[2].neighbours[Orientation.W] = _holes[1]

_holes[3].neighbours[Orientation.SE] = _holes[8]
_holes[3].neighbours[Orientation.SW] = _holes[7]
_holes[3].neighbours[Orientation.W] = _holes[2]

_holes[4].neighbours[Orientation.E] = _holes[5]
_holes[4].neighbours[Orientation.SE] = _holes[10]
_holes[4].neighbours[Orientation.SW] = _holes[9]
_holes[4].neighbours[Orientation.NE] = _holes[0]

_holes[5].neighbours[Orientation.E] = _holes[6]
_holes[5].neighbours[Orientation.SE] = _holes[11]
_holes[5].neighbours[Orientation.SW] = _holes[10]
_holes[5].neighbours[Orientation.W] = _holes[4]
_holes[5].neighbours[Orientation.NW] = _holes[0]
_holes[5].neighbours[Orientation.NE] = _holes[1]

_holes[6].neighbours[Orientation.E] = _holes[7]
_holes[6].neighbours[Orientation.SE] = _holes[12]
_holes[6].neighbours[Orientation.SW] = _holes[11]
_holes[6].neighbours[Orientation.W] = _holes[5]
_holes[6].neighbours[Orientation.NW] = _holes[1]
_holes[6].neighbours[Orientation.NE] = _holes[2]

_holes[7].neighbours[Orientation.E] = _holes[8]
_holes[7].neighbours[Orientation.SE] = _holes[13]
_holes[7].neighbours[Orientation.SW] = _holes[12]
_holes[7].neighbours[Orientation.W] = _holes[6]
_holes[7].neighbours[Orientation.NW] = _holes[2]
_holes[7].neighbours[Orientation.NE] = _holes[3]

_holes[8].neighbours[Orientation.SE] = _holes[14]
_holes[8].neighbours[Orientation.SW] = _holes[13]
_holes[8].neighbours[Orientation.W] = _holes[7]
_holes[8].neighbours[Orientation.NW] = _holes[3]

_holes[9].neighbours[Orientation.E] = _holes[10]
_holes[9].neighbours[Orientation.SE] = _holes[15]
_holes[9].neighbours[Orientation.NE] = _holes[4]

_holes[10].neighbours[Orientation.E] = _holes[11]
_holes[10].neighbours[Orientation.SE] = _holes[16]
_holes[10].neighbours[Orientation.SW] = _holes[15]
_holes[10].neighbours[Orientation.W] = _holes[9]
_holes[10].neighbours[Orientation.NW] = _holes[4]
_holes[10].neighbours[Orientation.NE] = _holes[5]

_holes[11].neighbours[Orientation.E] = _holes[12]
_holes[11].neighbours[Orientation.SE] = _holes[17]
_holes[11].neighbours[Orientation.SW] = _holes[16]
_holes[11].neighbours[Orientation.W] = _holes[10]
_holes[11].neighbours[Orientation.NW] = _holes[5]
_holes[11].neighbours[Orientation.NE] = _holes[6]

_holes[12].neighbours[Orientation.E] = _holes[13]
_holes[12].neighbours[Orientation.SE] = _holes[18]
_holes[12].neighbours[Orientation.SW] = _holes[17]
_holes[12].neighbours[Orientation.W] = _holes[11]
_holes[12].neighbours[Orientation.NW] = _holes[6]
_holes[12].neighbours[Orientation.NE] = _holes[7]

_holes[13].neighbours[Orientation.E] = _holes[14]
_holes[13].neighbours[Orientation.SE] = _holes[19]
_holes[13].neighbours[Orientation.SW] = _holes[18]
_holes[13].neighbours[Orientation.W] = _holes[12]
_holes[13].neighbours[Orientation.NW] = _holes[7]
_holes[13].neighbours[Orientation.NE] = _holes[9]

_holes[14].neighbours[Orientation.SW] = _holes[19]
_holes[14].neighbours[Orientation.W] = _holes[13]
_holes[14].neighbours[Orientation.NW] = _holes[8]

_holes[15].neighbours[Orientation.E] = _holes[16]
_holes[15].neighbours[Orientation.SE] = _holes[21]
_holes[15].neighbours[Orientation.SW] = _holes[20]
_holes[15].neighbours[Orientation.NW] = _holes[9]
_holes[15].neighbours[Orientation.NE] = _holes[10]

_holes[16].neighbours[Orientation.E] = _holes[17]
_holes[16].neighbours[Orientation.SE] = _holes[22]
_holes[16].neighbours[Orientation.SW] = _holes[21]
_holes[16].neighbours[Orientation.W] = _holes[15]
_holes[16].neighbours[Orientation.NW] = _holes[10]
_holes[16].neighbours[Orientation.NE] = _holes[11]

_holes[17].neighbours[Orientation.E] = _holes[18]
_holes[17].neighbours[Orientation.SE] = _holes[23]
_holes[17].neighbours[Orientation.SW] = _holes[22]
_holes[17].neighbours[Orientation.W] = _holes[16]
_holes[17].neighbours[Orientation.NW] = _holes[11]
_holes[17].neighbours[Orientation.NE] = _holes[12]

_holes[18].neighbours[Orientation.E] = _holes[19]
_holes[18].neighbours[Orientation.SE] = _holes[24]
_holes[18].neighbours[Orientation.SW] = _holes[23]
_holes[18].neighbours[Orientation.W] = _holes[17]
_holes[18].neighbours[Orientation.NW] = _holes[12]
_holes[18].neighbours[Orientation.NE] = _holes[13]

_holes[19].neighbours[Orientation.SE] = _holes[25]
_holes[19].neighbours[Orientation.SW] = _holes[24]
_holes[19].neighbours[Orientation.W] = _holes[18]
_holes[19].neighbours[Orientation.NW] = _holes[13]
_holes[19].neighbours[Orientation.NE] = _holes[14]

_holes[20].neighbours[Orientation.E] = _holes[21]
_holes[20].neighbours[Orientation.SE] = _holes[26]
_holes[20].neighbours[Orientation.NE] = _holes[15]

_holes[21].neighbours[Orientation.E] = _holes[22]
_holes[21].neighbours[Orientation.SE] = _holes[27]
_holes[21].neighbours[Orientation.SW] = _holes[26]
_holes[21].neighbours[Orientation.W] = _holes[20]
_holes[21].neighbours[Orientation.NW] = _holes[15]
_holes[21].neighbours[Orientation.NE] = _holes[16]

_holes[22].neighbours[Orientation.E] = _holes[23]
_holes[22].neighbours[Orientation.SE] = _holes[28]
_holes[22].neighbours[Orientation.SW] = _holes[27]
_holes[22].neighbours[Orientation.W] = _holes[21]
_holes[22].neighbours[Orientation.NW] = _holes[16]
_holes[22].neighbours[Orientation.NE] = _holes[17]

_holes[23].neighbours[Orientation.E] = _holes[24]
_holes[23].neighbours[Orientation.SE] = _holes[29]
_holes[23].neighbours[Orientation.SW] = _holes[28]
_holes[23].neighbours[Orientation.W] = _holes[22]
_holes[23].neighbours[Orientation.NW] = _holes[17]
_holes[23].neighbours[Orientation.NE] = _holes[18]

_holes[24].neighbours[Orientation.E] = _holes[25]
_holes[24].neighbours[Orientation.SE] = _holes[30]
_holes[24].neighbours[Orientation.SW] = _holes[29]
_holes[24].neighbours[Orientation.W] = _holes[23]
_holes[24].neighbours[Orientation.NW] = _holes[18]
_holes[24].neighbours[Orientation.NE] = _holes[19]

_holes[25].neighbours[Orientation.SW] = _holes[30]
_holes[25].neighbours[Orientation.W] = _holes[24]
_holes[25].neighbours[Orientation.NW] = _holes[19]

_holes[26].neighbours[Orientation.E] = _holes[27]
_holes[26].neighbours[Orientation.SE] = _holes[31]
_holes[26].neighbours[Orientation.NW] = _holes[20]
_holes[26].neighbours[Orientation.NE] = _holes[21]

_holes[27].neighbours[Orientation.E] = _holes[28]
_holes[27].neighbours[Orientation.SE] = _holes[32]
_holes[27].neighbours[Orientation.SW] = _holes[31]
_holes[27].neighbours[Orientation.W] = _holes[26]
_holes[27].neighbours[Orientation.NW] = _holes[21]
_holes[27].neighbours[Orientation.NE] = _holes[22]

_holes[28].neighbours[Orientation.E] = _holes[29]
_holes[28].neighbours[Orientation.SE] = _holes[33]
_holes[28].neighbours[Orientation.SW] = _holes[32]
_holes[28].neighbours[Orientation.W] = _holes[27]
_holes[28].neighbours[Orientation.NW] = _holes[22]
_holes[28].neighbours[Orientation.NE] = _holes[23]

_holes[29].neighbours[Orientation.E] = _holes[30]
_holes[29].neighbours[Orientation.SE] = _holes[34]
_holes[29].neighbours[Orientation.SW] = _holes[33]
_holes[29].neighbours[Orientation.W] = _holes[28]
_holes[29].neighbours[Orientation.NW] = _holes[23]
_holes[29].neighbours[Orientation.NE] = _holes[24]

_holes[30].neighbours[Orientation.SW] = _holes[34]
_holes[30].neighbours[Orientation.W] = _holes[29]
_holes[30].neighbours[Orientation.NW] = _holes[24]
_holes[30].neighbours[Orientation.NE] = _holes[25]

_holes[31].neighbours[Orientation.E] = _holes[32]
_holes[31].neighbours[Orientation.NW] = _holes[26]
_holes[31].neighbours[Orientation.NE] = _holes[27]

_holes[32].neighbours[Orientation.E] = _holes[33]
_holes[32].neighbours[Orientation.W] = _holes[31]
_holes[32].neighbours[Orientation.NW] = _holes[27]
_holes[32].neighbours[Orientation.NE] = _holes[28]

_holes[33].neighbours[Orientation.E] = _holes[34]
_holes[33].neighbours[Orientation.W] = _holes[32]
_holes[33].neighbours[Orientation.NW] = _holes[28]
_holes[33].neighbours[Orientation.NE] = _holes[29]

_holes[34].neighbours[Orientation.W] = _holes[33]
_holes[34].neighbours[Orientation.NW] = _holes[29]
_holes[34].neighbours[Orientation.NE] = _holes[30]


def find_position(position, orientation):
    """Given a hole position and orientation, find the neighbouring hole position.
    
    Args:
        position:
            The position of the hole.
        orientation:
            The orientation of the neighbouring hole.
        
    Returns:
        The position of the neighbouring hole, or None if no position exists
        because the position would be off the board.
    """
    try:
        return _holes.index(_holes[position].neighbours[orientation])
    except (IndexError, KeyError):
        return None
