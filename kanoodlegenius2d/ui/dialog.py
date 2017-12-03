import tkinter as tk

from kanoodlegenius2d.ui.util import CanvasWidgetHelper


class Dialog(tk.Toplevel):
    """A popup panel which overlays the frame beneath it and can be closed by the user."""

    def __init__(self, message, master=None, **kwargs):
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

        self._width = kwargs.get('width', master.winfo_width() // 2)
        self._height = kwargs.get('height', master.winfo_height() // 2)
        self._x_offset = master.winfo_rootx() + ((master.winfo_width() - self._width) // 2)
        self._y_offset = master.winfo_rooty() + ((master.winfo_height() - self._height) // 2)

        self.geometry("%dx%d+%d+%d" % (self._width, self._height, self._x_offset, self._y_offset))

        self._canvas = tk.Canvas(self, width=self._width, height=self._height, bg='#000000', highlightthickness=0)
        self._canvas.pack()
        self._widget_helper = CanvasWidgetHelper(self._canvas)

        self._init_submit_button(**kwargs)
        self._init_cancel_button(**kwargs)
        self._init_message(message)

        timeout = kwargs.get('timeout')
        if timeout:
            self.after(timeout*1000, self.destroy)

    def _init_submit_button(self, **kwargs):
        if kwargs.get('show_submit', True):
            text = kwargs.get('submit_text', ' OK ')

            def submit():
                self.destroy()
                onsubmit = kwargs.get('onsubmit')
                if callable(onsubmit):
                    onsubmit()

            self._widget_helper.create_button(text, (self._width - 50, self._height - 40),
                                              font='helvetica', onclick=submit)

    def _init_cancel_button(self, **kwargs):
        if kwargs.get('show_cancel', False):
            text = kwargs.get('submit_text', 'CANCEL')

            def cancel():
                self.destroy()
                oncancel = kwargs.get('oncancel')
                if callable(oncancel):
                    oncancel()

            self._widget_helper.create_button(text, (60, self._height - 40),
                                              font='helvetica', onclick=cancel)

    def _init_message(self, message):
        self._canvas.create_text((self._width // 2, (self._height // 2) - 20), text=message,
                                 font=('helvetica', 18), width=self._width - 40,
                                 justify='center', fill='#FFFFFF')


def display_dialog(message, master=None, **kwargs):
    """Initialise and display a new dialog popup.

    Args:
        message:
            The text to display on the dialog.
        master:
            The parent widget.
        kwargs:
            Optional keyword arguments that can include:
                width:
                    The width of the dialog in pixels (default 50% of parent).
                height:
                    The height of the dialog in pixels (default 50% of parent).
                show_submit:
                    Whether to show a submit button (default True).
                submit_text:
                    The text of the submit button (default OK).
                onsubmit:
                    Callable invoked when the submit button pressed (default None).
                show_cancel:
                    Whether to show a cancel button (default False).
                cancel_text:
                    The text of the cancel button when shown (default CANCEL).
                oncancel:
                    Callable invoked when the cancel button pressed (default None).
                timeout:
                    The number of seconds after which to automatically cancel the
                    dialog (default None - no auto-cancel).
    """
    Dialog(message, master=master, **kwargs)
