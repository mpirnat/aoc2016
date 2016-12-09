#!/usr/bin/env python

"""
Solve day 9 of Advent of Code.

http://adventofcode.com/2016/day/9
"""

import re


def decompress(data, recursive=False):
    # Get rid of whitespace just in case
    data = re.sub(r'\s', '', data)

    # No markers in data, just return its length
    if '(' not in data:
        return len(data)

    length = 0

    # There are still markers in the data that must be processed...
    while '(' in data:

        # Find where the marker starts
        next_marker_start = data.find('(')

        # Add the characters leading up to the marker
        length += next_marker_start

        # Discard characters we've just counted
        data = data[next_marker_start:]

        # Find where the marker ends
        next_marker_end = data.find(')')

        # Figure out what the marker is telling us:
        # how many characters will be repeated, how many times?
        num_chars, times = [int(x) for x in data[1:next_marker_end].split('x')]

        # And discard the marker now that we've consumed it
        data = data[next_marker_end + 1:]

        # Add the expanded characters; recursively if we're doing part 2,
        # or not if we're doing part 1.
        if recursive:
            length += decompress(data[:num_chars], recursive=True) * times
        else:
            length += len(data[:num_chars]) * times

        # And discard the characters we've consumed in the expansion
        data = data[num_chars:]

    # No more markers, add any post-expansion leftovers
    length += len(data)

    return length


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
        print("Part 1:", decompress(data))
        print("Part 2:", decompress(data, recursive=True))
