#!/usr/bin/env python

import unittest
from day01 import position_from_instructions
from day01 import distance_from_position


class TestFollowsInstructions(unittest.TestCase):
    cases = (
        # (instructions, e/w, n/s, dist)
        ("R2, L3", 2, 3, 5),
        ("R2, R2, R2", 0, -2, 2),
        ("R5, L5, R5, R3", 10, 2, 12),
    )

    def test_gets_position_from_instructions(self):
        for (instructions, x, y, dist) in self.cases:
            position, path = position_from_instructions(instructions)
            distance = distance_from_position(position)

            self.assertEqual(position[0], x)
            self.assertEqual(position[1], y)
            self.assertEqual(distance, dist)


if __name__ == '__main__':
    unittest.main()
