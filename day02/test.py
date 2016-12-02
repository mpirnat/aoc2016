#!/usr/bin/env python

import unittest
from day02 import get_next_button


class TestFollowsInstructions(unittest.TestCase):
    cases = (
        ("5", "ULL", "1"),
        ("1", "RRDDD", "9"),
        ("9", "LURDL", "8"),
        ("8", "UUUUD", "5"),
    )

    def test_gets_next_button(self):
        for start, instructions, expected in self.cases:
            next_button = get_next_button(start, instructions)
            self.assertEqual(next_button, expected)


if __name__ == '__main__':
    unittest.main()
