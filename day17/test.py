#!/usr/bin/env python

import unittest
from day17 import open_doors, bfs

class TestFindsOpenDoorsFromHashAndPath(unittest.TestCase):

    cases = (
        ('hijkl', '', ['U', 'D', 'L']),
        ('hijkl', 'D', ['U', 'L', 'R']),
        ('hijkl', 'DU', ['R']),
        ('hijkl', 'DUR', []),
    )

    def test_finds_open_doors(self):
        for seed, path, expected in self.cases:
            self.assertEqual(open_doors(seed, path), expected)


class TestFindsShortestPath(unittest.TestCase):
    cases = (
        ('ihgpwlah', 'DDRRRD'),
        ('kglvqrro', 'DDUDRLRRUDRD'),
        ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'),
    )

    def test_finds_shortest_path(self):
        for seed, expected in self.cases:
            start = (0, 0)
            goal = (3, 3)
            paths = bfs(seed, start, goal)
            self.assertEqual(paths[0], expected)


class TestFindsLongestPath(unittest.TestCase):
    cases = (
        ('ihgpwlah', 370),
        ('kglvqrro', 492),
        ('ulqzkmiv', 830),
    )

    def test_finds_shortest_path(self):
        for seed, expected in self.cases:
            start = (0, 0)
            goal = (3, 3)
            paths = bfs(seed, start, goal)
            self.assertEqual(len(paths[-1]), expected)



if __name__ == '__main__':
    unittest.main()
