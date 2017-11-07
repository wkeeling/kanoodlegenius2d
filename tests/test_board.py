from unittest import TestCase

from kanoodlegenius2d.board import Board
from kanoodlegenius2d.models.orientation import Orientation
from kanoodlegenius2d.piece import (Part,
                                    PuzzlePiece)


class BoardTest(TestCase):

    def test_iterate_holes(self):
        count = 0
        for hole in Board():
            self.assertTrue(hole.empty)
            count += 1
        self.assertEqual(count, 35)

    def test_iterate_empty_holes(self):
        board = Board()
        board.holes[0].empty = False
        board.holes[15].empty = False
        count = 0
        for empty_hole in board.empties:
            self.assertTrue(empty_hole.empty)
            count += 1
        self.assertEqual(count, 33)

    def test_place_piece_in_hole1(self):
        part1 = Part()
        part2 = Part(Orientation.E)
        part3 = Part(Orientation.E)
        part4 = Part(Orientation.E)
        part5 = Part(Orientation.SW)

        piece = PuzzlePiece(part1, part2, part3, part4, part5)
        self.fail("Parts need to be linked, but 'parent' concept makes"
                  " no sense. Given a starting part, need to be able to"
                  " iterate each part in a piece, and discover its"
                  " orientation relative to the previous part.")
        # TODO: a part should support multiple "links" and it doesn't matter
        # which parts are linked to which, they just need to be linked in
        # order for them to be discovered, and to be able to determine their
        # relative orientation based on neighbour part. Perhaps use
        # neighbours concept similar to Hole?

    def test_hole0_neighbours(self):
        board = Board()
        hole1 = board[0]

        self.assertIsNotNone(hole1.neighbours.get(Orientation.E))
        self.assertIsNotNone(hole1.neighbours.get(Orientation.SE))
        self.assertIsNotNone(hole1.neighbours.get(Orientation.SW))
        self.assertIsNone(hole1.neighbours.get(Orientation.W))
        self.assertIsNone(hole1.neighbours.get(Orientation.NW))
        self.assertIsNone(hole1.neighbours.get(Orientation.NE))

    def test_hole15_neighbours(self):
        board = Board()
        hole15 = board[15]

        self.assertIs(hole15.neighbours[Orientation.E], board[16])
        self.assertIs(hole15.neighbours[Orientation.SE], board[21])
        self.assertIs(hole15.neighbours[Orientation.SW], board[20])
        self.assertIs(hole15.neighbours[Orientation.NW], board[9])
        self.assertIs(hole15.neighbours[Orientation.NE], board[10])

    def test_hole23_neighbours(self):
        board = Board()
        hole23 = board[23]

        self.assertIs(hole23.neighbours[Orientation.E], board[24])
        self.assertIs(hole23.neighbours[Orientation.SE], board[29])
        self.assertIs(hole23.neighbours[Orientation.SW], board[28])
        self.assertIs(hole23.neighbours[Orientation.W], board[22])
        self.assertIs(hole23.neighbours[Orientation.NW], board[17])
        self.assertIs(hole23.neighbours[Orientation.NE], board[18])

    def test_hole27_neighbours(self):
        board = Board()
        hole27 = board[27]

        self.assertIs(hole27.neighbours[Orientation.E], board[28])
        self.assertIs(hole27.neighbours[Orientation.SE], board[32])
        self.assertIs(hole27.neighbours[Orientation.SW], board[31])
        self.assertIs(hole27.neighbours[Orientation.W], board[26])
        self.assertIs(hole27.neighbours[Orientation.NW], board[21])
        self.assertIs(hole27.neighbours[Orientation.NE], board[22])

    def test_hole31_neighbours(self):
        board = Board()
        hole31 = board[31]

        self.assertIs(hole31.neighbours[Orientation.E], board[32])
        self.assertIsNone(hole31.neighbours.get(Orientation.SE))
        self.assertIsNone(hole31.neighbours.get(Orientation.SW))
        self.assertIsNone(hole31.neighbours.get(Orientation.W))
        self.assertIs(hole31.neighbours[Orientation.NW], board[26])
        self.assertIs(hole31.neighbours[Orientation.NE], board[27])
