#!/usr/bin/env python

"""
Solve day 2 of Advent of Code.

http://adventofcode.com/2016/day/2
"""

buttons = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def get_next_button(start, instructions):
    position = find_button(start)
    for instruction in instructions:
        if instruction == "U" and position[0] > 0:
            position[0] -= 1
        elif instruction == "D" and position[0] < 2:
            position[0] += 1
        elif instruction == "L" and position[1] > 0:
            position[1] -= 1
        elif instruction == "R" and position[1] < 2:
            position[1] += 1

    return buttons[position[0]][position[1]]


def find_button(button):
    for i, row in enumerate(buttons):
        for j, col in enumerate(row):
            if buttons[i][j] == button:
                return [i, j]


if __name__ == '__main__':
    with open('input.txt') as f:
        combo = []
        start = "5"

        for line in f:
            combo.append(get_next_button(start, line))
            start = combo[-1]

        print("Part 1:", ''.join(combo))
