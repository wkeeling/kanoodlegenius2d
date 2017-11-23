

class CanvasButton:
    """Represents a clickable button drawn onto a canvas widget."""

    def __init__(self, canvas, x, y, w, h, text, on_click=None, **kwargs):
        x1, y1, x2, y2 = x, y, x + w, y + h
        button = canvas.create_rectangle((x1, y1, x2, y2), outline='white', fill='black')
        x_offset = (x2 - x1) // 2
        y_offset = (y2 - y1) // 2
        text = canvas.create_text(x + x_offset, y + y_offset, text=text,
                                  fill=kwargs.get('text_colour', 'white'))

