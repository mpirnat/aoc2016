#!/usr/bin/env python

import unittest
from day07 import has_abba, get_abba_allowed_strings, get_abba_disallowed_strings
from day07 import supports_tls, count_tls_addresses
from day07 import find_abas, supports_ssl, count_ssl_addresses


class TestFindingABBASequences(unittest.TestCase):
    cases = (
        ('abba', True),
        ('oxyyxo', True),
        ('aaaa', False),
        ('abcd', False),
    )

    def test_finds_abba_sequences(self):
        for text, expected in self.cases:
            self.assertEqual(has_abba(text), expected)


class TestGettingAllowedChunks(unittest.TestCase):
    cases = (
        ('abba[mnop]qrst[abcd]defg', ['abba', 'qrst', 'defg']),
    )

    def test_finds_allowed_substrings(self):
        for text, expected in self.cases:
            self.assertEqual(get_abba_allowed_strings(text), expected)


class TestGettingDisallowedChunks(unittest.TestCase):
    cases = (
        ('abba[mnop]qrst[abcd]defg', ['mnop', 'abcd']),
    )

    def test_finds_disallowed_substrings(self):
        for text, expected in self.cases:
            self.assertEqual(get_abba_disallowed_strings(text), expected)


class TestCheckingTLSAddresses(unittest.TestCase):
    cases = (
        ('abba[mnop]qrst', True),
        ('abcd[bddb]xyyx', False),
        ('aaaa[qwer]tyui', False),
        ('ioxxoj[asdfgh]zxcvbn', True),
    )

    def test_finds_tls_addresses(self):
        for text, expected in self.cases:
            self.assertEqual(supports_tls(text), expected)

    def test_counts_tls_addresses(self):
        data = [x[0] for x in self.cases]
        self.assertEqual(count_tls_addresses(data), 2)


class TestFindingABASequences(unittest.TestCase):
    cases = (
        ('aba', ['aba']),
        ('xyxxyx', ['xyx']),
        ('aaakekeke', ['eke', 'kek']),
        ('zazbzbzbcdb', ['bzb', 'zaz', 'zbz']),
    )

    def test_finds_aba_sequences(self):
        for text, expected in self.cases:
            self.assertEqual(find_abas(text), expected)


class TestCheckingSSLAddresses(unittest.TestCase):
    cases = (
        ('aba[bab]xyz', True),
        ('xyx[xyx]xyx', False),
        ('aaa[kek]eke', True),
        ('zazbz[bzb]cdb', True),
    )

    def test_finds_ssl_addresses(self):
        for text, expected in self.cases:
            self.assertEqual(supports_ssl(text), expected)

    def test_counts_ssl_addresses(self):
        data = [x[0] for x in self.cases]
        self.assertEqual(count_ssl_addresses(data), 3)


if __name__ == '__main__':
    unittest.main()
