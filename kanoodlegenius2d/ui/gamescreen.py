import os
import tkinter as tk
from collections import deque

from kanoodlegenius2d.domain import (holes,
                                     orientation)
from kanoodlegenius2d.domain.models import (Noodle,
                                            PositionUnavailableException)
from kanoodlegenius2d.ui.components import (CanvasButton,
                                            Dialog,
                                            Fade)
from kanoodlegenius2d.ui import settings

HIGHLIGHT_COLOUR = '#ffffff'
REJECT_COLOUR = '#ff0000'
# Hold these globally to prevent images disappearing
# from a canvas due to garbage collection.
NOODLE_IMAGES = {}


class GameScreen(tk.Frame):
    """The main screen of the game where a player interacts with a puzzle board and selects noodles to place."""

    def __init__(self, board, oncomplete, oncancel, master=None, **kwargs):
        """Initialise a new GameScreen frame.

        Args:
            board: The Board instance.
            oncomplete: Callback called when the board has been completed. The callback should accept a single
                argument - the Board instance that has been completed.
            oncancel: Callback called when the Exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        super().__init__(master, width=800, height=480, bg='#000000', highlightthickness=1, **kwargs)

        board_and_noodle = tk.Frame(master=self, width=800, height=420, bg='#000000', highlightthickness=1)
        board_and_noodle.pack(side='top', fill='x')
        noodle_selection_frame = NoodleSelectionFrame(board, master=board_and_noodle)
        board_frame = BoardFrame(board, oncomplete, noodle_selection_frame, master=board_and_noodle)
        board_frame.pack(side='left')
        noodle_selection_frame.pack()
        status_frame = InfoFrame(board, oncancel, master=self)
        status_frame.pack()

        # Initialise the cache of noodle images.
        if not NOODLE_IMAGES:
            for noodle in Noodle.select():
                NOODLE_IMAGES[noodle.designation] = tk.PhotoImage(
                    file=os.path.join(os.path.dirname(__file__), 'images', 'red_sphere.gif'))


class BoardFrame(tk.Frame):
    """The frame of the GameScreen that contains the board."""

    def __init__(self, board, oncomplete, noodle_frame, master=None, **kwargs):
        """Initialise a new BoardFrame frame.

        Args:
            board: The Board instance.
            oncomplete: Callback called when the board has been completed. The callback should accept a single
                argument - the Board instance that has been completed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        args = {
            'width': 440,
            'height': 420,
            'bg': '#000000'
        }
        kwargs.update(args)
        super().__init__(master, **kwargs)

        self._board = board
        self._oncomplete = oncomplete
        self._noodle_frame = noodle_frame
        self._canvas = tk.Canvas(self, highlightthickness=0, **args)
        self._canvas.pack()
        self._fade = Fade(self._canvas)
        self._hole_pressed = False
        self._holes = []

        self._undo = CanvasButton(self._canvas, 'UNDO', (400, 380), onclick=self._undo_place_noodle, height=40,
                                  disabled=True)
        self._solve = CanvasButton(
            self._canvas, 'SOLVE', (50, 380),
            onclick=lambda _: Dialog(message='If you auto-solve the puzzle, it will not '
                                             'count towards your completed puzzle total.',
                                     master=self.master,
                                     title='Are you sure?',
                                     onsubmit=self._solve_puzzle,
                                     show_cancel=True),
            height=40, disabled=True)

        level_text = self._canvas.create_text(220, 130, text='Level {}'.format(board.puzzle.level.number),
                                              font=settings.fonts['gamescreen_intro'], fill='#FFFFFF')
        puzzle_text = self._canvas.create_text(220, 200, text='Puzzle {}'.format(board.puzzle.number),
                                               font=settings.fonts['gamescreen_intro'], fill='#FFFFFF')

        def draw():
            self._canvas.delete(puzzle_text, level_text)
            self._holes = self._draw_board()
            self._draw_noodles_on_board(fade_duration=100)

        self.after(2000, draw)

    def _draw_board(self):
        x, y = 115, 38
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
            if settings.show_board_numbers:
                x1, y1, x2, y2 = self._canvas.bbox(hole_id)
                centre = x1 + ((x2 - x1) // 2), y1 + ((y2 - y1) // 2)
                self._canvas.create_text(centre, text=str(index), fill='#ffffff')
            self._canvas.tag_bind(hole_id, '<ButtonPress-1>', self._create_on_hole_press(index, hole_id))

        return hole_ids

    def _draw_row(self, tl_x, tl_y, num):
        holes_ = []
        for i in range(num):
            hole_id = self._canvas.create_oval(tl_x, tl_y, tl_x + 55, tl_y + 55,
                                               outline='#000000', fill='#000000', width=2)
            self._fade.fadein(hole_id, '#4d4d4d', elements=['outline'], duration=1000)
            holes_.append(hole_id)
            tl_x += 56
        return holes_

    def _draw_noodles_on_board(self, fade_duration=0, oncomplete=None):
        for hole_id in self._holes:
            self._canvas.itemconfig(hole_id, fill='#000000')

        for i, board_noodle in enumerate(self._board.noodles, start=3):

            def draw(i, n):
                if fade_duration == 0:
                    i = 0

                self.after(i*600, lambda: self._draw_noodle(n, n.position, fade_duration))

                if i == len(self._board.noodles) + 2:

                    def draw_complete():
                        self._noodle_frame.board_initialised()
                        if oncomplete:
                            oncomplete()

                    self.after(i * 700, draw_complete)

            draw(i, board_noodle)

    def _draw_noodle(self, noodle, position, fade_duration=0):
        last_position = position
        try:
            colour = noodle.colour
        except AttributeError:
            colour = noodle.noodle.colour
        try:
            image = NOODLE_IMAGES[noodle.designation]
        except AttributeError:
            image = NOODLE_IMAGES[noodle.noodle.designation]

        def show_image(item):
            x1, y1, x2, y2 = self._canvas.bbox(item)
            return lambda: self._canvas.create_image(x1 + ((x2 - x1) // 2), y1 + ((y2 - y1) // 2), image=image)

        self._fade.fadein(self._holes[last_position], colour, duration=fade_duration,
                          onfaded=show_image(self._holes[last_position]))
        self._canvas.itemconfig(self._holes[last_position], outline='#4d4d4d', width=2)

        for part in noodle.parts:
            last_position = holes.find_position(last_position, part)
            self._fade.fadein(self._holes[last_position], colour, duration=fade_duration,
                              onfaded=show_image(self._holes[last_position]))
            self._canvas.itemconfig(self._holes[last_position], outline='#4d4d4d', width=2)

        self._undo.disable(len(self._board.noodles) <= len(self._board.puzzle.noodles) or self._board.auto_completed)

    def _create_on_hole_press(self, hole_index, hole_id):
        def _on_hole_press(_):
            if not self._hole_pressed and self._canvas.itemcget(hole_id, 'fill') == '#000000':
                noodle, selected_part = self._noodle_frame.accept()
                if selected_part is None:
                    # No noodle selected in NoodleSelectionFrame
                    self._noodle_frame.reject(noodle)
                    return
                self._hole_pressed = True
                try:
                    root_index = self._board.place(noodle, position=hole_index, part_pos=selected_part)
                except PositionUnavailableException:
                    self._reject_place_noodle(noodle, hole_id)
                else:
                    self._commit_place_noodle(noodle, hole_id, root_index)
                    if self._board.completed:
                        self._oncomplete(self._board)

        return _on_hole_press

    def _reject_place_noodle(self, noodle, hole_id):
        self._noodle_frame.reject(noodle)
        self._canvas.itemconfig(hole_id, outline=REJECT_COLOUR, width=4)
        self._canvas.tag_raise(hole_id)

        def revert():
            self._canvas.itemconfig(hole_id, outline='#4d4d4d', width=2)
            self._hole_pressed = False

        self.after(500, revert)

    def _commit_place_noodle(self, noodle, hole_id, root_index):
        self._canvas.itemconfig(hole_id, outline=HIGHLIGHT_COLOUR, width=4)
        self._canvas.tag_raise(hole_id)

        def commit():
            self._draw_noodle(noodle, root_index, fade_duration=40)
            self._hole_pressed = False

        self.after(500, commit)

    def _undo_place_noodle(self, _):
        num_board_noodles = len(self._board.noodles)
        num_puzzle_noodles = len(self._board.puzzle.noodles)
        if num_puzzle_noodles < num_board_noodles < 7:
            noodle = self._board.undo()
            self._undo.disable(len(self._board.noodles) <= len(self._board.puzzle.noodles))
            self._solve.disable(False)
            if noodle:
                self._noodle_frame.reject(noodle)
                self._draw_noodles_on_board()

    def _solve_puzzle(self):
        self._board.solve()
        self._solve.disable(True)

        for hole_id in self._holes:
            self._canvas.itemconfig(hole_id, fill='#000000')

        puzzle_noodles = [noodle.noodle for noodle in self._board.puzzle.noodles]

        for noodle in self._board.noodles:
            if noodle.noodle in puzzle_noodles:
                self._draw_noodle(noodle, noodle.position)

        def draw_remaining():
            for noodle in self._board.noodles:
                if noodle.noodle not in puzzle_noodles:
                    self._draw_noodle(noodle, noodle.position, fade_duration=1500)
            self.after(4000, lambda: self._oncomplete(self._board))

        self.after(2000, draw_remaining)

        for _ in range(7 - len(self._board.puzzle.noodles)):
            self._noodle_frame.accept()


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

    def __init__(self, board, master=None, **kwargs):
        super().__init__(master, width=360, height=420, bg='#000000', **kwargs)

        self._board = board
        self._selectable_noodles = deque(set(Noodle.select()) - set([noodle.noodle for noodle in self._board.noodles]))

        noodle_frame = tk.Frame(self, width=360, height=300, bg='#000000')
        noodle_frame.pack(side='top')
        self._noodle_canvas = tk.Canvas(noodle_frame, width=360, height=300, bg='#000000', highlightthickness=0)
        self._noodle_canvas.pack()
        self._fade = Fade(self._noodle_canvas)

        control_frame = tk.Frame(self, width=360, height=120, bg='#000000')
        control_frame.pack(side='top')
        self._prev, self._next, self._rotate, self._flip = self._init_buttons(control_frame)

        # The part of the noodle that a user has pressed (0 - 4)
        self._selected_part = None
        self._images = []

    def board_initialised(self):
        """Called by the BoardFrame to indicate that it has finished initialising."""
        self._draw_noodle(fade_duration=300)
        self._toggle_disable_buttons()

        if not self._board.player.seen_instructions:
            def close():
                self._board.player.seen_instructions = True
                self._board.player.save()

            self.after(1000, lambda: Dialog(
                message='\n\n\nArrange the remaining noodles to fill in every remaining space on the board.\n\n'
                        'i. Manipulate the noodle using the control buttons.\n'
                        'ii. Touch the part of the noodle you want to place.\n'
                        'iii. Touch the hole on the board where you want to place it.',
                title='Instructions',
                justify='left',
                master=self.master,
                width=600,
                height=300,
                onsubmit=close))

    def _draw_noodle(self, fade_duration=0):
        noodle_parts, image_parts = [], []

        if self._selectable_noodles:
            noodle = self._selectable_noodles[0]
            noodle_parts.append(self._noodle_canvas.create_oval(0, 0, 55, 55, fill='#ffffff', outline='#4d4d4d',
                                                                width=2))

            for p in noodle.parts:
                offsets = self.orientation_offsets[p]
                coords = self._noodle_canvas.coords(noodle_parts[-1])
                noodle_parts.append(self._noodle_canvas.create_oval(coords[0] + offsets[0],
                                                                    coords[1] + offsets[1],
                                                                    coords[0] + offsets[0] + 55,
                                                                    coords[1] + offsets[1] + 55,
                                                                    fill='#ffffff', outline='#4d4d4d', width=2))

                # Now that a new part has been drawn, re-centre the noodle as it currently stands
                self._recentre(noodle_parts)

            for noodle_part in noodle_parts:
                x1, y1, x2, y2 = self._noodle_canvas.bbox(noodle_part)
                image_parts.append(self._noodle_canvas.create_image(x1 + ((x2 - x1) // 2), y1 + ((y2 - y1) // 2),
                                                                    image=NOODLE_IMAGES[noodle.designation],
                                                                    state='hidden'))

            def show_image(index):
                return lambda: self._noodle_canvas.itemconfig(image_parts[index], state='normal')

            for i, part in enumerate(noodle_parts):
                self._fade.fadein(part, noodle.colour, duration=fade_duration, onfaded=show_image(i))
                self._noodle_canvas.tag_bind(image_parts[i], '<ButtonPress-1>',
                                             self._create_on_part_press(i, noodle_parts, image_parts))

    def _recentre(self, noodle_parts):
        canvas_width = int(self._noodle_canvas.config()['width'][4])
        canvas_height = int(self._noodle_canvas.config()['height'][4])
        bbox = self._noodle_canvas.bbox(*noodle_parts)
        x_offset = ((canvas_width - (bbox[2] - bbox[0])) // 2) - bbox[0]
        y_offset = ((canvas_height - (bbox[3] - bbox[1])) // 2) - bbox[1]
        for part in noodle_parts:
            self._noodle_canvas.move(part, x_offset, y_offset)

    def _create_on_part_press(self, index, part_ids, image_ids):
        def _on_part_press(_):
            for part_id in part_ids:
                self._noodle_canvas.itemconfig(part_id, outline='#4d4d4d', width=2)

            if self._selected_part == index:
                self._noodle_canvas.itemconfig(part_ids[index], outline='#4d4d4d', width=2)
                self._selected_part = None
            else:
                self._noodle_canvas.itemconfig(part_ids[index], outline=HIGHLIGHT_COLOUR, width=4)
                self._noodle_canvas.tag_raise(part_ids[index])
                self._noodle_canvas.tag_raise(image_ids[index])
                self._selected_part = index

        return _on_part_press

    def _init_buttons(self, control_frame):
        canvas = tk.Canvas(control_frame, width=300, height=100, bg='#000000', highlightthickness=0)
        canvas.pack()

        args = {
            'width': 100,
            'height': 40,
            'disabled': True
        }

        prev = CanvasButton(canvas, text='<< PREV', pos=(90, 20), onclick=self._prev_noodle, **args)
        nxt = CanvasButton(canvas, text='NEXT >>', pos=(200, 20), onclick=self._next_noodle, **args)
        rotate = CanvasButton(canvas, text='ROTATE', pos=(90, 70), onclick=self._rotate_noodle, **args)
        flip = CanvasButton(canvas, text='FLIP', pos=(200, 70), onclick=self._flip_noodle, **args)

        return prev, nxt, rotate, flip

    def _next_noodle(self, _):
        items = self._noodle_canvas.find_all()
        self._selectable_noodles.rotate()
        self._draw_noodle(fade_duration=60)
        self._clear_items(items)

    def _prev_noodle(self, _):
        items = self._noodle_canvas.find_all()
        self._selectable_noodles.rotate(-1)
        self._draw_noodle(fade_duration=60)
        self._clear_items(items)

    def _rotate_noodle(self, _):
        if self._selectable_noodles:
            items = self._noodle_canvas.find_all()
            self._selectable_noodles[0].rotate()
            self._draw_noodle(fade_duration=60)
            self._clear_items(items)

    def _flip_noodle(self, _):
        if self._selectable_noodles:
            items = self._noodle_canvas.find_all()
            self._selectable_noodles[0].flip()
            self._draw_noodle(fade_duration=60)
            self._clear_items(items)

    def _clear_items(self, items):
        def clear():
            for i in items:
                self._noodle_canvas.delete(i)

        for item in items:
            self._fade.fadeout(item, duration=60, elements=['fill', 'outline'], onfaded=clear)

    def _toggle_disable_buttons(self):
        self._next.disable(len(self._selectable_noodles) <= 1)
        self._prev.disable(len(self._selectable_noodles) <= 1)
        self._flip.disable(len(self._selectable_noodles) == 0)
        self._rotate.disable(len(self._selectable_noodles) == 0)

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

        def redraw():
            self._noodle_canvas.delete('all')
            if self._selectable_noodles:
                self._draw_noodle(fade_duration=40)
            self._toggle_disable_buttons()

        self.after(500, redraw)

        return noodle, part

    def reject(self, noodle):
        """Reject accepting a noodle and place it back into the list of
        selectable noodles.

        Args:
            noodle: The noodle being rejected.
        """
        self._selectable_noodles.insert(0, noodle)
        self._noodle_canvas.delete('all')
        self._draw_noodle()
        self._toggle_disable_buttons()


class InfoFrame(tk.Frame):
    """The bar at the bottom that holds information about the player, current level etc."""

    def __init__(self, board, oncancel, master=None, **kwargs):
        """Initialise a new InfoFrame frame.

        Args:
            board: The Board instance.
            oncancel: Callback called when the Exit button is pressed.
            master: The parent widget.
            **kwargs: Optional keyword arguments to configure this screen.
        """
        frame_args = {
            'width': 800,
            'height': 60,
            'bg': '#000000',
        }
        kwargs.update(frame_args)
        super().__init__(master, highlightthickness=1, **kwargs)

        canvas = tk.Canvas(self, highlightthickness=0, **kwargs)
        canvas.pack()

        canvas.create_text(120, 26, text='PLAYER: {}'.format(board.player.name),
                           font=settings.fonts['gamescreen_player'], fill=Noodle.get(Noodle.designation == 'B').colour)
        canvas.create_text(300, 26, text='LEVEL: {}'.format(board.puzzle.level.number),
                           font=settings.fonts['gamescreen_status'], fill=Noodle.get(Noodle.designation == 'F').colour)
        canvas.create_text(380, 26, text='PUZZLE: {}'.format(board.puzzle.number),
                           font=settings.fonts['gamescreen_status'], fill=Noodle.get(Noodle.designation == 'F').colour)
        CanvasButton(canvas, 'EXIT', pos=(715, 26), width=140, height=40, onclick=lambda _: oncancel())
