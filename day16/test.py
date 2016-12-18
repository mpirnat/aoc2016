#!/usr/bin/env python

import unittest

from day16 import generate_data, generate_checksum


class TestGeneratingData(unittest.TestCase):

    def test_generates_data(self):
        cases = (
            ('1', '100'),
            ('0', '001'),
            ('11111', '11111000000'),
            ('111100001010', '1111000010100101011110000'),
        )
        for data, expected in cases:
            self.assertEqual(generate_data(data, len(data)+1), expected)

    def test_generates_at_least_minimum_data_needed(self):
        cases = (
            ('1', 10, '100011001001110'),
        )
        for data, disk_size, expected in cases:
            self.assertEqual(generate_data(data, disk_size), expected)


class TestGeneratingChecksums(unittest.TestCase):

    def test_generates_checksums(self):
        cases = (
            ('110010110100', 12, '100'),
        )
        for data, disk_size, expected in cases:
            self.assertEqual(generate_checksum(data, disk_size), expected)

    def test_doing_it_all(self):
        cases = (
            ('10000', 20, '01100'),
        )
        for data, disk_size, expected_checksum in cases:
            data = generate_data(data, disk_size)
            checksum = generate_checksum(data, disk_size)
            self.assertEqual(checksum, expected_checksum)


if __name__ == '__main__':
    unittest.main()
