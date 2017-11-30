import tkinter as tk

from kanoodlegenius2d.ui.util import CanvasWidgetHelper


class Dialog(tk.Toplevel):
    """A popup panel which overlays the frame beneath it and can be closed by the user."""

    def __init__(self, message, master=None, **kwargs):
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
                        The text of the cancel button when shown (default Cancel).
                    oncancel:
                        Callable invoked when the cancel button pressed (default None).
                    timeout:
                        The number of seconds after which to automatically submit the
                        dialog (default None - no auto-submit).
        """
        super().__init__(master, bg='#000000', highlightthickness=1)

        # Make the dialog appear on top of its parent
        self.transient(master)
        # Make the dialog modal
        self.grab_set()
        # Remove window border
        self.overrideredirect(True)
        # Make the geometry update
        self.update_idletasks()

        width = kwargs.get('width', master.winfo_width() // 2)
        height = kwargs.get('height', master.winfo_height() // 2)

        self.geometry("%dx%d+%d+%d" % (width, height,
                                       master.winfo_rootx() + ((master.winfo_width() - width) // 2),
                                       master.winfo_rooty() + ((master.winfo_height() - height) // 2)))

        canvas = tk.Canvas(self, width=width, height=height, bg='#000000', highlightthickness=0)
        canvas.pack()
        self._widget_helper = CanvasWidgetHelper(canvas)

        self._init_submit_button(**kwargs)

    def _init_submit_button(self, **kwargs):
        if kwargs.get('show_submit', True):
            text = kwargs.get('submit_text', ' OK ')

            def submit():
                self.destroy()
                onsubmit = kwargs.get('onsubmit')
                if callable(onsubmit):
                    onsubmit()

            self._widget_helper.create_button(text, (self.winfo_x() + self.winfo_width() - 100,
                                                     self.winfo_y() - self.winfo_height() - 100),
                                              font='helvetica', onclick=submit)

