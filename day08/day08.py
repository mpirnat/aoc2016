#!/usr/bin/env python

"""
Solve day 8 of Advent of Code.

http://adventofcode.com/2016/day/8
"""

import copy

NUM_ROWS = 6
NUM_COLS = 50


class Screen:

    def __init__(self, rows, cols):
        self.data = []
        for i in range(rows):
            self.data.append([False] * cols)

    def do_command(self, command):
        function, args = self.parse_command(command)
        return function(*args)

    def parse_command(self, command):
        parts = command.split()

        if parts[0] == 'rect':
            return (self.rect, tuple([int(x) for x in parts[1].split('x')]))

        elif parts[1] == 'column':
            col = int(parts[2].split('=')[-1])
            by = int(parts[-1])
            return (self.rotate_column, (col, by))

        elif parts[1] == 'row':
            row = int(parts[2].split('=')[-1])
            by = int(parts[-1])
            return (self.rotate_row, (row, by))

    def rect(self, cols, rows):
        """
        rect AxB turns on all of the pixels in a rectangle at the top-left of the
        screen which is A wide and B tall.
        """
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] = True

    def rotate_row(self, row, by):
        """
        rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
        right by B pixels. Pixels that would fall off the right end appear at the
        left end of the row.
        """
        for i in range(by):
            self.data[row].insert(0, self.data[row].pop())

    def rotate_column(self, col, by):
        """
        rotate column x=A by B shifts all of the pixels in column A (0 is the left
        column) down by B pixels. Pixels that would fall off the bottom appear at
        the top of the column.
        """
        column = [row[col] for row in self.data]

        for i in range(by):
            column.insert(0, column.pop())

        for row in self.data:
            row[col] = column.pop(0)

    def count_lit_pixels(self):
        return sum(sum(x) for x in self.data)

    def display(self):
        print('\n'.join(''.join('#' if p else ' ' for p in row)
                for row in self.data))


if __name__ == '__main__':
    with open('input.txt') as f:
        screen = Screen(NUM_ROWS, NUM_COLS)
        for command in f:
            screen.do_command(command)
        print("Part 1:", screen.count_lit_pixels())
        print("Part 2:")
        screen.display()
