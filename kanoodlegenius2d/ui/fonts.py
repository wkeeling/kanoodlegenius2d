import os
from shutil import copyfile


def initialise():
    """Initialise the game fonts, placing them into the necessary directory."""
    fonts_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'fonts')
    target_dir = os.path.join(os.path.expanduser('~'), '.fonts')

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for font in os.listdir(fonts_dir):
        source = os.path.join(fonts_dir, font)
        target = os.path.join(target_dir, font)
        if not os.path.exists(target):
            copyfile(source, target)
