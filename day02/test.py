#!/usr/bin/env python

import unittest
from day02 import get_next_button, part1_buttons, part2_buttons


class TestFollowsInstructionsForPart1(unittest.TestCase):
    buttons = part1_buttons

    cases = (
        ("5", "ULL", "1"),
        ("1", "RRDDD", "9"),
        ("9", "LURDL", "8"),
        ("8", "UUUUD", "5"),
    )

    def test_gets_next_button(self):
        for start, instructions, expected in self.cases:
            next_button = get_next_button(start, self.buttons, instructions)
            self.assertEqual(next_button, expected)


class TestFollowsInstructionsForPart2(TestFollowsInstructionsForPart1):
    buttons = part2_buttons

    cases = (
        ("5", "ULL", "5"),
        ("5", "RRDDD", "D"),
        ("D", "LURDL", "B"),
        ("B", "UUUUD", "3"),
    )


if __name__ == '__main__':
    unittest.main()
