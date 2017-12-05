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
