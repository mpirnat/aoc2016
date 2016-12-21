#!/usr/bin/env python

"""
Solve day 20 of Advent of Code.

http://adventofcode.com/2016/day/20
"""


def sorted_ranges(data):
    ranges = [line.split('-') for line in data]
    ranges = sorted([(int(x), int(y)) for (x, y) in ranges])
    return ranges


def first_open_address(ranges):
    i = 0

    for range_start, range_end in ranges:
        if range_start <= i <= range_end:
            i = range_end + 1

    return i


def count_open_addresses(ranges, start=0, end=4294967295):
    address = start
    index = 0
    total = 0

    while address <= end:
        # Get the next range to work with
        try:
            range_start, range_end = ranges[index]

        # We're out of ranges, so it's open season
        except IndexError:
            total += 1
            address += 1
            continue

        # Address might be in range?
        if range_start <= address:
            # Yep, address is in range, skip to end of range
            if address <= range_end:
                address = range_end + 1
                continue
            # Nope, try the next range
            index += 1

        # Address not in any ranges, add it to the total
        # and move on to checking the next address
        else:
            total += 1
            address += 1

    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        ranges = sorted_ranges(f)

        print("Part 1:", first_open_address(ranges))
        print("Part 2:", count_open_addresses(ranges))
