from collections import deque
import tkinter as tk

from kanoodlegenius2d.models import (initialise,
                                     Game,
                                     Noodle)
from kanoodlegenius2d import orientation


class PuzzleScreen(tk.Frame):
    """Represents the main screen of the game where a player interacts with
    a puzzle board and selects noodles to place.
    """
    def __init__(self, board, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        board_and_noodle = tk.Frame(self, bg='black')
        board_and_noodle.pack(side='top', fill='x')
        noodle_selection_frame = NoodleSelectionFrame(
            board, master=board_and_noodle, width=360, height=420, bg='black'
        )
        board_frame = BoardFrame(
            board, noodle_selection_frame, master=board_and_noodle, width=440, height=420, bg='black'
        )
        board_frame.pack(side='left')
        noodle_selection_frame.pack()
        status_frame = StatusFrame(self, width=800, height=60, bg='black')
        status_frame.pack()


class BoardFrame(tk.Frame):
    """The frame of the PuzzleScreen that contains the board."""
    def __init__(self, board, noodle_frame, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        self._board = board
        self._noodle_frame = noodle_frame
        self._canvas = tk.Canvas(self, width=440, height=420, bg='black', highlightbackground='white')
        self._canvas.pack()
        holes = self._draw_board()

        for i, hole in enumerate(holes):
            self._canvas.tag_bind(hole, '<ButtonPress-1>', self._create_on_hole_press(i, hole))

        self._hole_pressed = False

    def _draw_board(self):
        x, y = 110, 38
        x_incr, y_incr = 29, 49
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


class NoodleSelectionFrame(tk.Frame):
    """The frame of the PuzzleScreen that allows a noodle to be selected."""

    orientation_offsets = {
        orientation.E: (55, 0),
        orientation.SE: (28, 47),
        orientation.SW: (-27, 50),
        orientation.W: (-56, 0),
        orientation.NW: (-28, -48),
        orientation.NE: (27, -48)
    }

    def __init__(self, board, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        self._board = board
        self._selectable_noodles = deque(set(Noodle.select()) - set([noodle.noodle for noodle in self._board.noodles]))

        noodle_frame = tk.Frame(self)
        noodle_frame.pack(side='top')
        self._canvas = tk.Canvas(noodle_frame, width=360, height=300, bg='black', highlightbackground='white')
        self._canvas.pack()
        self._draw_noodle()

        control_frame = tk.Frame(self)
        control_frame.pack(side='top')

        prev = tk.Button(control_frame, text='Prev', highlightbackground='black',
                         command=self._prev_noodle)
        prev.pack(side='left')
        nxt = tk.Button(control_frame, text='Next', highlightbackground='black',
                        command=self._next_noodle)
        nxt.pack(side='right')

    def _draw_noodle(self):
        noodle_parts = []
        noodle = self._selectable_noodles[0]

        noodle_parts.append(self._canvas.create_oval(0, 0, 55, 55, fill='red'))
        orientations = noodle.part1, noodle.part2, noodle.part3, noodle.part4

        for o in orientations:
            offsets = self.orientation_offsets[o]
            coords = self._canvas.coords(noodle_parts[-1])
            noodle_parts.append(self._canvas.create_oval(coords[0] + offsets[0],
                                                         coords[1] + offsets[1],
                                                         coords[0] + offsets[0] + 55,
                                                         coords[1] + offsets[1] + 55,
                                                         fill='red'))
            # Now that a new part has been drawn, re-centre the noodle as it currently stands
            self._recentre(noodle_parts)

    def _next_noodle(self):
        self._canvas.delete('all')
        self._selectable_noodles.rotate()
        self._draw_noodle()

    def _prev_noodle(self):
        self._canvas.delete('all')
        self._selectable_noodles.rotate(-1)
        self._draw_noodle()

    def _recentre(self, noodle_parts):
        canvas_width = int(self._canvas.config()['width'][4])
        canvas_height = int(self._canvas.config()['height'][4])
        bbox = self._canvas.bbox(*noodle_parts)
        x_offset = ((canvas_width - (bbox[2] - bbox[0])) // 2) - bbox[0]
        y_offset = ((canvas_height - (bbox[3] - bbox[1])) // 2) - bbox[1]
        for part in noodle_parts:
            self._canvas.move(part, x_offset, y_offset)


class StatusFrame(tk.Frame):
    """The bar at the bottom that holds information about the player, current level etc."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480')  # Will eventually be set by the main kanoodlegenius2d root screen

    # initialise()
    # b = Game.start('Will')
    b = Game.resume('Will')  # The board instance will be passed by our parent eventually
    puzzle_screen = PuzzleScreen(b, root)
    puzzle_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
