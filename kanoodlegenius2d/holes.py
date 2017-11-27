from kanoodlegenius2d import orientation
"""Helper functions for determining hole positions."""


class _Hole:
    """Represents a hold on the board and knows about its surrounding _holes,
    or immediate neighbours.
    """
    def __init__(self):
        self.neighbours = {}  # Add a neighbour with orientation key, Hole val

    
# Manually wire up each hole on the board adding its neighbours.
_holes = [_Hole() for _ in range(35)]

_holes[0].neighbours[orientation.E] = _holes[1]
_holes[0].neighbours[orientation.SE] = _holes[5]
_holes[0].neighbours[orientation.SW] = _holes[4]

_holes[1].neighbours[orientation.E] = _holes[2]
_holes[1].neighbours[orientation.SE] = _holes[6]
_holes[1].neighbours[orientation.SW] = _holes[5]
_holes[1].neighbours[orientation.W] = _holes[0]

_holes[2].neighbours[orientation.E] = _holes[3]
_holes[2].neighbours[orientation.SE] = _holes[7]
_holes[2].neighbours[orientation.SW] = _holes[6]
_holes[2].neighbours[orientation.W] = _holes[1]

_holes[3].neighbours[orientation.SE] = _holes[8]
_holes[3].neighbours[orientation.SW] = _holes[7]
_holes[3].neighbours[orientation.W] = _holes[2]

_holes[4].neighbours[orientation.E] = _holes[5]
_holes[4].neighbours[orientation.SE] = _holes[10]
_holes[4].neighbours[orientation.SW] = _holes[9]
_holes[4].neighbours[orientation.NE] = _holes[0]

_holes[5].neighbours[orientation.E] = _holes[6]
_holes[5].neighbours[orientation.SE] = _holes[11]
_holes[5].neighbours[orientation.SW] = _holes[10]
_holes[5].neighbours[orientation.W] = _holes[4]
_holes[5].neighbours[orientation.NW] = _holes[0]
_holes[5].neighbours[orientation.NE] = _holes[1]

_holes[6].neighbours[orientation.E] = _holes[7]
_holes[6].neighbours[orientation.SE] = _holes[12]
_holes[6].neighbours[orientation.SW] = _holes[11]
_holes[6].neighbours[orientation.W] = _holes[5]
_holes[6].neighbours[orientation.NW] = _holes[1]
_holes[6].neighbours[orientation.NE] = _holes[2]

_holes[7].neighbours[orientation.E] = _holes[8]
_holes[7].neighbours[orientation.SE] = _holes[13]
_holes[7].neighbours[orientation.SW] = _holes[12]
_holes[7].neighbours[orientation.W] = _holes[6]
_holes[7].neighbours[orientation.NW] = _holes[2]
_holes[7].neighbours[orientation.NE] = _holes[3]

_holes[8].neighbours[orientation.SE] = _holes[14]
_holes[8].neighbours[orientation.SW] = _holes[13]
_holes[8].neighbours[orientation.W] = _holes[7]
_holes[8].neighbours[orientation.NW] = _holes[3]

_holes[9].neighbours[orientation.E] = _holes[10]
_holes[9].neighbours[orientation.SE] = _holes[15]
_holes[9].neighbours[orientation.NE] = _holes[4]

_holes[10].neighbours[orientation.E] = _holes[11]
_holes[10].neighbours[orientation.SE] = _holes[16]
_holes[10].neighbours[orientation.SW] = _holes[15]
_holes[10].neighbours[orientation.W] = _holes[9]
_holes[10].neighbours[orientation.NW] = _holes[4]
_holes[10].neighbours[orientation.NE] = _holes[5]

_holes[11].neighbours[orientation.E] = _holes[12]
_holes[11].neighbours[orientation.SE] = _holes[17]
_holes[11].neighbours[orientation.SW] = _holes[16]
_holes[11].neighbours[orientation.W] = _holes[10]
_holes[11].neighbours[orientation.NW] = _holes[5]
_holes[11].neighbours[orientation.NE] = _holes[6]

_holes[12].neighbours[orientation.E] = _holes[13]
_holes[12].neighbours[orientation.SE] = _holes[18]
_holes[12].neighbours[orientation.SW] = _holes[17]
_holes[12].neighbours[orientation.W] = _holes[11]
_holes[12].neighbours[orientation.NW] = _holes[6]
_holes[12].neighbours[orientation.NE] = _holes[7]

_holes[13].neighbours[orientation.E] = _holes[14]
_holes[13].neighbours[orientation.SE] = _holes[19]
_holes[13].neighbours[orientation.SW] = _holes[18]
_holes[13].neighbours[orientation.W] = _holes[12]
_holes[13].neighbours[orientation.NW] = _holes[7]
_holes[13].neighbours[orientation.NE] = _holes[8]

_holes[14].neighbours[orientation.SW] = _holes[19]
_holes[14].neighbours[orientation.W] = _holes[13]
_holes[14].neighbours[orientation.NW] = _holes[8]

_holes[15].neighbours[orientation.E] = _holes[16]
_holes[15].neighbours[orientation.SE] = _holes[21]
_holes[15].neighbours[orientation.SW] = _holes[20]
_holes[15].neighbours[orientation.NW] = _holes[9]
_holes[15].neighbours[orientation.NE] = _holes[10]

_holes[16].neighbours[orientation.E] = _holes[17]
_holes[16].neighbours[orientation.SE] = _holes[22]
_holes[16].neighbours[orientation.SW] = _holes[21]
_holes[16].neighbours[orientation.W] = _holes[15]
_holes[16].neighbours[orientation.NW] = _holes[10]
_holes[16].neighbours[orientation.NE] = _holes[11]

_holes[17].neighbours[orientation.E] = _holes[18]
_holes[17].neighbours[orientation.SE] = _holes[23]
_holes[17].neighbours[orientation.SW] = _holes[22]
_holes[17].neighbours[orientation.W] = _holes[16]
_holes[17].neighbours[orientation.NW] = _holes[11]
_holes[17].neighbours[orientation.NE] = _holes[12]

_holes[18].neighbours[orientation.E] = _holes[19]
_holes[18].neighbours[orientation.SE] = _holes[24]
_holes[18].neighbours[orientation.SW] = _holes[23]
_holes[18].neighbours[orientation.W] = _holes[17]
_holes[18].neighbours[orientation.NW] = _holes[12]
_holes[18].neighbours[orientation.NE] = _holes[13]

_holes[19].neighbours[orientation.SE] = _holes[25]
_holes[19].neighbours[orientation.SW] = _holes[24]
_holes[19].neighbours[orientation.W] = _holes[18]
_holes[19].neighbours[orientation.NW] = _holes[13]
_holes[19].neighbours[orientation.NE] = _holes[14]

_holes[20].neighbours[orientation.E] = _holes[21]
_holes[20].neighbours[orientation.SE] = _holes[26]
_holes[20].neighbours[orientation.NE] = _holes[15]

_holes[21].neighbours[orientation.E] = _holes[22]
_holes[21].neighbours[orientation.SE] = _holes[27]
_holes[21].neighbours[orientation.SW] = _holes[26]
_holes[21].neighbours[orientation.W] = _holes[20]
_holes[21].neighbours[orientation.NW] = _holes[15]
_holes[21].neighbours[orientation.NE] = _holes[16]

_holes[22].neighbours[orientation.E] = _holes[23]
_holes[22].neighbours[orientation.SE] = _holes[28]
_holes[22].neighbours[orientation.SW] = _holes[27]
_holes[22].neighbours[orientation.W] = _holes[21]
_holes[22].neighbours[orientation.NW] = _holes[16]
_holes[22].neighbours[orientation.NE] = _holes[17]

_holes[23].neighbours[orientation.E] = _holes[24]
_holes[23].neighbours[orientation.SE] = _holes[29]
_holes[23].neighbours[orientation.SW] = _holes[28]
_holes[23].neighbours[orientation.W] = _holes[22]
_holes[23].neighbours[orientation.NW] = _holes[17]
_holes[23].neighbours[orientation.NE] = _holes[18]

_holes[24].neighbours[orientation.E] = _holes[25]
_holes[24].neighbours[orientation.SE] = _holes[30]
_holes[24].neighbours[orientation.SW] = _holes[29]
_holes[24].neighbours[orientation.W] = _holes[23]
_holes[24].neighbours[orientation.NW] = _holes[18]
_holes[24].neighbours[orientation.NE] = _holes[19]

_holes[25].neighbours[orientation.SW] = _holes[30]
_holes[25].neighbours[orientation.W] = _holes[24]
_holes[25].neighbours[orientation.NW] = _holes[19]

_holes[26].neighbours[orientation.E] = _holes[27]
_holes[26].neighbours[orientation.SE] = _holes[31]
_holes[26].neighbours[orientation.NW] = _holes[20]
_holes[26].neighbours[orientation.NE] = _holes[21]

_holes[27].neighbours[orientation.E] = _holes[28]
_holes[27].neighbours[orientation.SE] = _holes[32]
_holes[27].neighbours[orientation.SW] = _holes[31]
_holes[27].neighbours[orientation.W] = _holes[26]
_holes[27].neighbours[orientation.NW] = _holes[21]
_holes[27].neighbours[orientation.NE] = _holes[22]

_holes[28].neighbours[orientation.E] = _holes[29]
_holes[28].neighbours[orientation.SE] = _holes[33]
_holes[28].neighbours[orientation.SW] = _holes[32]
_holes[28].neighbours[orientation.W] = _holes[27]
_holes[28].neighbours[orientation.NW] = _holes[22]
_holes[28].neighbours[orientation.NE] = _holes[23]

_holes[29].neighbours[orientation.E] = _holes[30]
_holes[29].neighbours[orientation.SE] = _holes[34]
_holes[29].neighbours[orientation.SW] = _holes[33]
_holes[29].neighbours[orientation.W] = _holes[28]
_holes[29].neighbours[orientation.NW] = _holes[23]
_holes[29].neighbours[orientation.NE] = _holes[24]

_holes[30].neighbours[orientation.SW] = _holes[34]
_holes[30].neighbours[orientation.W] = _holes[29]
_holes[30].neighbours[orientation.NW] = _holes[24]
_holes[30].neighbours[orientation.NE] = _holes[25]

_holes[31].neighbours[orientation.E] = _holes[32]
_holes[31].neighbours[orientation.NW] = _holes[26]
_holes[31].neighbours[orientation.NE] = _holes[27]

_holes[32].neighbours[orientation.E] = _holes[33]
_holes[32].neighbours[orientation.W] = _holes[31]
_holes[32].neighbours[orientation.NW] = _holes[27]
_holes[32].neighbours[orientation.NE] = _holes[28]

_holes[33].neighbours[orientation.E] = _holes[34]
_holes[33].neighbours[orientation.W] = _holes[32]
_holes[33].neighbours[orientation.NW] = _holes[28]
_holes[33].neighbours[orientation.NE] = _holes[29]

_holes[34].neighbours[orientation.W] = _holes[33]
_holes[34].neighbours[orientation.NW] = _holes[29]
_holes[34].neighbours[orientation.NE] = _holes[30]


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
