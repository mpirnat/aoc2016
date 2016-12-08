#!/usr/bin/env python

import unittest
from day08 import Screen


class TestInitializingScreen(unittest.TestCase):

    def test_inits_screen(self):
        screen = Screen(3, 5)
        self.assertEqual(len(screen.data), 3)
        self.assertEqual(len(screen.data[0]), 5)


class TestParsingCommands(unittest.TestCase):

    cases = (
        ('rect 3x2', ('rect', (3, 2))),
        ('rotate column x=1 by 1', ('rotate_column', (1, 1))),
        ('rotate row y=1 by 2', ('rotate_row', (1, 2))),
    )

    def test_parses_commands(self):
        screen = Screen(3, 5)
        for command, expected in self.cases:
            parsed = screen.parse_command(command)
            self.assertEqual(parsed[0].__name__, expected[0])
            self.assertEqual(parsed[1], expected[1])


class TestManipulatingScreen(unittest.TestCase):

    def test_rect(self):
        screen = Screen(3, 7)
        screen.rect(3, 2)
        self.assertEqual(screen.data,
                [[True, True, True, False, False, False, False],
                 [True, True, True, False, False, False, False],
                 [False]*7])

    def test_rotate_column(self):
        screen = Screen(3, 7)
        screen.rect(3, 2)
        screen.rotate_column(1, 2)
        self.assertEqual(screen.data,
                [[True, True, True, False, False, False, False],
                 [True, False, True, False, False, False, False],
                 [False, True, False, False, False, False, False]])

    def test_rotate_row(self):
        screen = Screen(3, 7)
        screen.rect(3, 2)
        screen.rotate_row(1, 1)
        self.assertEqual(screen.data,
                [[True, True, True, False, False, False, False],
                 [False, True, True, True, False, False, False],
                 [False]*7])

    def test_example_input(self):
        screen = Screen(3, 7)
        screen.rect(3, 2)
        screen.rotate_column(1, 1)
        screen.rotate_row(0, 4)
        screen.rotate_column(1, 1)
        self.assertEqual(screen.data,
                [[False, True, False, False, True, False, True],
                 [True, False, True, False, False, False, False],
                 [False, True, False, False, False, False, False]])


class TestCountingLitPixels(unittest.TestCase):
    cases = (
        ([[False, False, False], [False, False, False]], 0),
        ([[True, False, False], [False, False, True]], 2),
        ([[True, True, True], [True, True, True]], 6),
    )

    def test_counts_lit_pixels(self):
        for data, expected in self.cases:
            screen = Screen(3,2)
            screen.data = data
            self.assertEqual(screen.count_lit_pixels(), expected)


if __name__ == '__main__':
    unittest.main()
