from unittest import TestCase

from kanoodlegenius2d.orientation import Orientation
from kanoodlegenius2d.piece import (Part,
                                    PuzzlePiece,
                                    Side)


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


class PuzzlePieceTest(TestCase):

    def test_flip_x(self):
        part1 = Part()
        part2 = Part()
        part3 = Part()
        part1.link(part2, Orientation.NE)
        part2.link(part3, Orientation.NE)

        piece = PuzzlePiece(PuzzlePiece.RED, part1, part2, part3)

        piece.flip_x()

        self.assertEqual(piece.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.SE)
        self.assertEqual(part3.orientation, Orientation.SE)

    def test_flip_x_again(self):
        part1 = Part()
        part2 = Part()
        part3 = Part()
        part4 = Part()
        part5 = Part()
        part1.link(part2, Orientation.SE)
        part2.link(part3, Orientation.SE)
        part3.link(part4, Orientation.NE)
        part4.link(part5, Orientation.E)

        piece = PuzzlePiece(PuzzlePiece.RED, part1, part2, part3, part4, part5)

        piece.flip_x()

        self.assertEqual(piece.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.NE)
        self.assertEqual(part3.orientation, Orientation.NE)
        self.assertEqual(part4.orientation, Orientation.SE)
        self.assertEqual(part5.orientation, Orientation.E)

    def test_flip_y(self):
        part1 = Part()
        part2 = Part()
        part3 = Part()
        part4 = Part()
        part1.link(part2, Orientation.NE)
        part2.link(part3, Orientation.NE)
        part3.link(part4, Orientation.E)

        piece = PuzzlePiece(PuzzlePiece.RED, part1, part2, part3, part4)

        piece.flip_y()

        self.assertEqual(piece.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.NW)
        self.assertEqual(part3.orientation, Orientation.NW)
        self.assertEqual(part4.orientation, Orientation.W)
