import tkinter as tk

from kanoodlegenius2d.domain.models import Player, Puzzle
from kanoodlegenius2d.ui import settings
from kanoodlegenius2d.ui.components import CanvasButton, PlayerPaginator


class HighScoreScreen(tk.Frame):
    """The starting screen."""

    def __init__(self, onexit, master=None, **kwargs):
        """Initialise a HighScoreScreen frame.

        Args:
            onexit: No-args callback that will be called when the exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        super().__init__(master, width=800, height=480, bg='#000000', highlightthickness=2, **kwargs)

        self._onexit = onexit

        self._init_title()
        players = sorted(Player.active_players(),
                         key=lambda p: (p.puzzles_completed.player_completed * -1, p.name))
        self._paginator = PlayerPaginator(players, page_size=4)
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

        title = tk.Label(title_frame, width=800, height=2, text='High Scores', bg='#000000', fg='#FFFFFF',
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
        x, y = 210, 20

        for player in self._paginator.players():
            self._canvas.create_text(x, y, text=player.name, font=settings.fonts['player_name'],
                                     fill='#ffffff')
            self._canvas.create_text(x + 220, y, text=' {} puzzles completed, {} auto-solved'
                                     .format(player.puzzles_completed.player_completed,
                                             player.puzzles_completed.auto_completed),
                                     font=settings.fonts['puzzles_completed'], fill='#666666')

            y += 50

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