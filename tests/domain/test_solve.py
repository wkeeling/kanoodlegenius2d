from unittest import TestCase

from kanoodlegenius2d.domain.models import Noodle, orientation
from kanoodlegenius2d.domain.solve import NoodleManipulator


class NoodleManipulatorTest(TestCase):

    def setUp(self):
        self._create_manipulator()

    def _create_manipulator(self, symmetrical=False):
        self._yellow = Noodle(designation='B', colour='yellow',
                              part1=orientation.E, part2=orientation.NE,
                              part3=orientation.SE, part4=orientation.NE)
        self._red = Noodle(designation='E', colour='#e60000',
                           part1=orientation.NE, part2=orientation.SE,
                           part3=orientation.NE, part4=orientation.SE)
        if not symmetrical:
            self._manipulator = NoodleManipulator(self._yellow)
        else:
            self._manipulator = NoodleManipulator(self._red, symmetrical=True)

    def test_noodle_first_iteration(self):
        pos = self._manipulate()

        self.assertEqual(id(pos.noodle), id(self._yellow))
        self.assertEqual(pos.noodle.part1, orientation.SE)
        self.assertEqual(pos.noodle.part2, orientation.E)
        self.assertEqual(pos.noodle.part3, orientation.SW)
        self.assertEqual(pos.noodle.part4, orientation.E)

    def test_part_first_iteration(self):
        pos = self._manipulate()

        self.assertEqual(pos.part, 0)

    def test_hole_first_iteration(self):
        pos = self._manipulate()

        self.assertEqual(pos.hole, 0)

    def test_noodle_n_iterations(self):
        pos = self._manipulate(iterations=3)

        self.assertEqual(pos.noodle.part1, orientation.W)
        self.assertEqual(pos.noodle.part2, orientation.SW)
        self.assertEqual(pos.noodle.part3, orientation.NW)
        self.assertEqual(pos.noodle.part4, orientation.SW)

        pos = self._manipulate(iterations=3)

        self.assertEqual(pos.noodle.part1, orientation.E)
        self.assertEqual(pos.noodle.part2, orientation.NE)
        self.assertEqual(pos.noodle.part3, orientation.SE)
        self.assertEqual(pos.noodle.part4, orientation.NE)

        pos = self._manipulate(iterations=1)

        self.assertEqual(pos.noodle.part1, orientation.NW)
        self.assertEqual(pos.noodle.part2, orientation.NE)
        self.assertEqual(pos.noodle.part3, orientation.W)
        self.assertEqual(pos.noodle.part4, orientation.NE)

        pos = self._manipulate(iterations=6)

        self.assertEqual(pos.noodle.part1, orientation.SE)
        self.assertEqual(pos.noodle.part2, orientation.E)
        self.assertEqual(pos.noodle.part3, orientation.SW)
        self.assertEqual(pos.noodle.part4, orientation.E)

    def test_part_n_iterations(self):
        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.part, 0)

        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.part, 0)

        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.part, 1)

        pos = self._manipulate(iterations=42)
        self.assertEqual(pos.part, 4)

        pos = self._manipulate(iterations=1)
        self.assertEqual(pos.part, 0)

    def test_hole_n_iterations(self):
        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.hole, 0)

        pos = self._manipulate(iterations=54)
        self.assertEqual(pos.hole, 0)

        pos = self._manipulate(iterations=1)
        self.assertEqual(pos.hole, 1)

        pos = self._manipulate(iterations=60)
        self.assertEqual(pos.hole, 2)

        pos = self._manipulate(iterations=60)
        self.assertEqual(pos.hole, 3)

        pos = self._manipulate(iterations=60)
        self.assertEqual(pos.hole, 4)

        pos = self._manipulate(iterations=60)
        self.assertIsNone(pos)

    def test_symmetrical_noodle_n_iterations(self):
        self._create_manipulator(symmetrical=True)

        pos = self._manipulate(iterations=3)

        self.assertEqual(pos.noodle.part1, orientation.SW)
        self.assertEqual(pos.noodle.part2, orientation.NW)
        self.assertEqual(pos.noodle.part3, orientation.SW)
        self.assertEqual(pos.noodle.part4, orientation.NW)

        pos = self._manipulate(iterations=3)

        self.assertEqual(pos.noodle.part1, orientation.NE)
        self.assertEqual(pos.noodle.part2, orientation.SE)
        self.assertEqual(pos.noodle.part3, orientation.NE)
        self.assertEqual(pos.noodle.part4, orientation.SE)

        pos = self._manipulate(iterations=1)

        self.assertEqual(pos.noodle.part1, orientation.E)
        self.assertEqual(pos.noodle.part2, orientation.SW)
        self.assertEqual(pos.noodle.part3, orientation.E)
        self.assertEqual(pos.noodle.part4, orientation.SW)

    def test_symmetrical_part_n_iterations(self):
        self._create_manipulator(symmetrical=True)

        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.part, 0)

        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.part, 1)

        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.part, 2)

        pos = self._manipulate(iterations=12)
        self.assertEqual(pos.part, 4)

        pos = self._manipulate(iterations=1)
        self.assertEqual(pos.part, 0)

    def test_symmetrical_hole_n_iterations(self):
        self._create_manipulator(symmetrical=True)

        pos = self._manipulate(iterations=6)
        self.assertEqual(pos.hole, 0)

        pos = self._manipulate(iterations=24)
        self.assertEqual(pos.hole, 0)

        pos = self._manipulate(iterations=1)
        self.assertEqual(pos.hole, 1)

        pos = self._manipulate(iterations=30)
        self.assertEqual(pos.hole, 2)

        pos = self._manipulate(iterations=30)
        self.assertEqual(pos.hole, 3)

        pos = self._manipulate(iterations=30)
        self.assertEqual(pos.hole, 4)

        pos = self._manipulate(iterations=30)
        self.assertIsNone(pos)

    def _manipulate(self, iterations=1):
        for _ in range(iterations):
            pos = self._manipulator.manipulate([0, 1, 2, 3, 4])
        return pos
