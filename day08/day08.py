#!/usr/bin/env python

"""
Solve day 8 of Advent of Code.

http://adventofcode.com/2016/day/8
"""

import copy

NUM_ROWS = 6
NUM_COLS = 50


def init_screen(num_rows, num_cols):
    screen = []
    for i in range(num_rows):
        screen.append([False] * num_cols)
    return screen


def do_command(command, screen):
    #print('\n', command)
    function, args = parse_command(command)
    screen = function(screen, *args)
    #display(screen)
    #print("Lit: ", count_lit_pixels(screen))
    #input('')
    return screen


def parse_command(command):
    parts = command.split()

    if parts[0] == 'rect':
        return (rect, tuple([int(x) for x in parts[1].split('x')]))

    elif parts[1] == 'column':
        col = int(parts[2].split('=')[-1])
        by = int(parts[-1])
        return (rotate_column, (col, by))

    elif parts[1] == 'row':
        row = int(parts[2].split('=')[-1])
        by = int(parts[-1])
        return (rotate_row, (row, by))


def rect(screen, cols, rows):
    """
    rect AxB turns on all of the pixels in a rectangle at the top-left of the
    screen which is A wide and B tall.
    """
    for i in range(rows):
        for j in range(cols):
            screen[i][j] = True

    return screen


def rotate_row(screen, row, by):
    """
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
    right by B pixels. Pixels that would fall off the right end appear at the
    left end of the row.
    """
    for i in range(by):
        screen[row].insert(0, screen[row].pop())

    return screen


def rotate_column(screen, col, by):
    """
    rotate column x=A by B shifts all of the pixels in column A (0 is the left
    column) down by B pixels. Pixels that would fall off the bottom appear at
    the top of the column.
    """
    column = [row[col] for row in screen]

    for i in range(by):
        column.insert(0, column.pop())

    for row in screen:
        row[col] = column.pop(0)

    return screen


def count_lit_pixels(screen):
    return sum(sum(x) for x in screen)


def display(screen):
    print('\n'.join(''.join('#' if p else ' '  for p in row) for row in screen))


if __name__ == '__main__':
    with open('input.txt') as f:
        screen = init_screen(NUM_ROWS, NUM_COLS)
        for command in f:
            screen = do_command(command, screen)
        print("Part 1:", count_lit_pixels(screen))
        print("Part 2:")
        display(screen)
