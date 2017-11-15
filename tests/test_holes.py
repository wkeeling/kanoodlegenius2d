from unittest import TestCase

from kanoodlegenius2d.holes import find_position
from kanoodlegenius2d import orientation


class FindPositionTest(TestCase):

    def test_neighbour_positions_hole0(self):
        self.assertEqual(find_position(0, orientation.E), 1)

    def test_invalid_position(self):
        self.assertIsNone(find_position(100, orientation.E))

    def test_no_neighbour(self):
        self.assertIsNone(find_position(0, orientation.W))
