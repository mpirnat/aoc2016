#!/usr/bin/env python

"""
Solve day 22 of Advent of Code.

http://adventofcode.com/2016/day/22
"""

import itertools
import re
from collections import namedtuple

Node = namedtuple('Node', ['name', 'size', 'used', 'avail'])

df_regex = re.compile(r'(node-x(\d+)-y(\d+))\s+'
        '(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')


def make_nodes(df):
    grid = [[]]
    row_num = 0

    for line in df.splitlines():
        items = df_regex.findall(line)
        if not items:
            continue

        #[('node-x0-y0', '0', '0', '87', '71', '16', '81')]
        items = [int(x) if x.isdigit() else x for x in items[0]]
        name, x, y, size, used, avail, percent = items


        if x > row_num:
            grid.append([])
            row_num = x

        grid[-1].append(Node(name=name, size=size, used=used, avail=avail))

    return grid


def viable_nodes(grid):
    pairs = set()

    nodes = list(itertools.chain(*grid))

    for node in nodes:
        for other_node in nodes:
            if node == other_node \
                    or not node.used \
                    or other_node.avail < node.used:
                continue
            pairs.add((node, other_node))

    return pairs


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = make_nodes(f.read())
        pairs = viable_nodes(grid)
        print("Part 1:", len(pairs))

