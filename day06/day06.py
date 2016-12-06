#!/usr/bin/env python

"""
Solve day 6 of Advent of Code.

http://adventofcode.com/2016/day/6
"""

from collections import Counter


def decode_most_common(data):
    message = ""
    cols = data_by_cols(data)

    for col in cols:
        c = Counter(col)
        char = c.most_common(1)[0][0]
        message += char

    return message


def decode_least_common(data):
    message = ""
    cols = data_by_cols(data)

    for col in cols:
        c = Counter(col)
        char = c.most_common()[-1][0]
        message += char

    return message


def data_by_cols(data):
    cols = []
    for line in data:
        for i, char in enumerate(line):
            if len(cols) == i:
                cols.append([])
            cols[i].append(char)
    return cols


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.readlines()
        message = decode_most_common(data)
        print("Part 1:", message)

        message2 = decode_least_common(data)
        print("Part 2:", message2)
