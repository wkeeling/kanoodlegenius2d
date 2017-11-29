import tkinter as tk


class Dialog(tk.Toplevel):
    """A popup panel which overlays the frame beneath it and can be closed by the user."""

    def __init__(self, title, message, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        # Make the dialog appear on top of its parent
        self.transient(master)
        # Make the dialog modal
        self.grab_set()
        # Remove window border
        self.overrideredirect(True)
        self.update_idletasks()

        # self.geometry("%dx%d" % (200, 120))
        self.title = title
        self._message = tk.Message(self, text=message)
        self._message.pack()