#!/usr/bin/env python

"""
Solve day 13 of Advent of Code.

http://adventofcode.com/2016/day/13
"""


def is_wall(x, y, modifier=0):
    """
    You can determine whether a given x,y coordinate will be a wall or an open space
    using a simple system:

        * Find x*x + 3*x + 2*x*y + y + y*y.
        * Add the office designer's favorite number (your puzzle input).
        * Find the binary representation of that sum; count the number of bits
          that are 1.
        * If the number of bits that are 1 is even, it's an open space.
        * If the number of bits that are 1 is odd, it's a wall.
    """
    value = x*x + 3*x + 2*x*y + y + y*y
    value += modifier
    bin_value = bin(value)[2:] # discard leading '0b' bytes indicator
    ones = bin_value.count('1')
    return ones % 2 == 1


def get_moves(x, y, visited, modifier=0):
    moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(x, y) for (x, y) in moves
            if x >= 0 and y >= 0
            and not is_wall(x, y, modifier=modifier)
            and (x, y) not in visited]


def navigate_maze(origin, goal, modifier=0, max_steps=None):
    result = None

    visited = {origin}
    new_positions = visited.copy()

    steps = 0

    while True:  # assumes there's actually a path...
        positions_to_check = new_positions.copy()
        new_positions = set()

        for x, y in positions_to_check:
            for new_x, new_y in get_moves(x, y, visited, modifier):
                visited.add((new_x, new_y))
                new_positions.add((new_x, new_y))
        steps += 1

        if goal in new_positions and not max_steps:
            result = steps
            break
        elif max_steps and steps == max_steps:
            result = len(visited)
            break

    return result


if __name__ == '__main__':
    origin = (1, 1)
    goal = (31, 39)
    modifier = 1352

    print("Part 1:", navigate_maze(origin, goal, modifier=modifier))
    print("Part 2:", navigate_maze(origin, goal, modifier=modifier,
        max_steps=50))
