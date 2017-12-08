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
        super().__init__(master, **kwargs)

        canvas = tk.Canvas(self, width=800, height=480, bg='#000000', highlightthickness=0)
        canvas.pack()

        canvas.create_text(400, 60, text='Kanoodle Genius 2D', font=('helvetica', 22),
                           justify='center', fill='#FFFFFF')

        args = {
            'width': 150,
            'height': 50,
            'font': 'helvetica'
        }

        CanvasButton(canvas, 'NEW PLAYER', (305, 200), onclick=lambda _: onnewplayer, **args)
        CanvasButton(canvas, 'EXISTING PLAYER', (485, 200), onclick=lambda _: onexistingplayer, **args)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480+500+300')  # Will eventually be set by the main kanoodlegenius2d root screen
    game_screen = HomeScreen(lambda: None, lambda: None, master=root, highlightthickness=2)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
