import tkinter as tk

from kanoodlegenius2d.ui.gamescreen import GameScreen
from kanoodlegenius2d.ui.homescreen import HomeScreen
from kanoodlegenius2d.ui.newplayerscreen import NewPlayerScreen
from kanoodlegenius2d.ui.selectplayerscreen import SelectPlayerScreen


class MasterScreen(tk.Tk):

    def __init__(self):
        """Initialise a Masterscreen frame.

        The MasterScreen is responsible for coordinating switching between other screens.
        """
        super().__init__()

        self.geometry('800x480+500+300')
        self.attributes('-topmost', True)
        self.update()
        self.attributes('-topmost', False)

        self._current_screen = self._create_homescreen()
        self.mainloop()

    def _create_homescreen(self):
        home_screen = HomeScreen(onnewplayer=self._onnewplayer, onexistingplayer=self._onexistingplayer,
                                 master=self)
        home_screen.pack()
        return home_screen

    def _onnewplayer(self):
        self._current_screen.destroy()
        self._current_screen = NewPlayerScreen(oncreate=self._oncreatenewplayer, oncancel=self._oncancel, master=self)
        self._current_screen.pack()

    def _onexistingplayer(self):
        self._current_screen.destroy()
        self._current_screen = SelectPlayerScreen(onselect=self._oncreatenewplayer, oncancel=self._oncancel,
                                                  master=self)
        self._current_screen.pack()

    def _oncreatenewplayer(self, player):
        pass

    def _onselectplayer(self, player):
        pass

    def _oncancel(self):
        current_screen = self._current_screen
        self._current_screen = self._create_homescreen()
        current_screen.destroy()

    def _switch_screen(self, new_screen):
        old_screen = self._current_screen
        self._current_screen = new_screen
        self._current_screen.tkraise()
        old_screen.destroy()

if __name__ == '__main__':
    MasterScreen()
