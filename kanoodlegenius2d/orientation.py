import collections


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