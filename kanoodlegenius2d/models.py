import logging
import os

from peewee import (CharField,
                    FixedCharField,
                    ForeignKeyField,
                    IntegerField,
                    Model,
                    SqliteDatabase)

from kanoodlegenius2d import data
from kanoodlegenius2d import holes
from .orientation import Orientation

_LOG = logging.getLogger(__name__)

database = SqliteDatabase(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))


def initialise():
    """Initialise the database, creating the database tables if they don't already
    exist, and set up initial data.
    """
    global database
    database.connect()

    if not Puzzle.table_exists():
        data.setup()


def shutdown():
    """Shutdown the database, performing any cleanup operations and
    closing the active connection.
    """
    database.close()


class BaseModel(Model):
    """Base model that all concrete model classes should inherit from."""
    class Meta:
        database = database


class Game(BaseModel):
    """Represents a single Kanoodle Genius game for a given player."""

    @staticmethod
    def start(player_name):
        """Convenience method which assembles the objects necessary to begin a new game.

        Args:
            player_name:
                The name of the player starting the game.
        """
        game = Game.create()
        player = Player.create(name=player_name, game=game)

        first_puzzle = Level.select()[0].puzzles[0]
        board = Board.create(player=player, puzzle=first_puzzle)  # Creates an empty board referencing player/puzzle
        board.setup(first_puzzle)  # Sets up the noodles on the board based on the puzzle

        return game


class Level(BaseModel):
    """Represents a level within the game."""
    number = IntegerField()
    name = CharField(max_length=20)

    def __str__(self):
        return '<Level: {} ({})>'.format(self.number, self.name)


class PartPositionMixin:
    def get_part_positions(self, root_position=None):
        """Get the hole positions of each part of the noodle based on the
        root position.

        Args:
            root_position:
                The position of the root part. If not specified the root
                position will be discovered from the subclass.

        Returns:
            A list of the hole position integers representing each part of
            the noodle.
        """
        if root_position is None:
            root_position = getattr(self, 'position')

        positions = [root_position]

        for i in range(1, 5):
            position = holes.find_position(positions[-1], getattr(self, 'part{}'.format(i)))
            if position is None:
                raise PositionUnavailableException('The position for part {} is off the board'.format(i))
            positions.append(position)

        return positions


class Noodle(PartPositionMixin, BaseModel):
    """Represents a noodle - a puzzle piece."""
    designation = FixedCharField(max_length=1)
    colour = CharField()

    # The default orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)

    def rotate(self, increment=1):
        """Rotate the noodle clockwise by the specified number of increments.

        Args:
            increment:
                The number of increments to rotate the noodle by.
        """
        for _ in range(increment):
            self.part1 = Orientation.rotate(self.part1)
            self.part2 = Orientation.rotate(self.part2)
            self.part3 = Orientation.rotate(self.part3)
            self.part4 = Orientation.rotate(self.part4)

    def __str__(self):
        return '<Noodle: {}>'.format(self.colour)


class Player(BaseModel):
    """Represents a player playing the game."""
    game = ForeignKeyField(Game)
    name = CharField(max_length=10)

    def __str__(self):
        return '<Player: {}>'.format(self.name)


class Puzzle(BaseModel):
    """Represents a Kanoodle Genius puzzle, which is basically a
    board preconfigured with some noodles.
    """
    level = ForeignKeyField(Level, 'puzzles')
    number = IntegerField()

    def __str__(self):
        return '<Puzzle: {}>'.format(self.number)


class Board(BaseModel):
    """Represents the board that a player is solving a puzzle on."""
    player = ForeignKeyField(Player, related_name='boards')
    puzzle = ForeignKeyField(Puzzle)

    def place(self, noodle, position):
        """Place a noodle onto the board in the specified position.

        Args:
            noodle:
                The noodle instance to place on the board.
            position:
                The hole position to place the root part of the noodle on to.
                Board hole positions begin at 0.
        Raises:
            PositionOccupiedException:
                If any of the positions targeted by the specified noodle's parts
                are occupied.
        """
        if position not in range(35):
            raise PositionUnavailableException('Position {} is not on the board')

        target_positions = set(noodle.get_part_positions(position))
        board_noodles = BoardNoodle.select().where(BoardNoodle.board == self)

        if board_noodles:
            occupied_positions = set()

            for board_noodle in board_noodles:
                occupied_positions.update(board_noodle.get_part_positions())

            overlap = occupied_positions & target_positions

            if overlap:
                raise PositionUnavailableException('Positions {} are occupied'.format(overlap))

        BoardNoodle.create(board=self, noodle=noodle, position=position, part1=noodle.part1,
                           part2=noodle.part2, part3=noodle.part3, part4=noodle.part4)

    def setup(self, puzzle):
        # Create a BoardNoodle based on each PuzzleNoode
        pass


class BoardNoodle(PartPositionMixin, BaseModel):
    """Represents an instance of a noodle on a player's board."""
    board = ForeignKeyField(Board, related_name='noodles')
    noodle = ForeignKeyField(Noodle)
    # The position of the root part on the board
    position = IntegerField()
    # The orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)

    def __str__(self):
        return '<BoardNoodle: {}>'.format(self.id)


class PuzzleNoodle(PartPositionMixin, BaseModel):
    """Represents an instance of a Noodle preconfigured on a
    puzzle board.
    """
    puzzle = ForeignKeyField(Puzzle, related_name='noodles')
    noodle = ForeignKeyField(Noodle)
    # The position of the root part on the puzzle
    position = IntegerField()
    # The orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)

    def __str__(self):
        return '<PuzzleNoodle: {}>'.format(self.id)


class PositionUnavailableException(Exception):
    """Indicates that a position on the board is occupied (in use by another noodle)
    or the position itself is not on the board.
    """
