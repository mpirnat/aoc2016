#!/usr/bin/env python

import unittest
from day14 import find_keys


class TestFindingKeys(unittest.TestCase):

    def test_finds_keys(self):
        salt = 'abc'
        keys = find_keys(salt, max_keys=64)
        self.assertEqual(keys[0][0], 39)
        self.assertEqual(keys[1][0], 92)
        self.assertEqual(keys[63][0], 22728, keys)

    def test_finds_stretched_keys(self):
        salt = 'abc'
        keys = find_keys(salt, max_keys=64, stretch=2016)
        self.assertEqual(keys[0][0], 10)
        self.assertEqual(keys[63][0], 22551, keys)


if __name__ == '__main__':
    unittest.main()
