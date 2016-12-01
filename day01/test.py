#!/usr/bin/env python

import unittest
from day01 import position_from_instructions
from day01 import distance_from_origin


class TestFollowsInstructions(unittest.TestCase):
    cases = (
        # (instructions, dx, dy, dist)
        ("R2, L3", 2, 3, 5),
        ("R2, R2, R2", 0, -2, 2),
        ("R5, L5, R5, R3", 10, 2, 12),
    )

    def test_gets_position_from_instructions(self):
        for (instructions, dx, dy, dist) in self.cases:
            position = position_from_instructions(instructions)
            distance = distance_from_origin(position)

            self.assertEqual(position[0], dx)
            self.assertEqual(position[1], dy)
            self.assertEqual(distance, dist)

    def test_gets_path_from_instructions(self):
        for (instructions, dx, dy, dist) in self.cases:
            path = [(0, 0)]
            position = position_from_instructions(instructions, path)

            self.assertEqual(path, [
                (0,0), (1,0), (2,0),
                (2,1), (2,2), (2,3)
            ])
            break


if __name__ == '__main__':
    unittest.main()
