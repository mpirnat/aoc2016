#!/usr/bin/env python

"""
Solve day 18 of Advent of Code.

http://adventofcode.com/2016/day/18

Another one where I could probably optimize part 2, but it would take longer
than just running the naïve implementation.
"""

SAFE = '.'
TRAP = '^'

def next_row(row):
    new_row = ''
    num_tiles = len(row)
    for i in range(num_tiles):
        center = row[i]
        left = row[i-1] if i != 0 else SAFE
        right = row[i+1] if i < num_tiles-1 else SAFE

        rules = {
            (TRAP, TRAP, SAFE): TRAP,
            (SAFE, TRAP, TRAP): TRAP,
            (TRAP, SAFE, SAFE): TRAP,
            (SAFE, SAFE, TRAP): TRAP,
        }

        new_row += rules.get((left, center, right), SAFE)

    return new_row


def count_safe_tiles(row, total_rows):
    safe_tiles = row.count(SAFE)
    for i in range(total_rows - 1):
        new_row = next_row(row)
        safe_tiles += new_row.count(SAFE)
        row = new_row
    return safe_tiles


if __name__ == '__main__':
    with open('input.txt') as f:
        num_rows = 40
        first_row = f.read().strip()
        print("Part 1:", count_safe_tiles(first_row, num_rows))

        num_rows = 400000
        print("Part 2:", count_safe_tiles(first_row, num_rows))

