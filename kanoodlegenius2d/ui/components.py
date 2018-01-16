import struct
import tkinter as tk

from kanoodlegenius2d.ui import settings


class Dialog(tk.Toplevel):
    """A popup panel which overlays the panel beneath it and can be closed by the user."""

    def __init__(self, master, message, **kwargs):
        """Initialise and display a new dialog popup.

        Args:
            master: The parent widget.
            message: The text to display on the dialog.
            **kwargs: Optional keyword arguments that can include:
                title: Title displayed above the message.
                width: The width of the dialog in pixels (default 50% of parent).
                height: The height of the dialog in pixels (default 50% of parent).
                justify: The justify setting for the message (default center).
                show_submit: Whether to show a submit button (default True).
                submit_text: The text of the submit button (default OK).
                onsubmit: Callable invoked when the submit button pressed (default None).
                show_cancel: Whether to show a cancel button (default False).
                cancel_text: The text of the cancel button when shown (default CANCEL).
                oncancel: Callable invoked when the cancel button pressed (default None).
                timeout: The number of seconds after which to automatically cancel the
                    dialog (default None - no auto-cancel).
        """
        super().__init__(master, bg='#000000', highlightthickness=2)

        # Hide dialog until we've configured it
        self.geometry("0x0+0+0")
        # Make the dialog appear on top of its parent
        self.transient(master)
        # Make the dialog modal
        self.grab_set()
        # Remove window border
        self.overrideredirect(True)
        # Make the geometry update
        self.update_idletasks()

        self._title = kwargs.get('title')
        self._width = kwargs.get('width', master.winfo_width() // 2)
        self._height = kwargs.get('height', master.winfo_height() // 2)
        self._x_offset = master.winfo_rootx() + ((master.winfo_width() - self._width) // 2)
        self._y_offset = master.winfo_rooty() + ((master.winfo_height() - self._height) // 2)
        self._justify = kwargs.get('justify', 'center')

        self.geometry("%dx%d+%d+%d" % (self._width, self._height, self._x_offset, self._y_offset))

        self._canvas = tk.Canvas(self, width=self._width, height=self._height, bg='#000000', highlightthickness=0)
        self._canvas.pack()

        self._init_submit_button(**kwargs)
        self._init_cancel_button(**kwargs)
        self._init_message(message)

        timeout = kwargs.get('timeout')
        if timeout:
            self.after(timeout*1000, self.destroy)

    def _init_submit_button(self, **kwargs):
        if kwargs.get('show_submit', True):
            text = kwargs.get('submit_text', ' OK ')

            def submit(_):
                self.destroy()
                onsubmit = kwargs.get('onsubmit')
                if callable(onsubmit):
                    onsubmit()

            CanvasButton(self._canvas, text, (self._width - 50, self._height - 50), onpress=submit)

    def _init_cancel_button(self, **kwargs):
        if kwargs.get('show_cancel', False):
            text = kwargs.get('submit_text', 'CANCEL')

            def cancel(_):
                self.destroy()
                oncancel = kwargs.get('oncancel')
                if callable(oncancel):
                    oncancel()

            CanvasButton(self._canvas, text, (57, self._height - 50), onpress=cancel)

    def _init_message(self, message):
        title = None
        if self._title is not None:
            title = self._canvas.create_text(
                (self._width // 2, 40),
                text=self._title,
                font=settings.fonts['dialog_title'],
                width=self._width - 40,
                justify='center',
                fill='#FFFFFF'
            )

        y = (self._height // 2) - 20

        if title:
            y = self._canvas.coords(title)[1] + 60

        self._canvas.create_text(
            self._width // 2, y,
            text=message,
            font=settings.fonts['dialog_message'],
            width=self._width - 40,
            justify=self._justify,
            fill='#FFFFFF'
        )


class CanvasButton:
    """Represents a button drawn onto the canvas."""

    DISABLED_COLOUR = '#404040'

    def __init__(self, canvas, text, pos, onpress, lockable=False, **kwargs):
        """Initialise a new CanvasButton.

        Args:
            text: The text of the button.
            pos: The x,y point (2-tuple) that the button will be centred around.
            onpress: The callback for when the button is pressed. This will receive
                a single parameter: the text of the pressed button.
            lockable: Whether the button is a lockable button (e.g. a caps lock key).
                Lockable buttons remain pressed until they are pressed again.
            **kwargs: Additional arguments that can be used to configure the button:
                font: The font to use.
                text_colour: The text colour to use (default 'white').
                width: The width of the button (will override padding).
                height: The height of the button (will override padding).
                padding: The padding between the text and the edge of the button
                    (default: 10).
                disabled: Whether to disable the button.
        Returns:
            A CanvasButton object that represents the rendered button.
        """
        self._canvas = canvas
        self._text = text
        self._pos = pos
        self._onpress = onpress
        self._lockable = lockable
        self._options = kwargs

        self._locked = False
        self._fade = Fade(canvas)
        self._btext, self._button = self._draw_button(text, pos, kwargs.get('disabled', False))
        self._configure_button(kwargs.get('disabled', False))

    def _draw_button(self, text, pos, disabled=False):
        args = {
            'text': text,
            'fill': self._options.get('text_colour', '#ffffff')
            if not disabled else self.DISABLED_COLOUR,
            'font': self._options.get('font', settings.fonts['button_standard'])
        }

        text = self._canvas.create_text(pos[0], pos[1], **args)
        bbox = self._canvas.bbox(text)
        padding = self._options.get('padding', 10)
        width = self._options.get('width', ((bbox[2] - bbox[0]) + (padding * 2)))
        height = self._options.get('height', ((bbox[3] - bbox[1]) + (padding * 2)))
        x_offset = (width - (bbox[2] - bbox[0])) // 2
        y_offset = (height - (bbox[3] - bbox[1])) // 2

        args = {
            'outline': '#ffffff' if not disabled else self.DISABLED_COLOUR,
            'fill': '#000000'
        }

        button = self._round_rectangle(bbox[0] - x_offset, bbox[1] - y_offset,
                                       bbox[2] + x_offset, bbox[3] + y_offset, **args)

        self._canvas.tag_raise(text)

        return text, button

    def _round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """Taken from: https://stackoverflow.com/a/44100075/2091925"""

        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        return self._canvas.create_polygon(points, **kwargs, smooth=True)

    def _configure_button(self, disabled):
        def onpress(_):
            self._canvas.itemconfigure(self._button, fill='#ffffff')
            self._canvas.itemconfigure(self._btext, fill='#000000')

            if settings.touchscreen:
                # Ensure that the button is eventually released, even if
                # the ButtonRelease event is never received. This sometimes
                # seen on the raspberry pi touchscreen, but not normally
                # with a mouse.
                def release():
                    if not self._locked:
                        self._fade.fadeout(self._button, duration=20)
                        self._canvas.itemconfigure(self._btext, fill='#ffffff')
                self._canvas.master.after(500, release)

        def onrelease(_):
            if self._lockable:
                self._locked = not self._locked

            if not self._locked:
                self._fade.fadeout(self._button, duration=20)
                self._canvas.itemconfigure(self._btext, fill='#ffffff')

            self._onpress(self.text)

        if not disabled:
            self._canvas.tag_bind(self._btext, '<ButtonPress-1>', onpress)
            self._canvas.tag_bind(self._button, '<ButtonPress-1>', onpress)
            self._canvas.tag_bind(self._btext, '<ButtonRelease-1>', onrelease)
            self._canvas.tag_bind(self._button, '<ButtonRelease-1>', onrelease)

    @property
    def text(self):
        """Get the text of the button.

        Returns:
            The button text.
        """
        return self._canvas.itemcget(self._btext, 'text')

    @text.setter
    def text(self, text):
        """Set the text of the button.

        Args:
            text: The button text to set.
        """
        self._canvas.itemconfigure(self._btext, text=text)

    def disable(self, disabled):
        """Set the disabled state of the button.

        Args:
            disabled: True if the button should be disabled,
                False if it should be enabled.
        """
        self._canvas.delete(self._btext, self._button)
        self._btext, self._button = self._draw_button(self._text, self._pos, disabled)
        self._configure_button(disabled)


class Fade:
    """A mechanism of fading a canvas item."""

    def __init__(self, canvas):
        self._canvas = canvas

    def fadein(self, item, colour, **kwargs):
        """Fade the specified canvas item from black to its current colour.

        Args:
            item: The canvas item to fade in.
            colour: The colour to fade to.
            **kwargs: Addition keyword arguments that can be used to configure the fade
                behaviour:
                duration: The duration in ms of the fade (default 1000).
                elements: The parts of the item to be faded - a sequence of
                    names. Default ['fill']
                onfaded: Optional callback which will be called once the fade
                    has completed.


        """
        duration = kwargs.get('duration', 1000)
        red, green, blue = struct.unpack('BBB', bytes.fromhex(colour[1:]))
        slices = max((duration // 100), 10)
        increment = max(max((red, green, blue)) // slices, 1)

        def fade(r, g, b):
            if r < red:
                r += increment
                r = min(r, red)
            if g < green:
                g += increment
                g = min(g, green)
            if b < blue:
                b += increment
                b = min(b, blue)
            faded = '#%02x%02x%02x' % (r, g, b)
            config = {}
            for element in kwargs.get('elements', ['fill']):
                config[element] = faded
            self._canvas.itemconfigure(item, **config)
            if sum((r, g, b)) < sum((red, green, blue)):
                self._canvas.master.after(duration // slices, lambda: fade(r, g, b))
            else:
                onfaded = kwargs.get('onfaded')
                if callable(onfaded):
                    onfaded()

        fade(0, 0, 0)

    def fadeout(self, item, **kwargs):
        """Fade the specified canvas item from its current colour to black.

        Args:
            item: The canvas item to fade out.
            **kwargs: Addition keyword arguments that can be used to configure the fade
                behaviour:
                duration: The duration in ms of the fade (default 1000).
                elements: The parts of the item to be faded - a sequence of
                    names. Default ['fill']
                onfaded: Optional callback which will be called once the fade
                    has completed.

        """
        duration = kwargs.get('duration', 1000)
        current_colour = self._canvas.itemcget(item, 'fill')
        red, green, blue = struct.unpack('BBB', bytes.fromhex(current_colour[1:]))
        slices = max((duration // 100), 10)
        decrement = max(max((red, green, blue)) // slices, 1)

        def fade(r, g, b):
            r -= decrement
            g -= decrement
            b -= decrement
            r, g, b = max(r, 0), max(g, 0), max(b, 0)
            faded = '#%02x%02x%02x' % (r, g, b)
            config = {}
            for element in kwargs.get('elements', ['fill']):
                config[element] = faded
            self._canvas.itemconfigure(item, **config)
            if sum((r, g, b)) > 0:
                self._canvas.master.after(duration // slices, lambda: fade(r, g, b))
            else:
                onfaded = kwargs.get('onfaded')
                if callable(onfaded):
                    onfaded()

        fade(red, green, blue)

