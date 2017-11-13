import os
import sqlite3
from unittest import TestCase

from peewee import SqliteDatabase
from playhouse.test_utils import test_database

from kanoodlegenius2d.models import (Board,
                                     BoardNoodle,
                                     Game,
                                     initialise,
                                     Level,
                                     Noodle,
                                     Player,
                                     Puzzle,
                                     PuzzleNoodle,
                                     PositionUnavailableException,
                                     shutdown)
from kanoodlegenius2d import orientation

test_db = SqliteDatabase(':memory:')


class InitialiseTest(TestCase):

    def test_initialise_database(self):
        initialise()
        self.assertTrue(os.path.exists(self._datafile_path))
        conn = sqlite3.connect(self._datafile_path)
        tables = [t[0] for t in conn.execute("SELECT name FROM sqlite_master WHERE type='table';")]
        self.assertIn('puzzle', tables)

    def setUp(self):
        self._datafile_path = os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db')

    def tearDown(self):
        shutdown()
        try:
            os.remove(self._datafile_path)
        except OSError:
            pass


class StartNewGameTest(TestCase):

    def test_start_new_game(self):
        """Test assemble the model objects needed to begin a new game."""
        board = Game.start('test_player')

    def setUp(self):
        self._datafile_path = os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db')
        initialise()

    def tearDown(self):
        shutdown()
        try:
            os.remove(self._datafile_path)
        except OSError:
            pass


class NoodleTest(TestCase):

    def test_rotate_noodle_single_increment(self):
        with test_database(test_db, (Noodle,), create_tables=True):
            Noodle.create(designation='D', colour='light_blue',
                          part1=orientation.E,
                          part2=orientation.E,
                          part3=orientation.NE,
                          part4=orientation.SE)

            light_blue = Noodle.get(Noodle.colour == 'light_blue')
            light_blue.rotate()

            self.assertEqual(light_blue.part1, orientation.SE)
            self.assertEqual(light_blue.part2, orientation.SE)
            self.assertEqual(light_blue.part3, orientation.E)
            self.assertEqual(light_blue.part4, orientation.SW)

    def test_rotate_noodle_multiple_increments(self):
        with test_database(test_db, (Noodle,), create_tables=True):
            Noodle.create(designation='D', colour='light_blue',
                          part1=orientation.E,
                          part2=orientation.E,
                          part3=orientation.NE,
                          part4=orientation.SE)

            light_blue = Noodle.get(Noodle.colour == 'light_blue')
            light_blue.rotate(3)

            self.assertEqual(light_blue.part1, orientation.W)
            self.assertEqual(light_blue.part2, orientation.W)
            self.assertEqual(light_blue.part3, orientation.SW)
            self.assertEqual(light_blue.part4, orientation.NW)

    def test_get_part_positions(self):
        noodle = Noodle(designation='D', code='light_blue',
                        part1=orientation.E,
                        part2=orientation.E,
                        part3=orientation.NE,
                        part4=orientation.SE)

        positions = noodle.get_part_positions(5)

        self.assertEqual(positions, [5, 6, 7, 3, 8])

    def test_flip(self):
        noodle = Noodle(designation='D', code='light_blue',
                        part1=orientation.E,
                        part2=orientation.E,
                        part3=orientation.NE,
                        part4=orientation.SE)

        noodle.flip()

        self.assertEqual(noodle.part1, orientation.W)
        self.assertEqual(noodle.part2, orientation.W)
        self.assertEqual(noodle.part3, orientation.NW)
        self.assertEqual(noodle.part4, orientation.SW)


class BoardTest(TestCase):

    def test_setup(self):
        with test_database(test_db, (Game, Player, Board, Level, Puzzle, PuzzleNoodle, BoardNoodle, Noodle),
                           create_tables=True):
            board = self._create_board()
            light_blue = Noodle.create(designation='D', colour='light_blue',
                                       part1=orientation.E,
                                       part2=orientation.E,
                                       part3=orientation.NE,
                                       part4=orientation.SE)
            light_blue.rotate(increment=3)
            board.puzzle.place(light_blue, position=3)
            board.setup()

            self.assertEqual(len(board.noodles), 1)
            self.assertEqual(board.noodles[0].id, 1)
            self.assertEqual(board.noodles[0].part1, orientation.W)
            self.assertEqual(board.noodles[0].part2, orientation.W)
            self.assertEqual(board.noodles[0].part3, orientation.SW)
            self.assertEqual(board.noodles[0].part4, orientation.NW)

    def test_place_noodle(self):
        with test_database(test_db, (Game, Player, Board, Level, Puzzle, BoardNoodle, Noodle), create_tables=True):
            board = self._create_board()
            light_blue = Noodle.create(designation='D', colour='light_blue',
                                       part1=orientation.E,
                                       part2=orientation.E,
                                       part3=orientation.NE,
                                       part4=orientation.SE)

            board.place(light_blue, 5)

            board_noodle = BoardNoodle.get(BoardNoodle.position == 5)
            self.assertEqual(board_noodle.part1, light_blue.part1)
            self.assertEqual(board_noodle.part2, light_blue.part2)
            self.assertEqual(board_noodle.part3, light_blue.part3)
            self.assertEqual(board_noodle.part4, light_blue.part4)

    def test_place_raises_exception_when_root_position_occupied(self):
        with test_database(test_db, (Game, Player, Board, Level, Puzzle, BoardNoodle, Noodle), create_tables=True):
            board = self._create_board()
            light_blue = Noodle.create(designation='D', colour='light_blue',
                                       part1=orientation.E,
                                       part2=orientation.E,
                                       part3=orientation.NE,
                                       part4=orientation.SE)
            yellow = Noodle.create(designation='B', colour='yellow',
                                   part1=orientation.E,
                                   part2=orientation.NE,
                                   part3=orientation.SE,
                                   part4=orientation.NE)
            board.place(light_blue, 5)

            with self.assertRaises(PositionUnavailableException):
                board.place(yellow, 5)

    def test_place_raises_exception_when_child_position_occupied(self):
        with test_database(test_db, (Game, Player, Board, Level, Puzzle, BoardNoodle, Noodle), create_tables=True):
            board = self._create_board()
            light_blue = Noodle.create(designation='D', colour='light_blue',
                                       part1=orientation.E,
                                       part2=orientation.E,
                                       part3=orientation.NE,
                                       part4=orientation.SE)
            yellow = Noodle.create(designation='B', colour='yellow',
                                   part1=orientation.E,
                                   part2=orientation.E,
                                   part3=orientation.NW,
                                   part4=orientation.E)
            board.place(light_blue, 5)

            with self.assertRaises(PositionUnavailableException):
                board.place(yellow, 11)

    def test_place_raises_exception_when_root_position_off_board(self):
        with test_database(test_db, (Game, Player, Board, Level, Puzzle, BoardNoodle, Noodle), create_tables=True):
            board = self._create_board()
            light_blue = Noodle.create(designation='D', colour='light_blue',
                                       part1=orientation.E,
                                       part2=orientation.E,
                                       part3=orientation.NE,
                                       part4=orientation.SE)

            with self.assertRaises(PositionUnavailableException):
                board.place(light_blue, 37)

    def test_place_raises_exception_when_child_position_off_board(self):
        with test_database(test_db, (Game, Player, Board, Level, Puzzle, BoardNoodle, Noodle), create_tables=True):
            board = self._create_board()
            light_blue = Noodle.create(designation='D', colour='light_blue',
                                       part1=orientation.E,
                                       part2=orientation.E,
                                       part3=orientation.NE,
                                       part4=orientation.SE)

            with self.assertRaises(PositionUnavailableException):
                board.place(light_blue, 0)

    def _create_board(self):
        level = Level.create(number=1, name='test level')
        puzzle = Puzzle.create(level=level, number=1)
        game = Game.create()
        player = Player.create(name='test', game=game)
        board = Board.create(player=player, puzzle=puzzle)

        return board


class PuzzleNoodleTest(TestCase):

    def test_get_part_positions(self):
        puzzle_noodle = PuzzleNoodle(position=5,
                                     part1=orientation.E,
                                     part2=orientation.E,
                                     part3=orientation.NE,
                                     part4=orientation.SE)

        positions = puzzle_noodle.get_part_positions()

        self.assertEqual(positions, [5, 6, 7, 3, 8])


class BoardNoodleTest(TestCase):

    def test_get_part_positions(self):
        board_noodle = BoardNoodle(position=5,
                                   part1=orientation.E,
                                   part2=orientation.E,
                                   part3=orientation.NE,
                                   part4=orientation.SE)

        positions = board_noodle.get_part_positions()

        self.assertEqual(positions, [5, 6, 7, 3, 8])
