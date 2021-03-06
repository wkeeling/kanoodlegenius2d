import os
import sqlite3
from unittest import TestCase

from peewee import IntegrityError

from kanoodlegenius2d.domain import orientation
from kanoodlegenius2d.domain.models import (Board,
                                            BoardNoodle,
                                            DuplicatePlayerNameException,
                                            Game,
                                            initialise,
                                            Level,
                                            Noodle,
                                            Player,
                                            Puzzle,
                                            PuzzleNoodle,
                                            PositionUnavailableException,
                                            shutdown)
from tests.domain.common import ModelTestCase


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


class GameIntegrationTest(TestCase):

    def test_start_new_game(self):
        """Test assemble the model objects needed to begin a new game."""
        board = Game.start('test_player')

        dark_blue = Noodle.dark_blue()
        board.place(dark_blue, position=32)  # Placed OK

        yellow = Noodle.yellow()
        yellow.rotate(increment=2)
        try:
            board.place(yellow, position=7)  # Not placed OK
        except PositionUnavailableException:
            pass

        board_noodles = board.noodles
        self.assertEqual(len(board_noodles), 5)

    def test_start_new_game_sets_last_played(self):
        """Test that the last played date is set when a new game is started."""
        board = Game.start('test_player')

        self.assertIsNotNone(board.player.game.last_played)

    def test_start_new_game_raises_exception_when_player_name_taken(self):
        """Test that an exception is raised when a new game is started with
        a player name that has already been used.
        """
        Game.start('test_player')

        with self.assertRaises(DuplicatePlayerNameException):
            Game.start('test_player')

    def test_start_new_game_rolls_back_transaction_when_player_name_taken(self):
        """Test that the transaction is rolled back (game not created) when
        a game is started with a player name that has already been used.
        """
        Game.start('test_player')

        try:
            Game.start('test_player')
        except DuplicatePlayerNameException:
            self.assertEqual(Game.select().count(), 1)

    def test_complete_puzzle_1(self):
        """Test complete the first puzzle, checking that the board
        indicates that the puzzle was completed successfully.
        """
        board = Game.start('test_player')

        dark_blue = Noodle.dark_blue()
        board.place(dark_blue, position=32)
        pink = Noodle.pink()
        pink.rotate(5)
        board.place(pink, position=29)
        yellow = Noodle.yellow()
        yellow.flip()
        yellow.rotate(increment=2)
        board.place(yellow, position=17)

        self.assertTrue(board.completed)

    def test_complete_game(self):
        """Test that the game indicates that it is fully complete."""
        self.fail('Implement')

    def test_get_games_ordered_by_last_played(self):
        """Test that the games a listed in reverse chronological
        order of last played.
        """
        board1 = Game.start('player1')
        board2 = Game.start('player2')

        games = list(Game.by_last_played())

        self.assertEqual(games, [board2.player.game, board1.player.game])

    def test_last_played(self):
        """Test that the last played date is set on a game when a
        player places a piece on the board.
        """
        board = Game.start('test_player')
        first_played = board.player.game.last_played  # Set when the game was started

        dark_blue = Noodle.dark_blue()
        board.place(dark_blue, position=32)

        self.assertNotEqual(board.player.game.last_played, first_played)

    def test_resume_game(self):
        """Test that the game can be resumed for a player."""
        board1 = Game.start('player1')
        dark_blue = Noodle.dark_blue()
        board1.place(dark_blue, position=32)

        board2 = Game.start('player2')
        dark_blue = Noodle.dark_blue()
        board2.place(dark_blue, position=32)

        player1 = Player.get(Player.name == 'player1')
        self.assertEqual(Game.resume(player1), board1)

    def setUp(self):
        self._datafile_path = os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db')
        initialise()

    def tearDown(self):
        shutdown()
        try:
            os.remove(self._datafile_path)
        except OSError:
            pass


class NoodleTest(ModelTestCase):

    requires = (Noodle, )

    def test_rotate_noodle_single_increment(self):
        Noodle.create(designation='D', colour='light_blue',
                      part1=orientation.E,
                      part2=orientation.E,
                      part3=orientation.NE,
                      part4=orientation.SE)

        light_blue = Noodle.light_blue()
        light_blue.rotate()

        self.assertEqual(light_blue.part1, orientation.SE)
        self.assertEqual(light_blue.part2, orientation.SE)
        self.assertEqual(light_blue.part3, orientation.E)
        self.assertEqual(light_blue.part4, orientation.SW)

    def test_rotate_noodle_multiple_increments(self):
        Noodle.create(designation='D', colour='light_blue',
                      part1=orientation.E,
                      part2=orientation.E,
                      part3=orientation.NE,
                      part4=orientation.SE)

        light_blue = Noodle.light_blue()
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


class BoardTest(ModelTestCase):

    requires = (Game, Player, Board, Level, Puzzle, PuzzleNoodle, BoardNoodle, Noodle)

    def test_setup(self):
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')
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
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')

        board.place(light_blue, position=5)

        board_noodle = BoardNoodle.get(BoardNoodle.position == 5)
        self.assertEqual(board_noodle.part1, light_blue.part1)
        self.assertEqual(board_noodle.part2, light_blue.part2)
        self.assertEqual(board_noodle.part3, light_blue.part3)
        self.assertEqual(board_noodle.part4, light_blue.part4)

    def test_place_noodle_specific_part(self):
        """Test place a noodle onto the board supplying the specific noodle
        part that should be placed.
        """
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')

        pos = board.place(light_blue, position=3, part_pos=3)

        self.assertEqual(pos, 5)
        board_noodle = BoardNoodle.get(BoardNoodle.position == 5)
        self.assertEqual(board_noodle.part1, light_blue.part1)
        self.assertEqual(board_noodle.part2, light_blue.part2)
        self.assertEqual(board_noodle.part3, light_blue.part3)
        self.assertEqual(board_noodle.part4, light_blue.part4)

    def test_place_noodle_specific_part_raises_exception_when_off_board(self):
        """Test place a noodle onto the board supplying the specific noodle
        part that should be placed, but part of the noodle is off the board.
        """
        board = self._create_board()
        light_blue = Noodle.create(designation='D', colour='light_blue',
                                   part1=orientation.E,
                                   part2=orientation.E,
                                   part3=orientation.NE,
                                   part4=orientation.SE)

        with self.assertRaises(PositionUnavailableException) as ctx:
            board.place(light_blue, position=0, part_pos=3)
        self.assertEqual(str(ctx.exception), 'Part 1 of the noodle is not on the board')

    def test_place_raises_exception_when_root_position_occupied(self):
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')
        yellow = Noodle.get(Noodle.designation == 'B')

        board.place(light_blue, position=5)

        with self.assertRaises(PositionUnavailableException):
            board.place(yellow, position=5)

    def test_place_raises_exception_when_child_position_occupied(self):
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')
        yellow = Noodle.get(Noodle.designation == 'B')

        board.place(light_blue, position=5)

        with self.assertRaises(PositionUnavailableException):
            board.place(yellow, position=11)

    def test_place_raises_exception_when_root_position_off_board(self):
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')

        with self.assertRaises(PositionUnavailableException):
            board.place(light_blue, position=37)

    def test_place_raises_exception_when_child_position_off_board(self):
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')

        with self.assertRaises(PositionUnavailableException):
            board.place(light_blue, position=0)

    def test_undo_place(self):
        """Test that the previous place noodle action can be undone."""
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')
        board.puzzle.place(light_blue, position=5)
        yellow = Noodle.get(Noodle.designation == 'B')

        board.place(yellow, position=20)

        BoardNoodle.get(BoardNoodle.position == 20)  # Should not raise a DoesNotExist

        noodle = board.undo()

        self.assertEqual(noodle, yellow)
        with self.assertRaises(BoardNoodle.DoesNotExist):
            BoardNoodle.get(BoardNoodle.position == 20)  # Noodle has been removed so will raise DoesNotExist

    def test_undo_no_place_does_nothing(self):
        """Test that attempting to undo when no place has occurred does nothing."""
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')

        board.puzzle.place(light_blue, position=5)

        noodle = board.undo()  # Nothing to undo, because undo does not remove puzzle noddles (only board noodles)

        self.assertIsNone(noodle)
        PuzzleNoodle.get(PuzzleNoodle.position == 5)  # Should not raise a DoesNotExist

    def test_undo_place_updates_last_played(self):
        """Test that the undo function will update the last_played date on the Game instance."""
        board = self._create_board()
        light_blue = Noodle.get(Noodle.designation == 'D')
        board.puzzle.place(light_blue, position=5)
        yellow = Noodle.get(Noodle.designation == 'B')
        board.place(yellow, position=20)
        last_played = board.player.game.last_played

        board.undo()

        self.assertNotEqual(board.player.game.last_played, last_played)

    def test_solve(self):
        board = self._create_board()
        self._configure_puzzle(board.puzzle)
        board.setup()

        board.solve()

        self.assertTrue(board.completed)
        self.assertTrue(board.auto_completed)
        noodles = {noodle.position: noodle for noodle in board.noodles}
        self.assertEqual(noodles[29].part1, orientation.NE)
        self.assertEqual(noodles[29].part2, orientation.NW)
        self.assertEqual(noodles[29].part3, orientation.E)
        self.assertEqual(noodles[29].part4, orientation.NE)
        self.assertEqual(noodles[17].part1, orientation.NE)
        self.assertEqual(noodles[17].part2, orientation.E)
        self.assertEqual(noodles[17].part3, orientation.NW)
        self.assertEqual(noodles[17].part4, orientation.E)
        self.assertEqual(noodles[32].part1, orientation.E)
        self.assertEqual(noodles[32].part2, orientation.E)
        self.assertEqual(noodles[32].part3, orientation.NE)
        self.assertEqual(noodles[32].part4, orientation.NE)

    def _create_board(self):
        level = Level.create(number=1, name='test level')
        puzzle = Puzzle.create(
            level=level,
            number=1,
            solution='3,32,E,E,NE,NE;6,29,NE,NW,E,NE;2,17,NE,E,NW,E;'
        )
        game = Game.create()
        player = Player.create(name='test', game=game)
        board = Board.create(player=player, puzzle=puzzle)

        return board

    def _configure_puzzle(self, puzzle):
        light_blue = Noodle.light_blue()
        light_blue.rotate(increment=3)
        puzzle.place(light_blue, position=3)

        dark_green = Noodle.dark_green()
        puzzle.place(dark_green, position=9)

        light_green = Noodle.light_green()
        light_green.flip()
        light_green.rotate(increment=3)
        puzzle.place(light_green, position=15)

        red = Noodle.red()
        red.rotate()
        puzzle.place(red, position=20)

    def setUp(self):
        super().setUp()
        Noodle.create(designation='A', colour='#00e600',
                      part1=orientation.E,
                      part2=orientation.NE,
                      part3=orientation.NE,
                      part4=orientation.SE)
        Noodle.create(designation='B', colour='#ffff00',
                      part1=orientation.E,
                      part2=orientation.NE,
                      part3=orientation.SE,
                      part4=orientation.NE)
        Noodle.create(designation='C', colour='#000099',
                      part1=orientation.E,
                      part2=orientation.E,
                      part3=orientation.NE,
                      part4=orientation.NE)
        Noodle.create(designation='D', colour='#00ccff',
                      part1=orientation.E,
                      part2=orientation.E,
                      part3=orientation.NE,
                      part4=orientation.SE)
        Noodle.create(designation='E', colour='#e60000',
                      part1=orientation.NE,
                      part2=orientation.SE,
                      part3=orientation.NE,
                      part4=orientation.SE)
        Noodle.create(designation='F', colour='#ff00ff',
                      part1=orientation.E,
                      part2=orientation.NE,
                      part3=orientation.SE,
                      part4=orientation.E)
        Noodle.create(designation='G', colour='#004d00',
                      part1=orientation.NE,
                      part2=orientation.SE,
                      part3=orientation.E,
                      part4=orientation.NE)


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


class PlayerTest(ModelTestCase):

    requires = (Game, Player, Board, BoardNoodle, Level, Puzzle, Noodle)

    def test_player_with_same_name_raises_exception(self):
        # with test_database(test_db, (Game, Player)):
        game = Game.create()
        Player.create(name='test player', game=game)
        game = Game.create()
        with self.assertRaises(IntegrityError):
            Player.create(name='test player', game=game)

    def test_delete_player(self):
        """Test that a player is soft deleted."""
        game = Game.create()
        player = Player.create(name='test player', game=game)
        player.soft_delete()

        deleted_players = Player.select(Player.deleted == True).count()
        self.assertEqual(deleted_players, 1)

    def test_delete_player_named_updated(self):
        """Test that when a player is soft deleted, that the name is updated."""
        game = Game.create()
        player = Player.create(name='test player', game=game)
        player.soft_delete()

        deleted_player = Player.get(Player.deleted == True)
        self.assertTrue(deleted_player.name.startswith('test player_deleted_'))

    def test_get_active_players(self):
        game = Game.create()
        Player.create(name='test player', game=game).soft_delete()

        game = Game.create()
        Player.create(name='test player 1', game=game)

        game = Game.create()
        Player.create(name='test player 2', game=game)

        active_players = Player.active_players()

        self.assertEqual(len(active_players), 2)
        names = [player.name for player in active_players]
        self.assertIn('test player 1', names)
        self.assertIn('test player 2', names)

    def test_get_puzzles_completed(self):
        game = Game.create()
        player = Player.create(game=game, name='Test')
        level = Level.create(number=1, name='Level 1')
        Noodle.create(designation='A', colour='yellow', part1='NE', part2='SE', part3='E', part4='W')

        # Configure 2 complete boards
        for n in range(2):
            puzzle = Puzzle.create(level=level, number=n)
            board = Board.create(player=player, puzzle=puzzle)
            for p in range(7):
                BoardNoodle.create(board=board, noodle=Noodle.get(designation='A'), position=p,
                                   part1='NE', part2='SE', part3='E', part4='W')

        # Configure 1 incomplete board
        puzzle = Puzzle.create(level=level, number=2)
        board = Board.create(player=player, puzzle=puzzle)
        for p in range(6):
            BoardNoodle.create(board=board, noodle=Noodle.get(designation='A'), position=p,
                               part1='NE', part2='SE', part3='E', part4='W')

        completed = player.puzzles_completed

        self.assertEqual(completed.player_completed, 2)
        self.assertEqual(len(player.boards), 3)


class PuzzleTest(ModelTestCase):

    requires = (Level, Puzzle)

    def test_next_puzzle(self):
        level = Level.create(number=1, name='Super Pro')
        puzzle1 = Puzzle.create(level=level, number=1)
        puzzle2 = Puzzle.create(level=level, number=2)

        self.assertEqual(puzzle1.next_puzzle(), puzzle2)

    def test_no_next_puzzle(self):
        level = Level.create(number=1, name='Super Pro')
        Puzzle.create(level=level, number=1)
        puzzle2 = Puzzle.create(level=level, number=2)

        self.assertIsNone(puzzle2.next_puzzle())

    def test_next_puzzle_new_level(self):
        level1 = Level.create(number=1, name='Super Pro')
        level2 = Level.create(number=2, name='Champ')
        Puzzle.create(level=level1, number=1)
        puzzle2 = Puzzle.create(level=level1, number=2)
        puzzle3 = Puzzle.create(level=level2, number=1)

        self.assertEqual(puzzle2.next_puzzle(), puzzle3)
