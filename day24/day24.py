#!/usr/bin/env python

"""
Solve day 24 of Advent of Code.

http://adventofcode.com/2016/day/24
"""

from collections import deque
from itertools import permutations


def make_grid(data):
    grid = [list(line) for line in data]
    return grid


def find_goals(grid):
    goals = {}

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isdigit():
                goals[int(grid[row][col])] = (row, col)

    return goals


def measure_segments(grid, goals):
    segments = {}
    goal_positions = goals.values()
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for goal_id, position in goals.items():
        queue = deque([[position]])
        visited = set(position)

        while queue:
            path = queue.popleft()
            row, col = path[-1]

            # Found a path from one goal to another
            if (row, col) in goal_positions and len(path) > 1 and \
                    goal_id != int(grid[row][col]):
                segments[(goal_id, int(grid[row][col]))] = len(path) - 1
                #continue

            for d_row, d_col in moves:
                if can_move(grid, row + d_row, col + d_col) and \
                        (row + d_row, col + d_col) not in visited:
                    queue.append(path + [(row + d_row, col + d_col)])
                    visited.add((row + d_row, col + d_col))

    return segments


def can_move(grid, row, col):
    return 0 <= row < len(grid) and \
            0 <= col < len(grid[0]) and \
            grid[row][col] in '.01234567'


def shortest_path(segments, start_at=0, return_to=None):
    num_goals = sorted(segments.keys())[-1][0] + 1
    distances = []

    for path in permutations(range(1, num_goals)):
        path = (start_at,) + path + (return_to,)

        steps = 0
        for i in range(len(path) - 2):
            steps += segments[(path[i], path[i+1])]

        if return_to is not None:
            steps += segments[(path[-2], path[-1])]

        distances.append(steps)

    return min(distances)

"""
print('Part1:', min(distances1))
print('Part2:', min(distances2))
"""


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = make_grid(f.read().splitlines())
        goals = find_goals(grid)
        segments = measure_segments(grid, goals)

        print("Part 1:", shortest_path(segments))
        print("Part 2:", shortest_path(segments, return_to=0))
