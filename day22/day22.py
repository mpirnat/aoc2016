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

    for line in df.splitlines():
        items = df_regex.findall(line)
        if not items:
            continue

        #[('node-x0-y0', '0', '0', '87', '71', '16', '81')]
        items = [int(x) if x.isdigit() else x for x in items[0]]
        name, x, y, size, used, avail, percent = items

        if y > len(grid)-1:
            grid.append([])

        grid[y].append(Node(name=name, size=size, used=used, avail=avail))

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


def print_grid(grid):
    s = ''
    for i, row in enumerate(grid):
        for j, node in enumerate(row):
            if i == 0 and j == 0:
                s += 'O'
            elif node.size > 400:
                s += '#'
            elif node.used == 0:
                s += '_'
            elif i == 0 and j == len(grid[0]) -1:
                s += 'G'
            else:
                s += '.'
        else:
            s += '\n'
    print(s)


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = make_nodes(f.read())
        pairs = viable_nodes(grid)
        print("Part 1:", len(pairs))

        print("Part 2: here's a map, go count steps")
        print_grid(grid)
