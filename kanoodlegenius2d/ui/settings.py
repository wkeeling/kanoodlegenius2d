import platform


# Default fonts
fonts = {
    'homescreen_kanoodle': ('wood stamp', 80),
    'homescreen_genius': ('KG Counting Stars', 60),
    'homescreen_2d': ('cube vol.2', 36),
    'screen_title': ('wood stamp', 48),
    'gamescreen_player': ('wood stamp', 28),
    'gamescreen_status': ('wood stamp', 20),
    'player_name': ('FreeSans', 18),
    'button_standard': 'FreeSans',
    'button_keyboard': ('FreeSans', 16),
    'dialog_title': ('wood stamp', 28),
    'dialog_message': ('FreeSans', 18)
}

# System specific font overrides
if platform.system() == 'Darwin':
    fonts['button_standard'] = 'helvetica'
