#!/usr/bin/env python

import unittest

from day12 import run_code


class TestRunningCode(unittest.TestCase):

    code = ["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"]

    def test_runs_code(self):
        registers = run_code(self.code)
        self.assertEqual(registers['a'], 42)


if __name__ == '__main__':
    unittest.main()
