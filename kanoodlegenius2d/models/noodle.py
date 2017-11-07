from peewee import (CharField,
                    FixedCharField)

from .base import BaseModel


class Noodle(BaseModel):
    """Represents a noodle - a puzzle piece."""
    name = CharField()

    # The orientations of each part (excluding the root), relative to one another
    part1 = FixedCharField(max_length=2)
    part2 = FixedCharField(max_length=2)
    part3 = FixedCharField(max_length=2)
    part4 = FixedCharField(max_length=2)
    part5 = FixedCharField(max_length=2)
    part6 = FixedCharField(max_length=2)
