import collections


E = 'E'
SE = 'SE'
SW = 'SW'
W = 'W'
NW = 'NW'
NE = 'NE'


def rotate(start):
    orientations = collections.deque([NE, NW, W, SW, SE, E])

    if start not in orientations:
        raise ValueError('Invalid orientation {}'.format(start))

    while True:
        orientations.rotate()
        if orientations[1] == start:
            break

    return orientations[0]
