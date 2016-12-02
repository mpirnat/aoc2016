#!/usr/bin/env python

"""
Solve day 2 of Advent of Code.

http://adventofcode.com/2016/day/2
"""

part1_buttons = [["1", "2", "3"],
                 ["4", "5", "6"],
                 ["7", "8", "9"]]

part2_buttons = [[None, None, "1", None, None],
                 [None, "2", "3", "4", None],
                 ["5", "6", "7", "8", "9"],
                 [None, "A", "B", "C", None],
                 [None, None, "D", None, None]]


def get_next_button(start, buttons, instructions):
    orig_position = find_button(start, buttons)
    position = orig_position[:]
    row_limit = len(buttons) - 1
    col_limit = len(buttons[0]) - 1

    for instruction in instructions:
        if instruction == "U" and position[0] > 0:
            position[0] -= 1
        elif instruction == "D" and position[0] < row_limit:
            position[0] += 1
        elif instruction == "L" and position[1] > 0:
            position[1] -= 1
        elif instruction == "R" and position[1] < col_limit:
            position[1] += 1

        if buttons[position[0]][position[1]]:
            orig_position = position[:]
        else:
            position = orig_position[:]

    return buttons[position[0]][position[1]]


def find_button(button, buttons):
    for i, row in enumerate(buttons):
        for j, col in enumerate(row):
            if buttons[i][j] == button:
                return [i, j]


if __name__ == '__main__':
    with open('input.txt') as f:
        combo1 = []
        combo2 = []
        start1 = "5"
        start2 = "5"

        for line in f:
            combo1.append(get_next_button(start1, part1_buttons, line))
            combo2.append(get_next_button(start2, part2_buttons, line))
            start1 = combo1[-1]
            start2 = combo2[-1]

        print("Part 1:", ''.join(combo1))
        print("Part 2:", ''.join(combo2))
