import math
import tkinter as tk

from kanoodlegenius2d.domain.models import (Game,
                                            Player,
                                            initialise)
from kanoodlegenius2d.ui.components import (CanvasButton,
                                            Dialog)


class SelectPlayerScreen(tk.Frame):
    """Represents the screen where an existing player can be selected."""

    def __init__(self, onselect, oncancel, master=None, **kwargs):
        """Initialise a new SelectPlayerScreen frame.

        Args:
            onselect: Callback that will be called when a new player is selected. This
                will be passed a single argument - the board instance for the player.
            oncancel: Callback that will be called when the exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        super().__init__(master, **kwargs)

        self._onselect = onselect
        self._oncancel = oncancel

        self._init_title()
        self._paginator = PlayerPaginator(Player.active_players())
        self._init_player_list()

    def _init_title(self):
        title_frame = tk.Frame(self, highlightthickness=0)
        title_frame.pack()

        title = tk.Label(title_frame, width=800, height=4, text='Select Player', bg='#000000', fg='#FFFFFF',
                         font=('helvetica', 22))
        title.pack()

    def _init_player_list(self):
        canvas_frame = tk.Frame(self, highlightthickness=0)
        canvas_frame.pack()
        self._canvas = tk.Canvas(canvas_frame, width=800, height=480, bg='#000000', highlightthickness=0)
        self._canvas.pack()

        self._show_page()

        CanvasButton(self._canvas, 'EXIT', (700, 300), font='helvetica', onclick=self._oncancel)

    def _show_page(self):
        x, y = 150, 50

        for player in self._paginator.players():
            self._canvas.create_text(x, y, text=player.name, font=('helvetica', 18), fill='#666666')
            CanvasButton(self._canvas, ' X ', (575, y), font='helvetica',
                         onclick=self._create_ondelete_player(player))
            CanvasButton(self._canvas, 'SELECT', (640, y), font='helvetica', onclick=lambda: None)
            y += 40

        CanvasButton(self._canvas, '<< PREV', (345, 250), font='helvetica', onclick=self._onprev)
        CanvasButton(self._canvas, 'NEXT >>', (445, 250), font='helvetica', onclick=self._onnext)

    def _onnext(self, _):
        self._canvas.delete(*self._canvas.find_all())
        self._paginator.next_page()
        self._show_page()

    def _onprev(self, _):
        self._canvas.delete(*self._canvas.find_all())
        self._paginator.prev_page()
        self._show_page()

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
        return self._current_page != self._total_pages

    def prev_page(self):
        self._current_page -= 1
        self._current_page = max(self._current_page, 1)

    def has_prev_page(self):
        return self._current_page != 1

    def remove(self, player):
        self._players.remove(player)
        if not self.players():
            self._total_pages = self._calc_total_pages()
            self.prev_page()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480+500+300')  # Will eventually be set by the main kanoodlegenius2d root screen
    try:
        import os

        os.remove(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))
    except OSError:
        pass
    initialise()

    Game.start('Will')
    Game.start('John')
    Game.start('Fred')
    Game.start('Jack')
    Game.start('Gary')
    Game.start('Lucy')
    Game.start('Emma')
    import sys
    game_screen = SelectPlayerScreen(lambda _: None, lambda _: sys.exit(), root, highlightthickness=2)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
