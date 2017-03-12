from unittest.case import TestCase

from kanoodlegenius2d import (Board,
                              Orientation,
                              Part,
                              PuzzlePiece,
                              Side)


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


class BoardTest(TestCase):

    def test_iterate_holes(self):
        self.fail("Implement")

    def test_iterate_empty_holes(self):
        self.fail("Implement")

    def test_place_piece_in_hole1(self):
        self.fail("Implement")

    def test_hole1_neighbours(self):
        board = Board()
        hole1 = board[0]

        self.assertIsNotNone(hole1.neighbours.get(Orientation.E))
        self.assertIsNotNone(hole1.neighbours.get(Orientation.SE))
        self.assertIsNotNone(hole1.neighbours.get(Orientation.SW))
        self.assertIsNone(hole1.neighbours.get(Orientation.W))
        self.assertIsNone(hole1.neighbours.get(Orientation.NW))
        self.assertIsNone(hole1.neighbours.get(Orientation.NE))
