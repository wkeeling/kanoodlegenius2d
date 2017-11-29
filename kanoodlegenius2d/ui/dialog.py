import tkinter as tk

from kanoodlegenius2d.ui.util import CanvasWidgetHelper


class Dialog(tk.Toplevel):
    """A popup panel which overlays the frame beneath it and can be closed by the user."""

    def __init__(self, message, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, bg='#000000', highlightthickness=1, **kw)
        print(master.winfo_x(), master.winfo_rootx(), master.winfo_geometry())

        # Make the dialog appear on top of its parent
        self.transient(master)
        # Make the dialog modal
        self.grab_set()
        # Remove window border
        self.overrideredirect(True)


        width, height = 500, 300


        self.geometry("%dx%d+%d+%d" % (500, 300, 100, 100))

        # self.geometry("%dx%d" % (200, 120))
        canvas = tk.Canvas(self, width=500, height=300, bg='#000000', highlightthickness=0)
        canvas.pack()
        widget_helper = CanvasWidgetHelper(canvas)
        widget_helper.create_button(' OK ', (100, 100), font='helvetica', onclick=lambda: self.destroy())

