import tkinter as tk


class PuzzleScreen(tk.Frame):
    """Represents the main screen of the game where a player interacts with
    a puzzle board and selects noodles to place.
    """
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        board_and_noodle = tk.Frame(self)
        board_and_noodle.pack(side='top', fill='x')
        board_frame = BoardFrame(board_and_noodle, width=500, height=440, bg='black')
        noodle_frame = NoodleFrame(board_and_noodle, width=300, height=440, bg='gray')
        board_frame.pack(side='left')
        noodle_frame.pack(side='left')
        status_frame = StatusFrame(self, width=800, height=40, bg='black')
        status_frame.pack()


class BoardFrame(tk.Frame):
    """The frame of the PuzzleScreen that contains the board."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        # self._board = tk.Canvas


class NoodleFrame(tk.Frame):
    """The frame of the PuzzleScreen that contains the noodle."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)


class StatusFrame(tk.Frame):
    """The bar at the bottom that holds information about the player, current level etc."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480')  # Will eventually be set by the main kanoodlegenius2d root screen
    puzzle_screen = PuzzleScreen(root)
    puzzle_screen.pack(fill='x')
    root.mainloop()
