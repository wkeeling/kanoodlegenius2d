import os

import tkinter as tk

from kanoodlegenius2d.domain.models import initialise
from kanoodlegenius2d.ui.dialog import display_dialog
from kanoodlegenius2d.ui.components import CanvasButton


class NewPlayerScreen(tk.Frame):
    """Represents the screen where a new player can be entered."""

    def __init__(self, onsubmit, oncancel, master=None, **kw):
        super().__init__(master, **kw)

        self._onsubmit = onsubmit
        self._oncancel = oncancel

        self._canvas = tk.Canvas(self, width=800, height=480, bg='#000000', highlightthickness=1)
        self._canvas.pack()

        self._canvas.create_text(400, 60, text='Enter Player Name', font=('helvetica', 22),
                                 justify='center', fill='#FFFFFF')

        self._player_name = self._canvas.create_text(400, 120, text='', font=('helvetica', 18),
                                                     justify='center', fill='#FFFFFF')
        self._canvas.create_line(250, 135, 550, 135, fill='#666666', width=2.0)

        self._buttons = self._init_keyboard()

    def _init_keyboard(self):
        rows = (
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
            ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),
            ('k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'),
            ('u', 'v', 'w', 'x', 'y', 'z')
        )

        button_args = {
            'font': ('helvetica', 16),
            'width': 50,
            'height': 50
        }

        buttons = []
        y, offset = 220, 55
        for row in rows:
            x = 150
            for char in row:
                buttons.append(CanvasButton(self._canvas, str(char), (x, y), onclick=self._onkeypress, **button_args))
                x += offset
            y += offset

        button_args['font'] = ('helvetica', 14)
        CanvasButton(self._canvas, 'Del', (x, y - offset), onclick=self._ondelete, **button_args)
        x += offset
        CanvasButton(self._canvas, 'Shift', (x, y - offset), onclick=self._onshift, lockable=True, **button_args)
        x += offset
        CanvasButton(self._canvas, 'Exit', (x, y - offset), onclick=self._oncancel, **button_args)
        x += offset
        CanvasButton(self._canvas, 'Done', (x, y - offset), onclick=self._onsubmit, **button_args)

        return buttons

    def _onkeypress(self, key):
        self._canvas.itemconfigure(self._player_name,
                                   text=self._canvas.itemcget(self._player_name, 'text') + str(key))

    def _ondelete(self, _):
        self._canvas.itemconfigure(self._player_name,
                                   text=self._canvas.itemcget(self._player_name, 'text')[:-1])

    def _onshift(self, _):
        for key in self._buttons:
            if key.text.isalpha():
                if key.text.islower():
                    key.text = key.text.upper()
                else:
                    key.text = key.text.lower()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480+500+300')  # Will eventually be set by the main kanoodlegenius2d root screen
    try:
        import os

        os.remove(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))
    except OSError:
        pass
    initialise()

    game_screen = NewPlayerScreen(lambda _: None, lambda _: None, root, highlightthickness=1)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
