from collections import deque
import tkinter as tk

from kanoodlegenius2d.models import (initialise,
                                     Game,
                                     Noodle,
                                     PositionUnavailableException)
from kanoodlegenius2d import (holes,
                              orientation)


HIGHLIGHT_COLOUR = 'white'


class GameScreen(tk.Frame):
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
    """The frame of the GameScreen that contains the board."""
    def __init__(self, board, noodle_frame, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        self._board = board
        self._noodle_frame = noodle_frame
        self._canvas = tk.Canvas(self, width=440, height=420, bg='black', highlightbackground='white')
        self._canvas.pack()
        self._holes = self._draw_board()
        self._draw_noodles_on_board()

        self._hole_pressed = False

    def _draw_board(self):
        x, y = 110, 38
        x_incr, y_incr = 29, 49
        hole_ids = []
        hole_ids.extend(self._draw_row(x, y, 4))
        x -= x_incr
        y += y_incr
        hole_ids.extend(self._draw_row(x, y, 5))
        x -= x_incr
        y += y_incr
        hole_ids.extend(self._draw_row(x, y, 6))
        x += x_incr
        y += y_incr
        hole_ids.extend(self._draw_row(x, y, 5))
        x -= x_incr
        y += y_incr
        hole_ids.extend(self._draw_row(x, y, 6))
        x += x_incr
        y += y_incr
        hole_ids.extend(self._draw_row(x, y, 5))
        x += x_incr
        y += y_incr
        hole_ids.extend(self._draw_row(x, y, 4))

        for index, hole_id in enumerate(hole_ids):
            self._canvas.tag_bind(hole_id, '<ButtonPress-1>', self._create_on_hole_press(index, hole_id))

        return hole_ids

    def _draw_row(self, tl_x, tl_y, num):
        holes_ = []
        for i in range(num):
            hole_id = self._canvas.create_oval(tl_x, tl_y, tl_x + 55, tl_y + 55,
                                               outline='#4d4d4d', fill='black', width=2)
            holes_.append(hole_id)
            tl_x += 56
        return holes_

    def _draw_noodles_on_board(self):
        for board_noodle in self._board.noodles:
            self._draw_noodle(board_noodle, board_noodle.position)

    def _draw_noodle(self, noodle, position):
        last_position = position
        try:
            colour = noodle.colour
        except AttributeError:
            colour = noodle.noodle.colour
        self._canvas.itemconfig(self._holes[last_position], outline='#4d4d4d', fill=colour, width=2)
        for part in noodle.parts:
            last_position = holes.find_position(last_position, part)
            self._canvas.itemconfig(self._holes[last_position], outline='#4d4d4d', fill=colour, width=2)

    def _create_on_hole_press(self, hole_index, hole_id):
        def _on_hole_press(_):
            if not self._hole_pressed and self._canvas.itemcget(hole_id, 'fill') == 'black':
                noodle, part_pos = self._noodle_frame.accept()
                if part_pos is None:
                    # No noodle selected in NoodleSelectionFrame
                    self._noodle_frame.reject(noodle)
                    return
                self._hole_pressed = True
                try:
                    index = hole_index
                    # Traverse backwards along the noodle to the root position
                    for pos in reversed(range(part_pos)):
                        if index is None:
                            raise PositionUnavailableException()
                        index = holes.find_position(index, orientation.opposite(noodle.parts[pos]))
                    self._board.place(noodle, position=index)
                except PositionUnavailableException:
                    self._noodle_frame.reject(noodle)
                    self._canvas.itemconfig(hole_id, outline='red', width=4)
                    self._canvas.tag_raise(hole_id)

                    def revert():
                        self._canvas.itemconfig(hole_id, outline='#4d4d4d', width=2)
                        self._hole_pressed = False

                    self.after(500, revert)
                else:
                    self._canvas.itemconfig(hole_id, outline=HIGHLIGHT_COLOUR, width=4)
                    self._canvas.tag_raise(hole_id)

                    def commit():
                        self._draw_noodle(noodle, index)
                        self._hole_pressed = False

                    self.after(500, commit)

        return _on_hole_press


class NoodleSelectionFrame(tk.Frame):
    """The frame of the GameScreen that allows a noodle to be selected."""

    orientation_offsets = {
        orientation.E: (57, 0),
        orientation.SE: (29, 49),
        orientation.SW: (-29, 49),
        orientation.W: (-57, 0),
        orientation.NW: (-29, -49),
        orientation.NE: (29, -49)
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

        control_frame = tk.Frame(self)
        control_frame.pack(side='top')
        self._init_buttons(control_frame)
        self._draw_noodle()

        # The part of the noodle that a user has pressed (0 - 4)
        self._selected_part = None

    def _draw_noodle(self):
        noodle_parts = []
        noodle = self._selectable_noodles[0]

        noodle_parts.append(self._canvas.create_oval(0, 0, 55, 55, fill=noodle.colour, outline='#4d4d4d', width=2))

        for p in noodle.parts:
            offsets = self.orientation_offsets[p]
            coords = self._canvas.coords(noodle_parts[-1])
            noodle_parts.append(self._canvas.create_oval(coords[0] + offsets[0],
                                                         coords[1] + offsets[1],
                                                         coords[0] + offsets[0] + 55,
                                                         coords[1] + offsets[1] + 55,
                                                         fill=noodle.colour, outline='#4d4d4d', width=2))
            # Now that a new part has been drawn, re-centre the noodle as it currently stands
            self._recentre(noodle_parts)

        for i, part in enumerate(noodle_parts):
            self._canvas.tag_bind(part, '<ButtonPress-1>', self._create_on_part_press(i, noodle_parts))

    def _recentre(self, noodle_parts):
        canvas_width = int(self._canvas.config()['width'][4])
        canvas_height = int(self._canvas.config()['height'][4])
        bbox = self._canvas.bbox(*noodle_parts)
        x_offset = ((canvas_width - (bbox[2] - bbox[0])) // 2) - bbox[0]
        y_offset = ((canvas_height - (bbox[3] - bbox[1])) // 2) - bbox[1]
        for part in noodle_parts:
            self._canvas.move(part, x_offset, y_offset)

    def _create_on_part_press(self, index, part_ids):
        def _on_part_press(_):
            for part_id in part_ids:
                self._canvas.itemconfig(part_id, outline='#4d4d4d', width=2)

            if self._selected_part == part_ids[index]:
                self._canvas.itemconfig(part_ids[index], outline='#4d4d4d', width=2)
                self._selected_part = None
            else:
                self._canvas.itemconfig(part_ids[index], outline=HIGHLIGHT_COLOUR, width=4)
                self._canvas.tag_raise(part_ids[index])
                self._selected_part = index

        return _on_part_press

    def _init_buttons(self, control_frame):
        nxt_button = tk.Button(control_frame, text='Next', highlightbackground='black',
                               command=self._next_noodle)
        nxt_button.pack(side='left')

        rotate_button = tk.Button(control_frame, text='Rotate', highlightbackground='black',
                                  command=self._rotate_noodle)
        rotate_button.pack(side='left')

        flip_button = tk.Button(control_frame, text='Flip', highlightbackground='black',
                                command=self._flip_noodle)
        flip_button.pack(side='left')

    def _next_noodle(self):
        self._canvas.delete('all')
        self._selectable_noodles.rotate()
        self._draw_noodle()

    def _rotate_noodle(self):
        self._canvas.delete('all')
        self._selectable_noodles[0].rotate()
        self._draw_noodle()

    def _flip_noodle(self):
        self._canvas.delete('all')
        self._selectable_noodles[0].flip()
        self._draw_noodle()

    def accept(self):
        """Accept the currently selected noodle and part and remove them
        from the current list of selectable noodles.

        Returns:
            A 2-tuple consisting of the currently selected noodle
            and the part that was pressed (an integer in the range
            0 - 4).
        """
        noodle, part = self._selectable_noodles.popleft(), self._selected_part
        self._selected_part = None
        self._canvas.delete('all')
        if self._selectable_noodles:
            self.after(500, self._draw_noodle)
        return noodle, part

    def reject(self, noodle):
        """Reject accepting a noodle and place it back into the list of
        selectable noodles.

        Args:
            noodle:
                The noodle being rejected.
        """
        self._selectable_noodles.insert(0, noodle)
        self._canvas.delete('all')
        self._draw_noodle()


class StatusFrame(tk.Frame):
    """The bar at the bottom that holds information about the player, current level etc."""
    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x480')  # Will eventually be set by the main kanoodlegenius2d root screen

    initialise()
    b = Game.start('Will')
    # b = Game.resume('Will')  # The board instance will be passed by our parent eventually
    game_screen = GameScreen(b, root)
    game_screen.pack(fill='x')
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.mainloop()
