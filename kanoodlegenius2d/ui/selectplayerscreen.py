import math
import tkinter as tk

from kanoodlegenius2d.domain.models import (Game,
                                            Puzzle)
from kanoodlegenius2d.ui.components import (CanvasButton,
                                            Dialog)
from kanoodlegenius2d.ui.settings import fonts


class SelectPlayerScreen(tk.Frame):
    """Represents the screen where an existing player can be selected."""

    def __init__(self, onselect, oncancel, master=None, **kwargs):
        """Initialise a new SelectPlayerScreen frame.

        Args:
            onselect: Callback that will be called when a new player is selected. This
                will be passed a single argument - the board instance for the player.
            oncancel: No-args callback that will be called when the exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        super().__init__(master, width=800, height=480, bg='#000000', highlightthickness=2, **kwargs)

        self._onselect = onselect
        self._oncancel = oncancel

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
                         font=fonts['screen_title'])
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

        CanvasButton(canvas, 'EXIT', (700, 25), onclick=lambda _: self._oncancel())

    def _show_page(self):
        x, y = 170, 40

        for player in self._paginator.players():
            self._canvas.create_text(x, y, text=player.name, font=fonts['player_name'],
                                     fill='#ffffff')
            self._canvas.create_text(x + 220, y, text=' {}/{} puzzles completed'
                                     .format(player.puzzles_completed.player_completed, Puzzle.select().count()),
                                     font=fonts['puzzles_completed'], fill='#666666')
            CanvasButton(self._canvas, ' X ', (570, y), onclick=self._create_ondelete_player(player))
            CanvasButton(self._canvas, 'SELECT', (640, y), onclick=self._create_onselect_player(player))
            y += 45

        CanvasButton(self._canvas, '<< PREV', (345, 240), onclick=self._onprev,
                     disabled=not self._paginator.has_prev_page())
        CanvasButton(self._canvas, 'NEXT >>', (445, 240), onclick=self._onnext,
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
            Dialog(message="Are you sure you want to delete {}?".format(player.name),
                           master=self, onsubmit=delete, show_cancel=True)

        return ondelete


class PlayerPaginator:
    """Helper class for paginating a list of players in memory."""

    def __init__(self, players, page_size=4):
        self._players = list(players)
        self._page_size = page_size
        self._current_page = 1
        self._total_pages = self._calc_total_pages()

    def _calc_total_pages(self):
        return math.ceil(len(self._players) / self._page_size)

    def players(self):
        start = (self._current_page - 1) * self._page_size
        end = self._current_page * self._page_size
        return self._players[start:end]

    def next_page(self):
        self._current_page += 1
        self._current_page = min(self._current_page, self._total_pages)

    def has_next_page(self):
        return self._total_pages and self._current_page != self._total_pages

    def prev_page(self):
        self._current_page -= 1
        self._current_page = max(self._current_page, 1)

    def has_prev_page(self):
        return self._current_page != 1

    def remove(self, player):
        self._players.remove(player)
        self._total_pages = self._calc_total_pages()
        if not self.players():
            self.prev_page()
