from unittest import TestCase

from kanoodlegenius2d.models.orientation import Orientation


class OrientationTest(TestCase):

    def test_rotate_one_degree(self):
        o = Orientation.rotate(Orientation.E)

        self.assertEqual(o, Orientation.SE)

    def test_rotate_two_degrees(self):
        o = Orientation.rotate(Orientation.W)
        o = Orientation.rotate(o)

        self.assertEqual(o, Orientation.NE)

    def test_invalid_orientation(self):
        with self.assertRaises(ValueError):
            Orientation.rotate('foobar')
