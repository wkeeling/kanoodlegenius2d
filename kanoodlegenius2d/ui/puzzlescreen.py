import tkinter as tk


class PuzzleScreen(tk.Frame):
    """Represents the main screen of the game where a player interacts with
    a puzzle board and selects noodles to place.
    """
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        board_and_noodle = tk.Frame(self, bg='black')
        board_and_noodle.pack(side='top', fill='x')
        board_frame = BoardFrame(board_and_noodle, width=440, height=420, bg='black')
        noodle_frame = NoodleFrame(board_and_noodle, width=360, height=420, bg='black')
        board_frame.pack(side='left')
        noodle_frame.pack(side='left')
        status_frame = StatusFrame(self, width=800, height=60, bg='black')
        status_frame.pack()


class BoardFrame(tk.Frame):
    """The frame of the PuzzleScreen that contains the board."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        self._canvas = tk.Canvas(self, width=440, height=420, bg='black', highlightbackground='white')
        self._canvas.pack()
        holes = self._draw_board()

        for i, hole in enumerate(holes):
            self._canvas.tag_bind(hole, '<ButtonPress-1>', self._create_on_hole_press(i, hole))

        self._hole_pressed = False

    def _draw_board(self):
        x, y = 110, 38
        x_incr, y_incr = 28, 48
        holes = []
        holes.extend(self._draw_row(x, y, 4))
        x -= x_incr
        y += y_incr
        holes.extend(self._draw_row(x, y, 5))
        x -= x_incr
        y += y_incr
        holes.extend(self._draw_row(x, y, 6))
        x += x_incr
        y += y_incr
        holes.extend(self._draw_row(x, y, 5))
        x -= x_incr
        y += y_incr
        holes.extend(self._draw_row(x, y, 6))
        x += x_incr
        y += y_incr
        holes.extend(self._draw_row(x, y, 5))
        x += x_incr
        y += y_incr
        holes.extend(self._draw_row(x, y, 4))
        return holes

    def _draw_row(self, tl_x, tl_y, num):
        holes = []
        for i in range(num):
            hole_id = self._canvas.create_oval(tl_x, tl_y, tl_x + 55, tl_y + 55, outline='gray', fill='black', width=2)
            holes.append(hole_id)
            tl_x += 56
        return holes

    def _create_on_hole_press(self, index, hole):
        def _on_hole_press(event):
            if not self._hole_pressed:
                self._canvas.itemconfig(hole, outline='yellow')
                self._hole_pressed = True

                def revert():
                    self._canvas.itemconfig(hole, outline='gray')
                    self._hole_pressed = False
                self.after(500, revert)

        return _on_hole_press


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
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
