#!/usr/bin/env python

import unittest
from day08 import init_screen
from day08 import count_lit_pixels
from day08 import parse_command
from day08 import rect, rotate_column, rotate_row


class TestInitializingScreen(unittest.TestCase):

    def test_inits_screen(self):
        screen = init_screen(3, 5)
        self.assertEqual(len(screen), 3)
        self.assertEqual(len(screen[0]), 5)


class TestParsingCommands(unittest.TestCase):

    cases = (
        ('rect 3x2', (rect, (3, 2))),
        ('rotate column x=1 by 1', (rotate_column, (1, 1))),
        ('rotate row y=1 by 2', (rotate_row, (1, 2))),
    )

    def test_parses_commands(self):
        for command, expected in self.cases:
            self.assertEqual(parse_command(command), expected)


class TestManipulatingScreen(unittest.TestCase):

    def test_rect(self):
        screen = init_screen(3, 7)
        screen = rect(screen, 3, 2)
        self.assertEqual(screen,
                [[True, True, True, False, False, False, False],
                 [True, True, True, False, False, False, False],
                 [False]*7])

    def test_rotate_column(self):
        screen = init_screen(3, 7)
        screen = rect(screen, 3, 2)
        screen = rotate_column(screen, 1, 2)
        self.assertEqual(screen,
                [[True, True, True, False, False, False, False],
                 [True, False, True, False, False, False, False],
                 [False, True, False, False, False, False, False]])

    def test_rotate_row(self):
        screen = init_screen(3, 7)
        screen = rect(screen, 3, 2)
        screen = rotate_row(screen, 1, 1)
        self.assertEqual(screen,
                [[True, True, True, False, False, False, False],
                 [False, True, True, True, False, False, False],
                 [False]*7])

    def test_example_input(self):
        screen = init_screen(3, 7)
        screen = rect(screen, 3, 2)
        screen = rotate_column(screen, 1, 1)
        screen = rotate_row(screen, 0, 4)
        screen = rotate_column(screen, 1, 1)
        self.assertEqual(screen,
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
        for screen, expected in self.cases:
            self.assertEqual(count_lit_pixels(screen), expected)


if __name__ == '__main__':
    unittest.main()
