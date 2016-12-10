#!/usr/bin/env python

import unittest

from day10 import BotWrangler


class TestBots(unittest.TestCase):

    instructions = [x.strip() for x in
            """value 5 goes to bot 2
            bot 2 gives low to bot 1 and high to bot 0
            value 3 goes to bot 1
            bot 1 gives low to output 1 and high to bot 0
            bot 0 gives low to output 2 and high to output 0
            value 2 goes to bot 2""".splitlines()]

    def setUp(self):
        self.bw = BotWrangler(self.instructions)

    def test_outputs_have_expected_values(self):
        self.bw.process_bot_queues()
        outs = self.bw.outs

        self.assertEqual(outs[0][0], 5)
        self.assertEqual(outs[1][0], 2)
        self.assertEqual(outs[2][0], 3)

    def test_finds_bot_that_compares_specific_values(self):
        sought_bot = self.bw.process_bot_queues(seeking=(2,5))
        self.assertEqual(sought_bot, 2)

    def test_multiplies_specified_output_values(self):
        self.bw.process_bot_queues()

        self.assertEqual(self.bw.multiply_output_values(0, 1), 10)
        self.assertEqual(self.bw.multiply_output_values(1, 2), 6)
        self.assertEqual(self.bw.multiply_output_values(0, 2), 15)
        self.assertEqual(self.bw.multiply_output_values(0, 1, 2), 30)


if __name__ == '__main__':
    unittest.main()
