import tkinter as tk

from kanoodlegenius2d.domain.models import (Game,
                                            Player,
                                            initialise)
from kanoodlegenius2d.ui.components import (CanvasButton,
                                            display_dialog)


class SelectPlayerScreen(tk.Frame):
    """Represents the screen where an existing player can be selected."""

    def __init__(self, onselect, oncancel, master=None, **kw):
        """Initialise a new SelectPlayerScreen frame.

        Args:
            onselect:
                Callback that will be called when a new player is selected. This
                will be passed a single argument - the board instance for the player.
            oncancel:
                Callback that will be called when the exit button is pressed.
            master:
                The parent widget.
            kw:
                Optional keyword arguments to configure this screen.
        """
        super().__init__(master, **kw)

        self._onselect = onselect
        self._oncancel = oncancel

        self._init_title()
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
        canvas = tk.Canvas(canvas_frame, width=800, height=480, bg='#000000', highlightthickness=0)
        canvas.pack()

        x, y = 150, 75

        for player in Player.select().where(Player.deleted == False):
            canvas.create_text(x, y, text=player.name, font=('helvetica', 18), fill='#666666')
            CanvasButton(canvas, 'DELETE', (570, y), font='helvetica', onclick=self._create_delete_player(player))
            CanvasButton(canvas, ' GO ', (637, y), font='helvetica', onclick=lambda: None)
            y += 40

    def _create_delete_player(self, player):
        def delete(_):
            display_dialog(message="Are you sure you want to delete {}?".format(player.name),
                           master=self, show_cancel=True)
            player.soft_delete()

        return delete


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
    game_screen = SelectPlayerScreen(lambda _: None, lambda _: None, root, highlightthickness=2)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
