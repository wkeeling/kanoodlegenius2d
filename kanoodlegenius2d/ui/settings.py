import platform


# Default fonts
fonts = {
    'homescreen_kanoodle': ('wood stamp', 80),
    'homescreen_genius': ('KG Counting Stars', 60),
    'homescreen_2d': ('cube vol.2', 36),
    'screen_title': ('wood stamp', 36),
    'gamescreen_player': ('wood stamp', 28),
    'gamescreen_status': ('wood stamp', 22),
    'player_name': ('FreeSans', 18),
    'button_standard': 'FreeSans',
    'button_keyboard': ('FreeSans', 16),
    'dialog_title': ('wood stamp', 28),
    'dialog_message': ('FreeSans', 18)
}

# System specific font overrides
if platform.system() == 'Darwin':  # MacOS
    fonts['homescreen_kanoodle'] = ('wood stamp', 104)
    fonts['homescreen_genius'] = ('KG Counting Stars', 78)
    fonts['homescreen_2d'] = ('cube vol.2', 48)
    fonts['screen_title'] = ('wood stamp', 48)
    fonts['button_standard'] = ('helvetica', 16)
    fonts['button_keyboard'] = ('helvetica', 18)
    fonts['player_name'] = ('helvetica', 22)
    fonts['gamescreen_player'] = ('wood stamp', 38)
    fonts['gamescreen_status'] = ('wood stamp', 28)

