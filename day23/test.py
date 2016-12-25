#!/usr/bin/env python

import unittest
from day23 import run_code


class TestRunningCode(unittest.TestCase):

    code = ['cpy 2 a', 'tgl a', 'tgl a', 'tgl a', 'cpy 1 a', 'dec a', 'dec a']

    def test_runs_code(self):
        registers = run_code(self.code)
        self.assertEqual(registers['a'], 3)



if __name__ == '__main__':
    unittest.main()
