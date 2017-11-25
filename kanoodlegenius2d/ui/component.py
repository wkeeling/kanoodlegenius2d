
class CanvasWidgetCreator:
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
        text = self._canvas.create_text(pos[0], pos[1], text=text, fill=kwargs.get('text_colour', 'white'))
        bbox = self._canvas.bbox(text)
        padding = kwargs.get('padding', 10)
        width = kwargs.get('width', ((bbox[2] - bbox[0]) + (padding * 2)))
        height = kwargs.get('height', ((bbox[3] - bbox[1]) + (padding * 2)))
        x_offset = (width - (bbox[2] - bbox[0])) // 2
        y_offset = (height - (bbox[3] - bbox[1])) // 2

        button = self._canvas.create_rectangle((bbox[0] - x_offset, bbox[1] - y_offset,
                                                bbox[2] + x_offset, bbox[3] + y_offset),
                                               outline='white', fill='black')
        self._canvas.tag_raise(text)

        def on_press(_):
            self._canvas.itemconfigure(button, fill='white')
            self._canvas.itemconfigure(text, fill='black')

        def on_release(_):
            self._canvas.itemconfigure(button, fill='black')
            self._canvas.itemconfigure(text, fill='white')
            self._canvas.tag_bind(text, '<ButtonRelease-1>', onclick)
            self._canvas.tag_bind(button, '<ButtonRelease-1>', onclick)

        self._canvas.tag_bind(text, '<ButtonPress-1>', on_press)
        self._canvas.tag_bind(button, '<ButtonPress-1>', on_press)
        self._canvas.tag_bind(text, '<ButtonRelease-1>', on_release)
        self._canvas.tag_bind(button, '<ButtonRelease-1>', on_release)


def fade(canvas_item, to_colour, **kwargs):
    """Fade the specified canvas item from its current colour to the specified
    colour.

    Args:
        canvas_item:
            The canvas item to fade.
        to_colour:
            The colour to fade to.
        kwargs:
            Addition keyword arguments that can be used to configure the fade
            behaviour.
                duration: The duration in ms of the fade (default 1000).

    """

    pass
