#!/usr/bin/env python

"""
Solve day 10 of Advent of Code.

http://adventofcode.com/2016/day/10
"""

import re
from collections import defaultdict


class BotWrangler:

    def __init__(self, instructions):
        # Queue values going into bots and outputs;
        # each bot and each output gets a queue dynamically allocated for it
        # as it is encountered in the instructions.
        self.bots = defaultdict(list)
        self.outs = defaultdict(list)

        # Build the graph of bots and outputs
        self.graph = self.process_instructions(instructions)

    def process_instructions(self, instructions):
        graph = {}

        for line in instructions:

            if line.startswith('bot'):
                # Create a mapping of source bot to destination;
                # destination may be a bot with a number,
                # or it may be an output with a number.
                source, low_dest, high_dest = map(int, re.findall('\d+', line))
                low_dest_type, high_dest_type = re.findall(' (bot|output)', line)
                graph[source] = (low_dest_type, low_dest), \
                        (high_dest_type, high_dest)

            elif line.startswith('value'):
                # Put a value into the input queue for a given bot
                value, bot = map(int, re.findall('\d+', line))
                self.bots[bot].append(value)

        return graph

    def process_bot_queues(self, seeking=None):
        sought_bot = None

        # Keep processing bot queues until they are all empty...
        while self.bots:

            # Check each bot to see if it's ready to pass on values
            for bot, values in dict(self.bots).items():

                # Bot has two values, pass them on to the high and low
                # destinations specified in our graph for the bot
                if len(values) == 2:
                    low_value, high_value = sorted(self.bots.pop(bot))
                    (low_dest_type, low_dest), (high_dest_type, high_dest) = \
                            self.graph[bot]
                    self.bots[low_dest].append(low_value) \
                            if low_dest_type == 'bot' \
                            else self.outs[low_dest].append(low_value)
                    self.bots[high_dest].append(high_value) \
                            if high_dest_type == 'bot' \
                            else self.outs[high_dest].append(high_value)

                    # Find the bot that compares the values we're seeking
                    # (if we're seeking a particular bot)
                    if seeking and seeking == (low_value, high_value):
                        sought_bot = bot

        return sought_bot

    def multiply_output_values(self, *which_outputs):
        result = 1
        for i in which_outputs:
            result *= self.outs[i][0]
        return result


if __name__ == '__main__':
    with open('input.txt') as f:
        bw = BotWrangler(f.read().splitlines())
        print("Part 1:", bw.process_bot_queues(seeking=(17, 61)))
        print("Part 2:", bw.multiply_output_values(0, 1, 2))
