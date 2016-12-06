#!/usr/bin/env python

import unittest
from day06 import decode_most_common, decode_least_common

class TestDecodingMessages(unittest.TestCase):

    data = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]

    def test_decodes_using_most_common_chars(self):
        decoded = decode_most_common(self.data)
        self.assertEqual(decoded, 'easter')

    def test_decodes_using_least_common_chars(self):
        decoded = decode_least_common(self.data)
        self.assertEqual(decoded, 'advent')


if __name__ == '__main__':
    unittest.main()
