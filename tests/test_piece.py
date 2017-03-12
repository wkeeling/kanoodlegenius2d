from unittest import TestCase

from kanoodlegenius2d.orientation import Orientation
from kanoodlegenius2d.piece import (Part,
                                    PuzzlePiece,
                                    Side)


class PartTest(TestCase):

    def test_rotate_part(self):
        part = Part(Orientation.E)
        part.rotate()

        self.assertEqual(part.orientation, Orientation.SE)


class PuzzlePieceTest(TestCase):

    def test_flip_x(self):
        part1 = Part()
        part2 = Part(Orientation.NE)
        part3 = Part(Orientation.NE)

        piece = PuzzlePiece(PuzzlePiece.RED, part1, part2, part3)

        piece.flip_x()

        self.assertEqual(piece.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.SE)
        self.assertEqual(part3.orientation, Orientation.SE)

    def test_flip_x_again(self):
        part1 = Part()
        part2 = Part(Orientation.SE)
        part3 = Part(Orientation.SE)
        part4 = Part(Orientation.NE)
        part5 = Part(Orientation.E)

        piece = PuzzlePiece(PuzzlePiece.RED, part1, part2, part3, part4, part5)

        piece.flip_x()

        self.assertEqual(piece.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.NE)
        self.assertEqual(part3.orientation, Orientation.NE)
        self.assertEqual(part4.orientation, Orientation.SE)
        self.assertEqual(part5.orientation, Orientation.E)

    def test_flip_y(self):
        part1 = Part()
        part2 = Part(Orientation.NE)
        part3 = Part(Orientation.NE)
        part4 = Part(Orientation.E)

        piece = PuzzlePiece(PuzzlePiece.RED, part1, part2, part3, part4)

        piece.flip_y()

        self.assertEqual(piece.side, Side.B)
        self.assertEqual(part2.orientation, Orientation.NW)
        self.assertEqual(part3.orientation, Orientation.NW)
        self.assertEqual(part4.orientation, Orientation.W)
