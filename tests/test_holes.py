from unittest import TestCase

from kanoodlegenius2d.holes import (find_position,
                                    Orientation)


class FindPositionTest(TestCase):

    def test_neighbour_positions_hole0(self):
        self.assertEqual(find_position(0, Orientation.E), 1)

    def test_hole15_neighbours(self):
        self.fail('implement')

    def test_hole23_neighbours(self):
        self.fail('implement')

    def test_hole27_neighbours(self):
        self.fail('implement')

    def test_hole31_neighbours(self):
        self.fail('implement')

    def test_invalid_position(self):
        self.assertIsNone(find_position(100, Orientation.E))

    def test_no_neighbour(self):
        self.assertIsNone(find_position(0, Orientation.W))
