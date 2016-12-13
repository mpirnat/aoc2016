#!/usr/bin/env python

import unittest

from day13 import is_wall, navigate_maze


class TestCheckingForWalls(unittest.TestCase):

    expected = [
        ".#.####.##",
        "..#..#...#",
        "#....##...",
        "###.#.###.",
        ".##..#..#.",
        "..##....#.",
        "#...##.###",
    ]

    def test_finds_walls_and_spaces(self):
        modifier = 10
        for i in range(10):
            for j in range(7):
                self.assertEqual(
                        "#" if is_wall(i, j, modifier=modifier) else ".",
                        self.expected[j][i])

    def test_counts_steps(self):
        origin = (1, 1)
        goal = (7, 4)
        modifier = 10
        steps = navigate_maze(origin, goal, modifier=modifier)
        self.assertEqual(steps, 11)

    def test_counts_accessible_positions(self):
        origin = (1, 1)
        goal = (7, 4)
        modifier = 10
        positions = navigate_maze(origin, goal, modifier=modifier, max_steps=3)
        self.assertEqual(positions, 6)


if __name__ == '__main__':
    unittest.main()
