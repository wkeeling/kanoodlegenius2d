from unittest import TestCase

from peewee import SqliteDatabase
from playhouse.test_utils import test_database

from kanoodlegenius2d.models import (Noodle,
                                     Orientation)

test_db = SqliteDatabase(':memory:')


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
