import collections


E = 'E'
SE = 'SE'
SW = 'SW'
W = 'W'
NW = 'NW'
NE = 'NE'


def rotate(start):
    """Rotate the orientation clockwise one increment from the starting
    orientation.

    Args:
        start:
            The starting orientation.
    Returns:
        The orientation one increment clockwise from the start.
    """
    orientations = collections.deque([NE, NW, W, SW, SE, E])

    if start not in orientations:
        raise ValueError('Invalid orientation {}'.format(start))

    while True:
        orientations.rotate()
        if orientations[1] == start:
            break

    return orientations[0]


def opposite(orientation):
    """Return the orientation opposite from the one supplied, e.g. E --> W

    Args:
        orientation:
            The orientation to find the opposite of.
    Returns:
        The opposite orientation.
    """
    opposites = {
        E: W,
        SE: SW,
        NE: NW
    }

    try:
        return opposites[orientation]
    except KeyError:
        return dict(zip(opposites.values(), opposites.keys()))[orientation]
