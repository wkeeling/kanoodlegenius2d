
class CanvasWidgetCreator:
    """Helper class for rendering widgets on an existing canvas."""

    def __init__(self, canvas):
        """Initialise a new CanvasWidgetCreator with an existing canvas object.

        Args:
            canvas:
                The canvas object.
        """
        self._canvas = canvas

    def create_button(self, text, centre, onclick, **kwargs):
        """Create a clickable canvas button.

        Args:
            text:
                The text of the button.
            centre:
                The x,y point (2-tuple) that the button will be centred around.
            onclick:
                The callback for when the button is clicked.
            kwargs:
                Additional arguments that can be used to configure the
                button.
        """
        text = self._canvas.create_text(centre[0], centre[1], text=text, fill=kwargs.get('text_colour', 'white'))
        bbox = self._canvas.bbox(text)
        padding = 10
        button = self._canvas.create_rectangle((bbox[0] - padding, bbox[1] - padding,
                                                bbox[2] + padding, bbox[3] + padding),
                                               outline='white', fill='black')
        self._canvas.tag_raise(text)
        if onclick is not None:
            self._canvas.tag_bind(button, '<ButtonPress-1>', onclick)

