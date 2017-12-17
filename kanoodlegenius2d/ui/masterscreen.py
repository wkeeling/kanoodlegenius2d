import tkinter as tk

from kanoodlegenius2d.ui.components import Dialog
from kanoodlegenius2d.ui.gamescreen import GameScreen
from kanoodlegenius2d.ui.homescreen import HomeScreen
from kanoodlegenius2d.ui.newplayerscreen import NewPlayerScreen
from kanoodlegenius2d.ui.selectplayerscreen import SelectPlayerScreen


class MasterScreen(tk.Tk):
    """The MasterScreen is responsible for coordinating switching between screens."""

    def __init__(self):
        """Initialise a Masterscreen frame."""
        super().__init__()

        self.geometry('800x480+500+300')
        self.attributes('-topmost', True)
        self.update()
        self.attributes('-topmost', False)
        self.configure(background='#000000')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self._current_screen = None
        self._switch_screen(HomeScreen(onnewplayer=self._onnewplayer, onexistingplayer=self._onexistingplayer,
                                       master=self))
        self.mainloop()

    def _onnewplayer(self):
        self._switch_screen(NewPlayerScreen(oncreate=self._oncreatenewplayer, oncancel=self._oncancel, master=self))

    def _onexistingplayer(self):
        self._switch_screen(SelectPlayerScreen(onselect=self._onselectplayer, oncancel=self._oncancel,
                                               master=self))

    def _oncreatenewplayer(self, board):
        self._switch_screen(GameScreen(board, self._oncomplete, self._oncancel, self))

    def _onselectplayer(self, board):
        self._switch_screen(GameScreen(board, self._oncomplete, self._oncancel, self))

    def _oncancel(self):
        self._switch_screen(HomeScreen(onnewplayer=self._onnewplayer, onexistingplayer=self._onexistingplayer,
                                       master=self))

    def _oncomplete(self, board):
        next_puzzle = board.puzzle.next_puzzle()
        if next_puzzle is None:
            title = 'Congratulations'
            message = 'You have completed the game!'
        else:
            title = 'Congratulations'
            message = 'You have completed puzzle {}!' \
                .format(board.puzzle.number, next_puzzle.number)

        self.after(1500, lambda: Dialog(message, title=title, master=self))

    def _switch_screen(self, new_screen):
        old_screen = self._current_screen
        self._current_screen = new_screen
        self._current_screen.grid(row=0, column=0, sticky='nsew')
        self._current_screen.tkraise()
        if old_screen:
            old_screen.destroy()

if __name__ == '__main__':
    MasterScreen()
