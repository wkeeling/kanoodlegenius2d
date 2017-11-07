import os
import sqlite3
from unittest import TestCase

from kanoodlegenius2d.models import (Game,
                                     initialise)


class InitialiseTest(TestCase):

    def test_initialise_database(self):
        initialise()
        self.assertTrue(os.path.exists(self._datafile_path))
        conn = sqlite3.connect(self._datafile_path)
        tables = [t[0] for t in conn.execute("SELECT name FROM sqlite_master WHERE type='table';")]
        self.assertIn('puzzle', tables)

    def setUp(self):
        self._datafile_path = os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db')

    def tearDown(self):
        try:
            os.remove(self._datafile_path)
        except OSError:
            pass


class StartNewGameTest(TestCase):

    def test_start_new_game(self):
        """Test assemble the model objects needed to begin a new game."""
        game = Game.start('test_player')

    def setUp(self):
        self._datafile_path = os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db')
        initialise()

    def tearDown(self):
        try:
            os.remove(self._datafile_path)
        except OSError:
            pass