#!/usr/bin/env python

"""
Solve day 16 of Advent of Code.

http://adventofcode.com/2016/day/16

This solution is super-naïve and not at all optimised, but it took less time to
run part 2 on my 2011 Macbook Air than it did to start reading suggestions on
the AOC subreddit on how to make it more efficient, so I kind of don't really
care that much. ¯\_(ツ)_/¯
"""

import re


def generate_data(data, disk_size):
    """
    Start with an appropriate initial state (your puzzle input). Then, so long
    as you don't have enough data yet to fill the disk, repeat the following
    steps:

        * Call the data you have at this point "a".
        * Make a copy of "a"; call this copy "b".
        * Reverse the order of the characters in "b".
        * In "b", replace all instances of 0 with 1 and all 1s with 0.
        * The resulting data is "a", then a single 0, then "b".
    """
    while len(data) < disk_size:
        a = b = data
        b = ''.join(['1' if char == '0' else '0' for char in b[-1::-1]])
        data = a + '0' + b
    return data


def generate_checksum(data, disk_size):
    """
    The checksum for some given data is created by considering each
    non-overlapping pair of characters in the input data. If the two characters
    match (00 or 11), the next checksum character is a 1. If the characters do
    not match (01 or 10), the next checksum character is a 0. This should
    produce a new string which is exactly half as long as the original. If the
    length of the checksum is even, repeat the process until you end up with a
    checksum with an odd length.
    """
    data = data[:disk_size]
    checksum = data

    while len(checksum) % 2 == 0:
        pairs = re.findall(r'\d\d', checksum)
        checksum = ''.join(['1' if x[0] == x[1] else '0' for x in pairs])

    return checksum


if __name__ == '__main__':
    disk_size = 272
    initial_data = '01111001100111011'

    data = generate_data(initial_data, disk_size)
    checksum = generate_checksum(data, disk_size)
    print("Part 1:", checksum)

    disk_size = 35651584
    data = generate_data(initial_data, disk_size)
    checksum = generate_checksum(data, disk_size)
    print("Part 2:", checksum)

