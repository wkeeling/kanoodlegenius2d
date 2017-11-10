import logging
import os

from peewee import (CharField,
                    FixedCharField,
                    ForeignKeyField,
                    IntegerField,
                    Model,
                    SqliteDatabase)

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

    # Create the tables if they do not already exist
    for k, v in globals().items():
        if isinstance(v, type) and issubclass(v, BaseModel):
            _LOG.debug('Creating table {}'.format(k))
            getattr(v, 'create_table')(fail_silently=True)  # Don't error if the tables already exist

    # Set up the initial data where is does not already exist
    Noodle.create(designation='A', code='light_green',
                  part1=Orientation.SE,
                  part2=Orientation.NE,
                  part3=Orientation.E,
                  part4=Orientation.NE)
    Noodle.create(designation='B', code='yellow',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NW,
                  part4=Orientation.E)
    Noodle.create(designation='C', code='dark_blue',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NE,
                  part4=Orientation.NE)
    Noodle.create(designation='D', code='light_blue',
                  part1=Orientation.E,
                  part2=Orientation.E,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='E', code='red',
                  part1=Orientation.NE,
                  part2=Orientation.SE,
                  part3=Orientation.NE,
                  part4=Orientation.SE)
    Noodle.create(designation='G', code='dark_green',
                  part1=Orientation.NE,
                  part2=Orientation.SE,
                  part3=Orientation.E,
                  part4=Orientation.NE)
    Noodle.create(designation='F', code='pink',
                  part1=Orientation.NE,
                  part2=Orientation.NW,
                  part3=Orientation.E,
                  part4=Orientation.NE)

    level1 = Level.create(number=1, name='Super Pro')
    level2 = Level.create(number=2, name='Champ')
    level3 = Level.create(number=3, name='Whiz')

    puzzle = Puzzle.create(level=level1, number=1)
    light_blue = Noodle.get(Noodle.code == 'light_blue')
    light_blue.rotate(increment=3)
    puzzle.place(light_blue, position=3)


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
            root_position = self.position
        positions = [root_position]
        positions.append(holes.find_position(positions[-1], self.part1))
        positions.append(holes.find_position(positions[-1], self.part2))
        positions.append(holes.find_position(positions[-1], self.part3))
        positions.append(holes.find_position(positions[-1], self.part4))

        return positions


class Noodle(PartPositionMixin, BaseModel):
    """Represents a noodle - a puzzle piece."""
    designation = FixedCharField(max_length=1)
    code = CharField()

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

    def place(self, noodle, position):
        """Place a noodle onto the puzzle in the specified position.

        Args:
            noodle:
                The noodle instance to place on the puzzle.
            position:
                The hole position to place the root part of the noodle on to.
                Board hole positions begin at 0.
        Raises:
            PositionOccupiedException:
                If any of the positions targeted by the specified noodle's parts
                are occupied.
        """
        puzzle_noodles = PuzzleNoodle.select().where(PuzzleNoodle.puzzle == self)
        if puzzle_noodles:
            occupied_positions = set()
            for puzzle_noodle in puzzle_noodles:
                occupied_positions.update(puzzle_noodle.get_part_positions())
            overlap = occupied_positions & set(noodle.get_part_positions(position))
            if overlap:
                raise PositionUnavailableException('Positions {} are occupied'.format(overlap))
        PuzzleNoodle.create(puzzle=self, noodle=noodle, position=position, part1=noodle.part1,
                            part2=noodle.part2, part3=noodle.part3, part4=noodle.part4)


class Board(BaseModel):
    """Represents the board that a player is solving a puzzle on."""
    player = ForeignKeyField(Player, related_name='boards')
    puzzle = ForeignKeyField(Puzzle)

    def setup(self, puzzle):
        # Create a BoardNoodle based on each PuzzleNoode
        pass


class BoardNoodle(BaseModel):
    """Represents an instance of a noodle on a player's board."""
    board = ForeignKeyField(Board, related_name='noodles')
    noodle = ForeignKeyField(Noodle)


class PuzzleNoodle(PartPositionMixin, BaseModel):
    """Represents an instance of a Noodle preconfigured on a
    puzzle board.
    """
    puzzle = ForeignKeyField(Puzzle, related_name='noodles')
    noodle = ForeignKeyField(Noodle)
    # The position of the root part on the puzzle board
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
