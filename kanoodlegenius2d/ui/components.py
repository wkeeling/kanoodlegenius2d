import struct


class Fade:
    """A mechanism of fading a canvas item."""

    def __init__(self, canvas):
        self._canvas = canvas

    def fadein(self, item, colour, **kwargs):
        """Fade the specified canvas item from black to its current colour.

        Args:
            item:
                The canvas item to fade in.
            colour:
                The colour to fade to.
            kwargs:
                Addition keyword arguments that can be used to configure the fade
                behaviour.
                    duration:
                        The duration in ms of the fade (default 1000).
                    elements:
                        The parts of the item to be faded - a sequence of
                        names. Default ['fill']
                    onfaded:
                        Optional callback which will be called once the fade
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
            item:
                The canvas item to fade out.
            kwargs:
                Addition keyword arguments that can be used to configure the fade
                behaviour.
                    duration:
                        The duration in ms of the fade (default 1000).
                    elements:
                        The parts of the item to be faded - a sequence of
                        names. Default ['fill']
                    onfaded:
                        Optional callback which will be called once the fade
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


class CanvasButton:
    """Represents a button drawn onto the canvas."""

    def __init__(self, canvas, text, pos, onclick, lockable=False, **kwargs):
        """Initialise a new CanvasButton.

        Args:
            text:
                The text of the button.
            pos:
                The x,y point (2-tuple) that the button will be centred around.
            onclick:
                The callback for when the button is clicked. This will receive
                a single parameter: the text of the clicked button.
            lockable:
                Whether the button is a lockable button (e.g. a caps lock key).
                Lockable buttons remain pressed until they are pressed again.
            kwargs:
                Additional arguments that can be used to configure the
                button.
                    font:
                        The font to use.
                    text_colour:
                        The text colour to use (default 'white').
                    width:
                        The width of the button (will override padding).
                    height:
                        The height of the button (will override padding).
                    padding:
                        The padding between the text and the edge of the button
                        (default: 10).
        Returns:
            A CanvasButton object that represents the rendered button.
        """
        self._canvas = canvas
        self._text, self._button = self._draw_button(text, pos, **kwargs)
        self._locked = False
        self._fade = Fade(canvas)

        def onpress(_):
            self._canvas.itemconfigure(self._button, fill='#ffffff')
            self._canvas.itemconfigure(self._text, fill='#000000')

        def onrelease(_):
            if lockable:
                self._locked = not self._locked

            if not self._locked:
                self._fade.fadeout(self._button, duration=20)
                self._canvas.itemconfigure(self._text, fill='#ffffff')

            onclick(self.text)

        self._canvas.tag_bind(self._text, '<ButtonPress-1>', onpress)
        self._canvas.tag_bind(self._button, '<ButtonPress-1>', onpress)
        self._canvas.tag_bind(self._text, '<ButtonRelease-1>', onrelease)
        self._canvas.tag_bind(self._button, '<ButtonRelease-1>', onrelease)

    def _draw_button(self, text, pos, **kwargs):
        args = {
            'text': text,
            'fill': kwargs.get('text_colour', '#ffffff')
        }
        if 'font' in kwargs:
            args['font'] = kwargs['font']

        text = self._canvas.create_text(pos[0], pos[1], **args)
        bbox = self._canvas.bbox(text)
        padding = kwargs.get('padding', 10)
        width = kwargs.get('width', ((bbox[2] - bbox[0]) + (padding * 2)))
        height = kwargs.get('height', ((bbox[3] - bbox[1]) + (padding * 2)))
        x_offset = (width - (bbox[2] - bbox[0])) // 2
        y_offset = (height - (bbox[3] - bbox[1])) // 2

        button = self._canvas.create_rectangle((bbox[0] - x_offset, bbox[1] - y_offset,
                                                bbox[2] + x_offset, bbox[3] + y_offset),
                                               outline='#ffffff', fill='#000000')

        self._canvas.tag_raise(text)

        return text, button

    @property
    def text(self):
        """Get the text of the button.

        Returns:
            The button text.
        """
        return self._canvas.itemcget(self._text, 'text')

    @text.setter
    def text(self, text):
        """Set the text of the button.

        Args:
            text:
                The button text to set.
        """
        self._canvas.itemconfigure(self._text, text=text)
