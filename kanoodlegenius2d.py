#!/usr/bin/env python3
from kanoodlegenius2d.domain import models
from kanoodlegenius2d.ui import fonts, settings
from kanoodlegenius2d.ui.masterscreen import MasterScreen


fonts.initialise()
settings.initialise()
models.initialise()
MasterScreen()
