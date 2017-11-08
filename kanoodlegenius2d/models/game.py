from .base import BaseModel


class Game(BaseModel):
    """Represents a single Kanoodle Genius game for a given player."""

    @staticmethod
    def start(player_name):
        """Convenience method which assembles the objects necessary to begin a new game.

        Args:
            player_name:
                The name of the player starting the game.
        """
        from .board import Board
        from .level import Level
        from .player import Player

        game = Game.create()
        player = Player.create(name=player_name, game=game)

        first_puzzle = Level.select()[0].puzzles[0]
        board = Board.create(player=player, puzzle=first_puzzle)  # Creates an empty board referencing player/puzzle
        board.setup(first_puzzle)  # Sets up the noodles on the board based on the puzzle

        return game
