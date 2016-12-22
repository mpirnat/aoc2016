#!/usr/bin/env python

import unittest
from day21 import parse, invert_instruction
from day21 import swap_char, swap_position, reverse, \
        rotate, rotate_position, rotate_position_inverse, move


class TestParsingInstructions(unittest.TestCase):

    cases = (
        ('swap position 4 with position 0', (swap_position, [4, 0])),
        ('swap letter d with letter b', (swap_char, ['d', 'b'])),
        ('reverse positions 0 through 4', (reverse, [0, 4])),
        ('rotate left 1 step', (rotate, [-1])),
        ('rotate right 1 step', (rotate, [1])),
        ('move position 1 to position 4', (move, [1, 4])),
        ('rotate based on position of letter b', (rotate_position, ['b'])),
    )

    def test_parses_instructions(self):
        for instruction, expected in self.cases:
            self.assertEqual(parse(instruction), expected)


class TestInvertingInstructions(unittest.TestCase):

    cases = (
        ((swap_position, [4, 0]), (swap_position, [0, 4])),
        ((swap_char, ['d', 'b']), (swap_char, ['b', 'd'])),
        ((reverse, [0, 4]), (reverse, [0, 4])),
        ((rotate, [1]), (rotate, [-1])),
        ((rotate, [-1]), (rotate, [1])),
        ((move, [1, 4]), (move, [4, 1])),
        ((rotate_position, ['b']), (rotate_position_inverse, ['b'])),
    )

    def test_inverts_instructions(self):
        for parsed, expected in self.cases:
            self.assertEqual(invert_instruction(*parsed), expected)


class TestManipulatingStrings(unittest.TestCase):

    cases = (
        ('abcde', swap_position, [4, 0], 'ebcda'),
        ('ebcda', swap_char, ['d', 'b'], 'edcba'),
        ('edcba', reverse, [0, 4], 'abcde'),
        ('abcde', rotate, [-1], 'bcdea'),
        ('bcdea', rotate, [1], 'abcde'),
        ('bcdea', move, [1, 4], 'bdeac'),
        ('bdeac', move, [3, 0], 'abdec'),
        ('abdec', rotate_position, ['b'], 'ecabd'),
        ('ecabd', rotate_position, ['d'], 'decab'),
    )

    def test_manipulates_strings(self):
        for string, f, args, expected in self.cases:
            self.assertEqual(f(string, *args), expected, [f.__name__, string, args])


if __name__ == '__main__':
    unittest.main()
