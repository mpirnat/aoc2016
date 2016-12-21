#!/usr/bin/env python

import unittest

from day20 import sorted_ranges, first_open_address, count_open_addresses


class TestProcessingBlacklist(unittest.TestCase):

    data = "5-8\n0-2\n4-7"

    def test_processes_and_sorts_input_data(self):
        ranges = sorted_ranges(self.data.splitlines())
        self.assertEqual(ranges, [(0, 2), (4, 7), (5, 8)])

    def test_finds_first_open_address(self):
        ranges = sorted_ranges(self.data.splitlines())
        self.assertEqual(first_open_address(ranges), 3)

    def test_counts_all_open_addresses(self):
        ranges = sorted_ranges(self.data.splitlines())
        self.assertEqual(count_open_addresses(ranges, end=9), 2)


if __name__ == '__main__':
    unittest.main()
