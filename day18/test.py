#!/usr/bin/env python

import unittest

from day18 import next_row, count_safe_tiles


class TestMakingNextRow(unittest.TestCase):

    cases = (
        ('..^^.', '.^^^^'),
        ('.^^^^', '^^..^'),
        ('.^^.^.^^^^', '^^^...^..^'),
        ('^^^...^..^', '^.^^.^.^^.'),
        ('^.^^.^.^^.', '..^^...^^^'),
        ('..^^...^^^', '.^^^^.^^.^'),
        ('.^^^^.^^.^', '^^..^.^^..'),
        ('^^..^.^^..', '^^^^..^^^.'),
        ('^^^^..^^^.', '^..^^^^.^^'),
        ('^..^^^^.^^', '.^^^..^.^^'),
        ('.^^^..^.^^', '^^.^^^..^^'),
    )

    def test_makes_next_row(self):
        for row, expected in self.cases:
            self.assertEqual(next_row(row), expected)


class TestCountingSafeTiles(unittest.TestCase):

    cases = (
        ('..^^.', 3, 6),
        ('.^^.^.^^^^', 10, 38),
    )

    def test_counts_safe_tiles(self):
        for first_row, total_rows, expected in self.cases:
            self.assertEqual(count_safe_tiles(first_row, total_rows), expected)


if __name__ == '__main__':
    unittest.main()
