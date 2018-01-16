import platform


# Whether we're running on the Raspberry PI touchscreen display.
touchscreen = None

# Default fonts
fonts = {
    'homescreen_kanoodle': ('wood stamp', 80),
    'homescreen_genius': ('KG Counting Stars', 60),
    'homescreen_2d': ('cube vol.2', 36),
    'screen_title': ('wood stamp', 36),
    'gamescreen_intro': ('wood stamp', 60),
    'gamescreen_player': ('wood stamp', 28),
    'gamescreen_status': ('wood stamp', 22),
    'player_name': ('FreeSans', 18, 'bold'),
    'puzzles_completed': ('FreeSans', 16),
    'button_standard': ('wood stamp', 24),
    'button_keyboard': ('FreeSans', 16),
    'dialog_title': ('wood stamp', 36),
    'dialog_message': ('FreeSans', 16),
}

# Small offsets required to centre the sphere images on certain devices.
image_offsets = {
    'x': 1,
    'y': 1,
}

# System specific overrides
if platform.system() == 'Darwin':  # MacOS
    fonts['homescreen_kanoodle'] = ('wood stamp', 104)
    fonts['homescreen_genius'] = ('KG Counting Stars', 78)
    fonts['homescreen_2d'] = ('cube vol.2', 48)
    fonts['screen_title'] = ('wood stamp', 48)
    fonts['button_standard'] = ('wood stamp', 30)
    fonts['button_keyboard'] = ('helvetica', 18)
    fonts['player_name'] = ('helvetica', 22, 'bold')
    fonts['puzzles_completed'] = ('helvetica', 18)
    fonts['gamescreen_intro'] = ('wood stamp', 80)
    fonts['gamescreen_player'] = ('wood stamp', 38)
    fonts['gamescreen_status'] = ('wood stamp', 30)
    fonts['dialog_message'] = ('helvetica', 18)
    fonts['dialog_title'] = ('wood stamp', 48)

    image_offsets['x'] = 0
    image_offsets['y'] = 0

# Whether to show the mouse pointer
show_cursor = None

# Whether to show numbers in each hole on the board (useful for debugging)
show_board_numbers = False

# When admin mode is True, players can be deleted
admin_mode = False


def initialise(tk):
    """Initialise the settings with a Tk widget instance.

    Args:
        tk: A Tkinter widget instance.
    """
    global touchscreen
    touchscreen = platform.system() == 'Linux' and (tk.winfo_screenwidth() == 800 and tk.winfo_screenheight() == 480)

    global show_cursor
    show_cursor = not touchscreen
