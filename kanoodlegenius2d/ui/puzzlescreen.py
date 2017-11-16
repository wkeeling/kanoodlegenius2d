import tkinter as tk


class PuzzleScreen(tk.Frame):
    """Represents the main screen of the game where a player interacts with
    a puzzle board and selects noodles to place.
    """
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)


class BoardFrame(tk.Frame):
    """The frame of the PuzzleScreen that contains the board."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, width=480, height=480, bg='black', **kw)

        # self._board = tk.Canvas


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480')  # Will eventually be set by the main kanoodlegenius2d root screen
    puzzle_screen = PuzzleScreen(root)
    puzzle_screen.pack(fill='x')
    board = BoardFrame(puzzle_screen)
    board.pack(side='left')
    root.mainloop()
