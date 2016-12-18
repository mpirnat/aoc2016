#!/usr/bin/env python

"""
Solve day 18 of Advent of Code.

http://adventofcode.com/2016/day/18

Another one where I could probably optimize part 2, but it would take longer
than just running this naïve implementation.
"""

SAFE = '.'
TRAP = '^'


def next_row(row):
    new_row = ''
    num_tiles = len(row)

    for i in range(num_tiles):
        left = row[i-1] if i != 0 else SAFE
        right = row[i+1] if i < num_tiles-1 else SAFE
        new_row += SAFE if left == right else TRAP

    return new_row


def count_safe_tiles(row, total_rows):
    safe_tiles = 0
    for i in range(total_rows):
        safe_tiles += row.count(SAFE)
        row = next_row(row)
    return safe_tiles


if __name__ == '__main__':
    with open('input.txt') as f:
        num_rows = 40
        first_row = f.read().strip()
        print("Part 1:", count_safe_tiles(first_row, num_rows))

        num_rows = 400000
        print("Part 2:", count_safe_tiles(first_row, num_rows))

