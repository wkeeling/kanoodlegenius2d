import tkinter as tk

from kanoodlegenius2d.domain.models import Board, Game, Puzzle
from kanoodlegenius2d.ui import settings
from kanoodlegenius2d.ui.components import CanvasButton, Dialog, PlayerPaginator


class SelectPlayerScreen(tk.Frame):
    """The screen where an existing player can be selected."""

    def __init__(self, onselect, onexit, master=None, **kwargs):
        """Initialise a new SelectPlayerScreen frame.

        Args:
            onselect: Callback that will be called when a new player is selected. This
                will be passed a single argument - the board instance for the player.
            onexit: No-args callback that will be called when the exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        super().__init__(master, width=800, height=480, bg='#000000', highlightthickness=2, **kwargs)

        self._onselect = onselect
        self._onexit = onexit

        self._init_title()
        self._paginator = PlayerPaginator([game.player for game in Game.by_last_played() if not game.player.deleted])
        self._init_player_list()
        self._init_exit()

    def _init_title(self):
        args = {
            'width': 800,
            'height': 100,
            'bg': '#000000'
        }
        title_frame = tk.Frame(self, highlightthickness=0, **args)
        title_frame.pack()

        title = tk.Label(title_frame, width=800, height=2, text='Select Player', bg='#000000', fg='#FFFFFF',
                         font=settings.fonts['screen_title'])
        title.pack()

    def _init_player_list(self):
        args = {
            'width': 800,
            'height': 280,
            'bg': '#000000'
        }
        canvas_frame = tk.Frame(self, highlightthickness=0, **args)
        canvas_frame.pack()
        self._canvas = tk.Canvas(canvas_frame, highlightthickness=0, **args)
        self._canvas.pack()

        self._show_page()

    def _init_exit(self):
        args = {
            'width': 800,
            'height': 100,
            'bg': '#000000'
        }
        canvas_frame = tk.Frame(self, highlightthickness=0, **args)
        canvas_frame.pack()

        canvas = tk.Canvas(canvas_frame, highlightthickness=0, **args)
        canvas.pack()

        CanvasButton(canvas, 'EXIT', (700, 30), onpress=lambda _: self._onexit())

    def _show_page(self):
        x, y = 170, 40

        for player in self._paginator.players():
            self._canvas.create_text(x, y, text=player.name, font=settings.fonts['player_name'],
                                     fill='#ffff00')
            latest_board = player.boards.order_by(Board.id)[-1]
            self._canvas.create_text(x + 220, y, text=' Level {}, Puzzle {}'
                                     .format(latest_board.puzzle.level.number, latest_board.puzzle.number),
                                     font=settings.fonts['puzzles_completed'], fill='#666666')
            if settings.admin_mode:
                CanvasButton(self._canvas, ' X ', (570, y), onpress=self._create_ondelete_player(player))

            next_puzzle = player.boards[-1].puzzle.next_puzzle()
            button_text = 'SELECT' if next_puzzle is not None else 'COMPLETE'
            CanvasButton(self._canvas, button_text, (640, y), onpress=self._create_onselect_player(player),
                         disabled=next_puzzle is None)
            y += 60

        CanvasButton(self._canvas, '<< PREV', (345, 250), onpress=self._onprev,
                     disabled=not self._paginator.has_prev_page())
        CanvasButton(self._canvas, 'NEXT >>', (445, 250), onpress=self._onnext,
                     disabled=not self._paginator.has_next_page())

    def _onnext(self, _):
        self._canvas.delete(*self._canvas.find_all())
        self._paginator.next_page()
        self._show_page()

    def _onprev(self, _):
        self._canvas.delete(*self._canvas.find_all())
        self._paginator.prev_page()
        self._show_page()

    def _create_onselect_player(self, player):
        def onselect(_):
            board = Game.resume(player)
            return self._onselect(board)
        return onselect

    def _create_ondelete_player(self, player):
        def ondelete(_):
            def delete():
                player.soft_delete()
                self._paginator.remove(player)
                self._canvas.delete(*self._canvas.find_all())
                self._show_page()
            Dialog(self, message="Are you sure you want to delete {}?".format(player.name),
                   onsubmit=delete, show_cancel=True)

        return ondelete
