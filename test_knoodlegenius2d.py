from unittest.case import TestCase

from knoodlegenius2d import (Knoodle,
                             Orientation,
                             Part,
                             Side)


class OrientationTest(TestCase):

    def test_rotate_one_degree(self):
        o = Orientation.rotate(Orientation.E)

        self.assertEqual(o, Orientation.SE)

    def test_rotate_two_degrees(self):
        o = Orientation.rotate(Orientation.W)
        o = Orientation.rotate(o)

        self.assertEqual(o, Orientation.NE)


class PartTest(TestCase):

    def test_link_part(self):
        part = Part()
        child = Part()
        part.link(child, Orientation.SW)

        self.assertIsNone(part.orientation)
        self.assertEqual(child.orientation, Orientation.SW)

    def test_rotate_part(self):
        part = Part()
        child = Part()
        part.link(child, Orientation.SW)
        child.rotate()

        self.assertEqual(child.orientation, Orientation.W)


class KnoodleTest(TestCase):

    def test_flip_x(self):
        part1 = Part()
        part2 = Part()
        part3 = Part()
        part1.link(part2, Orientation.NE)
        part2.link(part3, Orientation.NE)

        knoodle = Knoodle(Knoodle.RED, part1, part2, part3)

        knoodle.flip_x()

        self.assertEqual(knoodle.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.SE)
        self.assertEqual(part3.orientation, Orientation.SE)

    def test_flip_x_again(self):
        part1 = Part()
        part2 = Part()
        part3 = Part()
        part4 = Part()
        part1.link(part2, Orientation.SE)
        part2.link(part3, Orientation.SE)
        part3.link(part4, Orientation.NE)

        knoodle = Knoodle(Knoodle.RED, part1, part2, part3, part4)

        knoodle.flip_x()

        self.assertEqual(knoodle.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.NE)
        self.assertEqual(part3.orientation, Orientation.NE)
        self.assertEqual(part4.orientation, Orientation.SE)


