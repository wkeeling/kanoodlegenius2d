import tkinter as tk

from kanoodlegenius2d.domain.models import (DuplicatePlayerNameException,
                                            Game)
from kanoodlegenius2d.ui.components import CanvasButton, Dialog
from kanoodlegenius2d.ui.settings import fonts


# The maximum length of a name a player can type in.
MAX_NAME_LENGTH = 10


class NewPlayerScreen(tk.Frame):
    """The screen where a new player can be entered."""

    def __init__(self, oncreate, onexit, master=None, **kwargs):
        """Initialise a NewPlayerScreen frame.

        Args:
            oncreate: Callback that will be called when a new player is created. This
                will be passed a single argument - the board instance for the player.
            onexit: No-args callback that will be called when the exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        super().__init__(master, highlightthickness=2, **kwargs)

        self._oncreate = oncreate
        self._onexit = onexit

        self._canvas = tk.Canvas(self, width=800, height=480, bg='#000000', highlightthickness=0)
        self._canvas.pack()

        self._canvas.create_text(400, 60, text='Enter Player Name', font=fonts['screen_title'],
                                 justify='center', fill='#FFFFFF')

        self._player_name = self._canvas.create_text(400, 120, text='', font=fonts['player_name'],
                                                     justify='center', fill='#666666')

        self._buttons = self._init_keyboard()

    def _init_keyboard(self):
        rows = (
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
            ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),
            ('k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'),
            ('u', 'v', 'w', 'x', 'y', 'z')
        )

        button_args = {
            'font': fonts['button_keyboard'],
            'width': 50,
            'height': 50
        }

        buttons = []
        y, offset = 200, 55
        for row in rows:
            x = 150
            for char in row:
                buttons.append(CanvasButton(self._canvas, str(char), (x, y), onpress=self._onkeypress, **button_args))
                x += offset
            y += offset

        button_args['font'] = fonts['button_standard']
        CanvasButton(self._canvas, 'DEL', (x, y - offset), onpress=self._ondelete, **button_args)
        x += offset
        CanvasButton(self._canvas, 'SHF', (x, y - offset), onpress=self._onshift, lockable=True, **button_args)
        x += offset
        CanvasButton(self._canvas, 'EXIT', (x, y - offset), onpress=lambda _: self._onexit(), **button_args)
        x += offset
        CanvasButton(self._canvas, ' OK ', (x, y - offset), onpress=self._onsubmit, **button_args)

        return buttons

    def _onkeypress(self, key):
        current_name = self._canvas.itemcget(self._player_name, 'text')
        if len(current_name) < MAX_NAME_LENGTH:
            self._canvas.itemconfigure(self._player_name, text=current_name + str(key))

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

    def _onsubmit(self, _):
        name = self._canvas.itemcget(self._player_name, 'text').strip()
        if not name:
            Dialog(self, message='Please enter a name')
        else:
            try:
                board = Game.start(name)
            except DuplicatePlayerNameException:
                Dialog(self, message='That name is already taken')
            else:
                self._oncreate(board)
