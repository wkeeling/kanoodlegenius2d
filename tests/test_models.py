import os
import sqlite3
from unittest import TestCase

from kanoodlegenius2d.models import initialise


class InitialiseTest(TestCase):

    def test_initialise_database(self):
        datafile_path = os.path.join(os.path.expanduser('~'), '.kanoodlegenius2d.db')
        try:
            initialise()
            self.assertTrue(os.path.exists(datafile_path))
            conn = sqlite3.connect(datafile_path)
            tables = [t[0] for t in conn.execute("SELECT name FROM sqlite_master WHERE type='table';")]
            self.assertIn('puzzle', tables)
        finally:
            try:
                os.remove(datafile_path)
            except OSError:
                pass
