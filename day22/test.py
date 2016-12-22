#!/usr/bin/env python

import unittest
from day22 import Node, make_nodes, viable_nodes


class TestMakingNodes(unittest.TestCase):

    def test_makes_nodes_from_input(self):
        df = """
        /dev/grid/node-x0-y0     87T   71T    16T   81%
        /dev/grid/node-x0-y1     93T   72T    21T   77%
        /dev/grid/node-x1-y0     86T   66T    20T   76%
        /dev/grid/node-x1-y1     93T   64T    29T   68%
        """

        nodes = make_nodes(df)
        self.assertEqual(nodes, [
            [Node(name='node-x0-y0', size=87, used=71, avail=16),
             Node(name='node-x1-y0', size=86, used=66, avail=20)],
            [Node(name='node-x0-y1', size=93, used=72, avail=21),
             Node(name='node-x1-y1', size=93, used=64, avail=29)]])


class TestFindingViableNodes(unittest.TestCase):

    grid = [
            [Node(name='A', size=100, used=1, avail=99),
             Node(name='B', size=100, used=50, avail=50)],
            [Node(name='C', size=100, used=0, avail=100),
             Node(name='D', size=100, used=100, avail=0)],
            [Node(name='E', size=50, used=10, avail=40),
             Node(name='F', size=100, used=60, avail=40)]]

    def test_finds_viable_nodes(self):
        grid = self.grid
        nodes = viable_nodes(grid)
        self.assertEqual(nodes, {
            (grid[0][0], grid[0][1]),
            (grid[0][0], grid[1][0]),
            (grid[0][0], grid[2][0]),
            (grid[0][0], grid[2][1]),
            (grid[0][1], grid[0][0]),
            (grid[0][1], grid[1][0]),
            (grid[1][1], grid[1][0]),
            (grid[2][0], grid[0][0]),
            (grid[2][0], grid[0][1]),
            (grid[2][0], grid[1][0]),
            (grid[2][0], grid[2][1]),
            (grid[2][1], grid[0][0]),
            (grid[2][1], grid[1][0])})


if __name__ == '__main__':
    unittest.main()
