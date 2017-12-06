import tkinter as tk

from kanoodlegenius2d.domain.models import (Game,
                                            initialise)


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

        title = tk.Label(title_frame, width=800, height=3, text='Select Player', bg='#000000', fg='#FFFFFF',
                         font=('helvetica', 22))
        title.pack()

    def _init_player_list(self):
        canvas_frame = tk.Frame(self, highlightthickness=0)
        canvas_frame.pack()
        self._canvas = tk.Canvas(canvas_frame, width=800, height=380, bg='#000000', highlightthickness=0)
        vbar = tk.Scrollbar(canvas_frame, width=32, bg='#000000', activebackground='#000000', orient='vertical')
        vbar.pack(side='right', fill='y')
        vbar.config(command=self._canvas.yview)
        self._canvas.config(yscrollcommand=vbar.set)
        self._canvas.pack(side='bottom')

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480+500+300')  # Will eventually be set by the main kanoodlegenius2d root screen
    try:
        import os

        os.remove(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))
    except OSError:
        pass
    initialise()

    game_screen = SelectPlayerScreen(lambda _: None, lambda _: None, root, highlightthickness=2)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
