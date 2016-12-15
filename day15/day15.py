#!/usr/bin/env python

"""
Solve day 15 of Advent of Code.

http://adventofcode.com/2016/day/15
"""

import re
from collections import namedtuple


Disc = namedtuple('Disc', ['name', 'num_pos', 'start_pos'])


def discs_from_input(data):
    discs = []
    for line in data:
        match = re.match(r'.+ #(?P<name>\d+) .+ (?P<num_pos>\d+) positions; '
                '.+ position (?P<start_pos>\d+).', line)
        discs.append(Disc(
                name=int(match.group('name')),
                num_pos=int(match.group('num_pos')),
                start_pos=int(match.group('start_pos'))))
    return sorted(discs)


def pos_at_time(disc, t):
    return (t + disc.start_pos) % disc.num_pos


def find_goal_state(discs):
    return [-disc.name % disc.num_pos for disc in discs]


def find_time_to_push(discs):
    goal = find_goal_state(discs)
    t = 0

    while True:
        positions = [pos_at_time(disc, t) for disc in discs]
        if positions == goal:
            break
        t += 1
    return t


if __name__ == '__main__':
    with open('input.txt') as f:
        discs = discs_from_input(f)
        print("Part 1:", find_time_to_push(discs))
