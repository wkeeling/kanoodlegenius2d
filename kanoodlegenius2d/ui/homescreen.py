from collections import OrderedDict
import tkinter as tk

from kanoodlegenius2d.domain.models import Noodle
from kanoodlegenius2d.ui.components import CanvasButton


class HomeScreen(tk.Frame):
    """Represents the starting screen."""

    def __init__(self, onnewplayer, onexistingplayer, master=None, **kwargs):
        """Initialise a HomeScreen frame.

        Args:
            onnewplayer: No-args callback called when the new player button is pressed.
            onexistingplayer: No-args callback called when the existing player button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        args = {
            'width': 800,
            'height': 480,
            'bg': '#000000'
        }
        kwargs.update(args)

        super().__init__(master, highlightthickness=2, **kwargs)

        canvas = tk.Canvas(self, highlightthickness=0, **args)
        canvas.pack()

        canvas.create_text(400, 100, text='Kanoodle', font=('wood stamp', 80),
                           justify='center', fill='#FFFFFF')

        colour_map = OrderedDict()
        colour_map['G'] = Noodle.get(Noodle.designation == 'A').colour
        colour_map['E'] = Noodle.get(Noodle.designation == 'E').colour
        colour_map['N'] = Noodle.get(Noodle.designation == 'C').colour
        colour_map['I'] = Noodle.get(Noodle.designation == 'B').colour
        colour_map['U'] = Noodle.get(Noodle.designation == 'D').colour
        colour_map['S'] = Noodle.get(Noodle.designation == 'F').colour

        x, x_offset = 250, 60
        for char in colour_map:
            canvas.create_text(x, 180, text=char, font=('KG Counting Stars', 60),
                               justify='center', fill=colour_map[char])
            x += x_offset

        canvas.create_text(615, 140, text='2D', font=('cube vol.2', 36),
                           justify='center', fill='#FFFFFF')

        args = {
            'width': 150,
            'height': 50,
            'font': 'helvetica'
        }

        CanvasButton(canvas, 'NEW PLAYER', (310, 280), onclick=lambda _: onnewplayer(), **args)
        CanvasButton(canvas, 'EXISTING PLAYER', (490, 280), onclick=lambda _: onexistingplayer(), **args)
