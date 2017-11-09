import os
import sqlite3
from unittest import TestCase

from peewee import SqliteDatabase
from playhouse.test_utils import test_database

from kanoodlegenius2d.models import (Game,
                                     initialise,
                                     Noodle,
                                     shutdown)
from kanoodlegenius2d.orientation import Orientation

test_db = SqliteDatabase(':memory:')


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
        shutdown()
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
        shutdown()
        try:
            os.remove(self._datafile_path)
        except OSError:
            pass


class NoodleTest(TestCase):

    def test_rotate_noodle_single_increment(self):
        with test_database(test_db, (Noodle,), create_tables=True):
            Noodle.create(designation='D', code='light_blue',
                          part1=Orientation.E,
                          part2=Orientation.E,
                          part3=Orientation.NE,
                          part4=Orientation.SE)

            light_blue = Noodle.get(Noodle.code == 'light_blue')
            light_blue.rotate()

            self.assertEqual(light_blue.part1, Orientation.SE)
            self.assertEqual(light_blue.part2, Orientation.SE)
            self.assertEqual(light_blue.part3, Orientation.E)
            self.assertEqual(light_blue.part4, Orientation.SW)

    def test_rotate_noodle_multiple_increments(self):
        with test_database(test_db, (Noodle,), create_tables=True):
            Noodle.create(designation='D', code='light_blue',
                          part1=Orientation.E,
                          part2=Orientation.E,
                          part3=Orientation.NE,
                          part4=Orientation.SE)

            light_blue = Noodle.get(Noodle.code == 'light_blue')
            light_blue.rotate(3)

            self.assertEqual(light_blue.part1, Orientation.W)
            self.assertEqual(light_blue.part2, Orientation.W)
            self.assertEqual(light_blue.part3, Orientation.SW)
            self.assertEqual(light_blue.part4, Orientation.NW)