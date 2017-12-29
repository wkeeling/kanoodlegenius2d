from unittest import TestCase

from peewee import SqliteDatabase


test_db = SqliteDatabase(':memory:')


class ModelTestCase(TestCase):
    requires = None

    def setUp(self):
        super(ModelTestCase, self).setUp()
        if self.requires:
            self.orig = []
            for m in self.requires:
                self.orig.append(m._meta.database)
                m._meta.database = test_db
            test_db.drop_tables(self.requires, True)
            test_db.create_tables(self.requires)

    def tearDown(self):
        super(ModelTestCase, self).tearDown()
        if self.requires:
            test_db.drop_tables(self.requires, True)
            for i, m in enumerate(self.requires):
                m._meta.database = self.orig[i]