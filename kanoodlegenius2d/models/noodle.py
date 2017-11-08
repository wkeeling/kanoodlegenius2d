from peewee import (CharField,
                    FixedCharField)

from .base import BaseModel


class Noodle(BaseModel):
    """Represents a noodle - a puzzle piece."""
    designation = FixedCharField(max_length=1)
    code = CharField()

    # The default orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)

    def rotate(self, increment=1):
        """Rotate the noodle clockwise by the specified number of increments.

        Args:
            increment:
                The number of increments to rotate the noodle by.
        """
