#!/usr/bin/env python

"""
Solve day 17 of Advent of Code.

http://adventofcode.com/2016/day/17
"""

from collections import deque
from hashlib import md5


DIRECTIONS = 'UDLR'

MOVES = {
    'U': lambda x, y: (x, y - 1),
    'D': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y),
}


def open_doors(seed, path):
    hashed = md5((seed+path).encode('utf8')).hexdigest()[:4]
    open_doors = [DIRECTIONS[i] for i, x in enumerate(hashed) if x in 'bcdef']
    return open_doors


def bfs(seed, start, goal):
    all_paths = []
    queue = deque()
    queue.append((start, [start], ''))

    while queue:
        # Let's explore the next location in our queue...
        (x, y), path, directions = queue.popleft()

        for direction in open_doors(seed, directions):
            # Figure out the next position for the given move
            next_x, next_y = MOVES[direction](x, y)

            # Reject moves that would go out of bounds
            if not (0 <= next_x <= 3 and 0 <= next_y <= 3):
                continue

            # Found a path to the goal
            elif (next_x, next_y) == goal:
                all_paths.append(directions + direction)

            # Add the next position to the queue of locations to explore
            else:
                queue.append((
                    (next_x, next_y),
                    path + [(next_x, next_y)],
                    directions + direction))

    return all_paths


if __name__ == '__main__':
    seed = 'dmypynyp'
    start = (0, 0)
    goal = (3, 3)
    all_paths = bfs(seed, start, goal)

    print("Part 1:", all_paths[0])
    print("Part 2:", len(all_paths[-1]))
