from unittest import TestCase

from kanoodlegenius2d import orientation


class OrientationTest(TestCase):

    def test_rotate_one_degree(self):
        o = orientation.rotate(orientation.E)

        self.assertEqual(o, orientation.SE)

    def test_rotate_two_degrees(self):
        o = orientation.rotate(orientation.W)
        o = orientation.rotate(o)

        self.assertEqual(o, orientation.NE)

    def test_invalid_orientation(self):
        with self.assertRaises(ValueError):
            orientation.rotate('foobar')
