from kanoodlegenius2d.domain import models
from kanoodlegenius2d.ui import fonts, settings
from kanoodlegenius2d.ui.masterscreen import MasterScreen


def main():
    fonts.initialise()
    settings.initialise()
    models.initialise()
    return MasterScreen()
