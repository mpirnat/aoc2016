#!/usr/bin/env python

import unittest
from day24 import make_grid, find_goals, measure_segments, can_move, shortest_path


class TestManipulatingGrid(unittest.TestCase):

    data = ["###########",
            "#0.1.....2#",
            "#.#######.#",
            "#4.......3#",
            "###########"]

    def setUp(self):
        self.grid = make_grid(self.data)

    def test_makes_grid(self):
        grid = self.grid
        self.assertEqual(self.grid[0][0], '#')
        self.assertEqual(self.grid[1][1], '0')
        self.assertEqual(self.grid[1][2], '.')

    def test_finds_goals(self):
        goals = find_goals(self.grid)
        self.assertEqual(goals, {
            0: (1, 1),
            1: (1, 3),
            2: (1, 9),
            3: (3, 9),
            4: (3, 1),
        })

    def test_checks_positions(self):
        self.assertEqual(can_move(self.grid, 0, 0), False)
        self.assertEqual(can_move(self.grid, 1, 1), True)
        self.assertEqual(can_move(self.grid, 1, 2), True)

    def test_finds_distances_between_goals(self):
        goals = find_goals(self.grid)
        segments = measure_segments(self.grid, goals)
        self.assertEqual(segments, {
            (0, 1): 2,
            (0, 2): 8,
            (0, 3): 10,
            (0, 4): 2,
            (1, 0): 2,
            (1, 2): 6,
            (1, 3): 8,
            (1, 4): 4,
            (2, 0): 8,
            (2, 1): 6,
            (2, 3): 2,
            (2, 4): 10,
            (3, 0): 10,
            (3, 1): 8,
            (3, 2): 2,
            (3, 4): 8,
            (4, 0): 2,
            (4, 1): 4,
            (4, 2): 10,
            (4, 3): 8,
        })

    def test_finds_length_of_shortest_path_to_all_goals(self):
        goals = find_goals(self.grid)
        segments = measure_segments(self.grid, goals)
        steps = shortest_path(segments)
        self.assertEqual(steps, 14)

    def test_finds_length_of_shortest_path_plus_return(self):
        goals = find_goals(self.grid)
        segments = measure_segments(self.grid, goals)
        steps = shortest_path(segments, return_to=0)
        self.assertEqual(steps, 20)


if __name__ == '__main__':
    unittest.main()
