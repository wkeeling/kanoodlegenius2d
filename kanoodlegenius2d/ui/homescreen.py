import tkinter as tk

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
        super().__init__(master, highlightthickness=2, **kwargs)

        canvas = tk.Canvas(self, width=800, height=480, bg='#000000', highlightthickness=0)
        canvas.pack()

        canvas.create_text(400, 100, text='Kanoodle Genius 2D', font=('helvetica', 32),
                           justify='center', fill='#FFFFFF')

        args = {
            'width': 150,
            'height': 50,
            'font': 'helvetica'
        }

        CanvasButton(canvas, 'NEW PLAYER', (305, 220), onclick=lambda _: onnewplayer(), **args)
        CanvasButton(canvas, 'EXISTING PLAYER', (485, 220), onclick=lambda _: onexistingplayer(), **args)
