import tkinter as tk

from kanoodlegenius2d.ui.util import CanvasWidgetHelper


class Dialog(tk.Toplevel):
    """A popup panel which overlays the frame beneath it and can be closed by the user."""

    def __init__(self, message, master=None, cnf=None, **kw):
        # need timeout that will override buttons
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, bg='#000000', highlightthickness=1, **kw)

        # Make the dialog appear on top of its parent
        self.transient(master)
        # Make the dialog modal
        self.grab_set()
        # Remove window border
        self.overrideredirect(True)

        self.update_idletasks()
        width, height = master.winfo_width() // 2, master.winfo_height() // 2
        self.geometry("%dx%d+%d+%d" % (width, height,
                                       master.winfo_rootx() + ((master.winfo_width() - width) // 2),
                                       master.winfo_rooty() + ((master.winfo_height() - height) // 2)))

        print(master.winfo_x(), master.winfo_y(), master.winfo_geometry())
        print(master.winfo_rootx(), master.winfo_rooty(), master.winfo_geometry())




        # self.geometry("%dx%d" % (200, 120))
        canvas = tk.Canvas(self, width=500, height=300, bg='#000000', highlightthickness=0)
        canvas.pack()
        widget_helper = CanvasWidgetHelper(canvas)
        widget_helper.create_button(' OK ', (100, 100), font='helvetica', onclick=lambda: self.destroy())

