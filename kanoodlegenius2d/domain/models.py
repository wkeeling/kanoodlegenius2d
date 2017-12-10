import logging
import os
from datetime import datetime

from peewee import (BooleanField,
                    CharField,
                    DateTimeField,
                    FixedCharField,
                    ForeignKeyField,
                    IntegerField,
                    IntegrityError,
                    Model,
                    SqliteDatabase)

from kanoodlegenius2d.domain import data
from kanoodlegenius2d.domain import holes
from kanoodlegenius2d.domain import orientation

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
    last_played = DateTimeField(default=datetime.now())

    @gproperty
    def player(self):
        """Convenience method for getting the game for a player.

        Although Game -> Player is technically a one to many relationship,
        a game only ever has a single player and so the relationship is
        effectively one to one.

        Returns:
            The Player instance for the game.
        """
        return self.player_set[0]

    @staticmethod
    def start(player_name):
        """Convenience method which assembles the objects necessary to begin a new game.

        Args:
            player_name: The name of the player starting the game.
        Returns:
            The board instance preconfigured with noodles, and ready to go.
        """
        game = Game.create()

        try:
            player = Player.create(name=player_name, game=game)
        except IntegrityError:
            raise DuplicatePlayerNameException(player_name)

        first_puzzle = Puzzle.get(Puzzle.number == 1)
        board = Board.create(player=player, puzzle=first_puzzle)  # Creates an empty board referencing player/puzzle
        board.setup()  # Sets up the noodles on the board based on the puzzle

        return board

    @staticmethod
    def resume(player):
        """Convenience method to resume a previous game for a player.

        Args:
            player: An instance of the Player resuming the game.
        Returns:
            The board instance holding the previous state of the game.
        """
        boards = player.boards.order_by(Board.id)
        return boards[-1]

    @staticmethod
    def by_last_played():
        """Get all games in reverse chronological order of last played (so
        most recent first.

        Returns:
            An iterator of games ordered by reverse chronological order of last played.
        """
        return Game.select().order_by(-Game.last_played)


class Level(BaseModel):
    """Represents a level within the game."""
    number = IntegerField()
    name = CharField(max_length=20)

    def __str__(self):
        return '<Level: {} ({})>'.format(self.number, self.name)


class PartAccessorMixin:

    @property
    def parts(self):
        """Convenience property for accessing the parts.

         Returns:
             A tuple of the parts.
         """
        return self.part1, self.part2, self.part3, self.part4

    def get_part_positions(self, root_position=None):
        """Get the hole positions of each part of the noodle based on the
        root position.

        Args:
            root_position: The position of the root part. If not specified the root
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


class Noodle(PartAccessorMixin, BaseModel):
    """Represents a noodle - a puzzle piece."""

    designation = FixedCharField(max_length=1)
    colour = CharField()

    # The default orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)

    @staticmethod
    def light_green():
        return Noodle.get(Noodle.designation == 'A')

    @staticmethod
    def yellow():
        return Noodle.get(Noodle.designation == 'B')

    @staticmethod
    def dark_blue():
        return Noodle.get(Noodle.designation == 'C')

    @staticmethod
    def light_blue():
        return Noodle.get(Noodle.designation == 'D')

    @staticmethod
    def red():
        return Noodle.get(Noodle.designation == 'E')

    @staticmethod
    def pink():
        return Noodle.get(Noodle.designation == 'F')

    @staticmethod
    def dark_green():
        return Noodle.get(Noodle.designation == 'G')

    def rotate(self, increment=1):
        """Rotate the noodle clockwise by the specified number of increments.

        Args:
            increment: The number of increments to rotate the noodle by.
        """
        for _ in range(increment):
            self.part1 = orientation.rotate(self.part1)
            self.part2 = orientation.rotate(self.part2)
            self.part3 = orientation.rotate(self.part3)
            self.part4 = orientation.rotate(self.part4)

    def flip(self):
        """Flip the noodle 180 degrees on its Y axis."""

        y_conversions = {
            orientation.SE: orientation.SW,
            orientation.NE: orientation.NW,
            orientation.NW: orientation.NE,
            orientation.SW: orientation.SE,
            orientation.E: orientation.W,
            orientation.W: orientation.E
        }
        self.part1 = y_conversions[self.part1]
        self.part2 = y_conversions[self.part2]
        self.part3 = y_conversions[self.part3]
        self.part4 = y_conversions[self.part4]

    def __str__(self):
        return '<Noodle: {}>'.format(self.colour)


class Player(BaseModel):
    """Represents a player playing the game."""

    game = ForeignKeyField(Game)
    name = CharField(max_length=10, unique=True)
    deleted = BooleanField(default=False)

    @staticmethod
    def active_players():
        """Get players that have not been soft deleted.

        Return:
            A queryset of players.
        """
        return Player.select().where(Player.deleted == False)

    def soft_delete(self):
        """Mark a player as deleted, but do not physically delete the
        database record.
        """
        self.deleted = True
        self.save()

    def __str__(self):
        return '<Player: {}>'.format(self.name)


class Puzzle(BaseModel):
    """Represents a Kanoodle Genius puzzle, which is basically a
    board preconfigured with some noodles.
    """
    level = ForeignKeyField(Level, related_name='puzzles')
    number = IntegerField()

    def place(self, noodle, *, position):
        """Place the specified noodle onto the puzzle at the specified position.

        Args:
            noodle: The noodle to place on the puzzle.
            position: The puzzle position to place the noodle's root part onto.
        """
        PuzzleNoodle.create(puzzle=self, noodle=noodle, position=position,
                            part1=noodle.part1,
                            part2=noodle.part2,
                            part3=noodle.part3,
                            part4=noodle.part4)

    def next_puzzle(self):
        """Get the next puzzle.

        Returns:
            The next puzzle, or None if no next puzzle (end of game).
        """
        try:
            return Puzzle.get(Puzzle.number == self.number+1)
        except Puzzle.DoesNotExist:
            # End of game
            return None

    def __str__(self):
        return '<Puzzle: {}>'.format(self.number)


class Board(BaseModel):
    """Represents the board that a player is solving a puzzle on."""
    player = ForeignKeyField(Player, related_name='boards')
    puzzle = ForeignKeyField(Puzzle)

    def place(self, noodle, *, position):
        """Place a noodle onto the board in the specified position.

        Args:
            noodle: The noodle instance to place on the board.
            position: The hole position to place the root part of the noodle on to.
                Board hole positions begin at 0.
        Raises:
            PositionOccupiedException: If any of the positions targeted by the specified
                noodle's parts are occupied.
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
                raise PositionUnavailableException('Position(s) {} are occupied'.format(
                    ', '.join([str(o) for o in overlap])))

        BoardNoodle.create(board=self, noodle=noodle, position=position, part1=noodle.part1,
                           part2=noodle.part2, part3=noodle.part3, part4=noodle.part4)
        self.player.game.last_played = datetime.now()
        self.player.game.save()

    def setup(self):
        """Set up the board based on the puzzle it is referencing.

        The puzzle acts as a template.
        """
        for puzzle_noodle in self.puzzle.noodles:
            noodle = puzzle_noodle.noodle
            noodle.part1 = puzzle_noodle.part1
            noodle.part2 = puzzle_noodle.part2
            noodle.part3 = puzzle_noodle.part3
            noodle.part4 = puzzle_noodle.part4
            self.place(noodle, position=puzzle_noodle.position)

    def undo(self):
        """Undo the last place operation.

        Returns:
            The noodle that was undone (removed from the board)
            or None if there was no operation to undo.
        """
        puzzle_noodles = [noodle.noodle for noodle in self.puzzle.noodles]
        for board_noodle in self.noodles.order_by(BoardNoodle.id.desc()):
            if board_noodle.noodle not in puzzle_noodles:
                board_noodle.delete_instance()
                return board_noodle.noodle

    @property
    def complete(self):
        """Whether the puzzle has been completed.

        Returns:
            True if the puzzle is complete, False otherwise.
        """
        return self.noodles.count() == 7

    def __str__(self):
        return '<Board: {}, Puzzle: {}, Level: {}>'.format(self.id, self.puzzle.id, self.puzzle.level.id)


class BoardNoodle(PartAccessorMixin, BaseModel):
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


class PuzzleNoodle(PartAccessorMixin, BaseModel):
    """Represents an instance of a noodle preconfigured on a
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


class DuplicatePlayerNameException(Exception):
    """Raised when an attempt is made to create a new player with the same name
    as an existing player.
    """


class PositionUnavailableException(Exception):
    """Indicates that a position on the board is occupied (in use by another noodle)
    or the position itself is not on the board.
    """
