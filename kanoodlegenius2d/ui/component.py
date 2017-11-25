import struct
import time


class CanvasWidgetHelper:
    """Helper class for rendering widgets on an existing canvas."""

    def __init__(self, canvas):
        """Initialise a new CanvasWidgetCreator with an existing canvas object.

        Args:
            canvas:
                The canvas object.
        """
        self._canvas = canvas

    def create_button(self, text, pos, onclick, **kwargs):
        """Create a clickable canvas button.

        Args:
            text:
                The text of the button.
            pos:
                The x,y point (2-tuple) that the button will be centred around.
            onclick:
                The callback for when the button is clicked.
            kwargs:
                Additional arguments that can be used to configure the
                button.
                    text_colour:
                        The text colour to use (default 'white').
                    width:
                        The width of the button (will override padding).
                    height:
                        The height of the button (will override padding).
                    padding:
                        The padding between the text and the edge of the button
                        (default: 10).
        """
        text = self._canvas.create_text(pos[0], pos[1], text=text, fill=kwargs.get('text_colour', '#FFFFFF'))
        bbox = self._canvas.bbox(text)
        padding = kwargs.get('padding', 10)
        width = kwargs.get('width', ((bbox[2] - bbox[0]) + (padding * 2)))
        height = kwargs.get('height', ((bbox[3] - bbox[1]) + (padding * 2)))
        x_offset = (width - (bbox[2] - bbox[0])) // 2
        y_offset = (height - (bbox[3] - bbox[1])) // 2

        button = self._canvas.create_rectangle((bbox[0] - x_offset, bbox[1] - y_offset,
                                                bbox[2] + x_offset, bbox[3] + y_offset),
                                               outline='white', fill='#000000')
        self._canvas.tag_raise(text)

        def on_press(_):
            self._canvas.itemconfigure(button, fill='#ffffff')
            self._canvas.itemconfigure(text, fill='#000000')

        def on_release(_):
            self.fadeout(button, duration=50)
            self._canvas.itemconfigure(text, fill='#ffffff')
            onclick()

        self._canvas.tag_bind(text, '<ButtonPress-1>', on_press)
        self._canvas.tag_bind(button, '<ButtonPress-1>', on_press)
        self._canvas.tag_bind(text, '<ButtonRelease-1>', on_release)
        self._canvas.tag_bind(button, '<ButtonRelease-1>', on_release)

    def fadeout(self, item, **kwargs):
        """Fade the specified canvas item from its current colour to black.

        Args:
            item:
                The canvas item to fade out.
            kwargs:
                Addition keyword arguments that can be used to configure the fade
                behaviour.
                    duration: The duration in ms of the fade (default 1000).

        """
        duration = kwargs.get('duration', 1000)
        current_colour = self._canvas.itemcget(item, 'fill')
        red, green, blue = struct.unpack('BBB', bytes.fromhex(current_colour[1:]))
        slices = max((duration // 100), 10)
        decrement = (max((red, green, blue)) // slices)

        def fade(r, g, b):
            print('time: {}, {}'.format(time.time(), r))
            r -= decrement
            g -= decrement
            b -= decrement
            r, g, b = max(r, 0), max(g, 0), max(b, 0)
            faded = '#%02x%02x%02x' % (r, g, b)
            self._canvas.itemconfigure(item, fill=faded)
            if sum((r, g, b)) > 0:
                self._canvas.master.after(duration // slices, lambda: fade(r, g, b))

        fade(red, green, blue)
