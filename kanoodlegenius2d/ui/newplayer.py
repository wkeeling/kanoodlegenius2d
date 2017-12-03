import os

import tkinter as tk

from kanoodlegenius2d.domain.models import initialise
from kanoodlegenius2d.ui.dialog import display_dialog
from kanoodlegenius2d.ui.util import CanvasWidgetHelper


class NewPlayerScreen(tk.Frame):
    """Represents the screen where a new player can be entered."""

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self._canvas = tk.Canvas(self, width=800, height=480, bg='#000000', highlightthickness=1)
        self._canvas.pack()
        self._widget_helper = CanvasWidgetHelper(self._canvas)

        self._player_text = self._canvas.create_text(400, 120, text='WILL', font=('helvetica', 18),
                                                     justify='center', fill='#FFFFFF')
        self._canvas.create_line(250, 135, 550, 135, fill='#666666', width=2.0)

        self._init_keyboard()

    def _init_keyboard(self):
        keys = (
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
            ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),
            ('k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'),
            ('u', 'v', 'w', 'x', 'y', 'z')
        )

        args = {
            'font': ('helvetica', 16),
            'width': 50,
            'height': 50
        }

        y, offset = 220, 55
        for row in keys:
            x = 150
            for key in row:
                self._widget_helper.create_button(str(key), (x, y), onclick=self._onclick, **args)
                x += offset
            y += offset

        args['font'] = ('helvetica', 14)
        self._widget_helper.create_button('Del', (x, y - offset), onclick=self._onclick, **args)
        x += offset
        self._widget_helper.create_button('Shift', (x, y - offset), onclick=self._onclick, **args)
        x += offset
        self._widget_helper.create_button('Back', (x, y - offset), onclick=self._back, **args)
        x += offset
        self._widget_helper.create_button(' OK ', (x, y - offset), onclick=self._submit, **args)

    def _onclick(self, key):
        if key == 'Del':
            self._canvas.itemconfigure(self._player_text,
                                       text=self._canvas.itemcget(self._player_text, 'text')[:-1])
        else:
            self._canvas.itemconfigure(self._player_text,
                                       text=self._canvas.itemcget(self._player_text, 'text') + str(key))

    def _back(self, _):
        pass

    def _submit(self, _):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480+500+300')  # Will eventually be set by the main kanoodlegenius2d root screen
    try:
        import os

        os.remove(os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db'))
    except OSError:
        pass
    initialise()

    game_screen = NewPlayerScreen(root, highlightthickness=1)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
