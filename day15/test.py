#!/usr/bin/env python

import unittest
from day15 import Disc, discs_from_input, pos_at_time, find_goal_state, \
        find_time_to_push


class TestSolvingDay15(unittest.TestCase):

    test_input = ["Disc #1 has 5 positions; at time=0, it is at position 4.",
            "Disc #2 has 2 positions; at time=0, it is at position 1."]

    def setUp(self):
        self.discs = discs_from_input(self.test_input)

    def test_parses_input_into_discs(self):
        self.assertEqual(len(self.discs), 2)
        self.assertEqual(self.discs[0].name, 1)
        self.assertEqual(self.discs[0].num_pos, 5)
        self.assertEqual(self.discs[0].start_pos, 4)
        self.assertEqual(self.discs[1].name, 2)
        self.assertEqual(self.discs[1].num_pos, 2)
        self.assertEqual(self.discs[1].start_pos, 1)

    def test_gets_position_at_time(self):
        cases = ((0, 4, 1), (1, 0, 0), (2, 1, 1), (3, 2, 0), (4, 3, 1),
                (5, 4, 0), (6, 0, 1))
        for t, pos1, pos2 in cases:
            self.assertEqual(pos_at_time(self.discs[0], t), pos1)
            self.assertEqual(pos_at_time(self.discs[1], t), pos2)

    def test_finds_goal_state(self):
        goal = find_goal_state(self.discs)
        self.assertEqual(goal, [4, 0])

    def test_finds_time_to_release_capsule(self):
        t_push = find_time_to_push(self.discs)
        self.assertEqual(t_push, 5)




if __name__ == '__main__':
    unittest.main()
