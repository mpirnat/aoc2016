#!/usr/bin/env python

import unittest
from day03 import is_possible_triangle, parse_line
from day03 import count_possible_triangles_in_rows
from day03 import count_possible_triangles_in_columns


class TestParsesInput(unittest.TestCase):

    cases = (
        ("    4   21  894", [4, 21, 894]),
    )

    def test_parses_input(self):
        for line, expected in self.cases:
            data = parse_line(line)
            self.assertEqual(data, expected)


class TestDetectsPossibleTriangles(unittest.TestCase):

    cases = (
        (5, 10, 25, False),
        (10, 10, 10, True),
    )

    def test_detects_possible_triangles(self):
        for *sides, expected in self.cases:
            is_possible = is_possible_triangle(*sides)
            self.assertEqual(is_possible, expected)


class TestCountsPossibleTriangles(unittest.TestCase):

    cases = (
        (["    4   21  894", "  419  794  987", "  424  797  125"], 1, 2),
    )

    def test_counts_possible_triangles_in_rows(self):
        for f, expected, junk in self.cases:
            count = count_possible_triangles_in_rows(f)
            self.assertEqual(count, expected)

    def test_counts_possible_triangles_in_columns(self):
        for f, junk, expected in self.cases:
            count = count_possible_triangles_in_columns(f)
            self.assertEqual(count, expected)


if __name__ == '__main__':
    unittest.main()
