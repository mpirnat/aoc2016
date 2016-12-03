#!/usr/bin/env python

"""
Solve day 3 of Advent of Code.

http://adventofcode.com/2016/day/3
"""


def is_possible_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a


def parse_line(line):
    return [int(x) for x in line.split()]


def count_possible_triangles_in_rows(f):
    count = 0

    for line in f:
        if is_possible_triangle(*parse_line(line)):
            count += 1

    return count


def count_possible_triangles_in_columns(f):
    count = 0
    line_buffer = []

    for line in f:
        line_buffer.append(parse_line(line))
        if len(line_buffer) != 3:
            continue

        for sides in zip(line_buffer[0], line_buffer[1], line_buffer[2]):
            if is_possible_triangle(*sides):
                count += 1

        line_buffer = []

    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        print("Part 1:", count_possible_triangles_in_rows(f))

    with open('input.txt') as f:
        print("Part 2:", count_possible_triangles_in_columns(f))
