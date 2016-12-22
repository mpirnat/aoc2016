#!/usr/bin/env python

"""
Solve day 21 of Advent of Code.

http://adventofcode.com/2016/day/21
"""

from collections import deque
from itertools import permutations


grammar = {
    ('swap', 'position'): lambda x: (swap_position, [int(x[2]), int(x[5])]),
    ('swap', 'letter'): lambda x: (swap_char, [x[2], x[5]]),
    ('reverse', 'positions'): lambda x: (reverse, [int(x[2]), int(x[4])]),
    ('rotate', 'left'): lambda x: (rotate, [-int(x[2])]),
    ('rotate', 'right'): lambda x: (rotate, [int(x[2])]),
    ('move', 'position'): lambda x: (move, [int(x[2]), int(x[5])]),
    ('rotate', 'based'): lambda x: (rotate_position, [x[6]]),
}


def parse(instr):
    instr = instr.split()
    fn, args = grammar[(instr[0], instr[1])](instr)
    return fn, args


def swap_position(string, pos1, pos2):
    """
    swap position X with position Y means that the letters at indexes X and Y
    (counting from 0) should be swapped.
    """
    new_string = list(string)
    new_string[pos1] = string[pos2]
    new_string[pos2] = string[pos1]
    return ''.join(new_string)


def swap_char(string, char1, char2):
    """
    swap letter X with letter Y means that the letters X and Y should be swapped
    (regardless of where they appear in the string).
    """
    pos1 = string.find(char1)
    pos2 = string.find(char2)
    return swap_position(string, pos1, pos2)


def reverse(string, pos1, pos2):
    """
    reverse positions X through Y means that the span of letters at indexes X
    through Y (including the letters at X and Y) should be reversed in order.
    """
    a = list(string)
    b = a[pos1:pos2+1]
    b.reverse()
    return ''.join(a[:pos1] + b + a[pos2+1:])


def rotate(string, steps):
    """
    rotate left/right X steps means that the whole string should be rotated; for
    example, one right rotation would turn abcd into dabc.
    """
    new_string = deque(string)
    new_string.rotate(steps)
    return ''.join(new_string)


def rotate_position(string, char):
    """
    Rotate based on position of letter X means that the whole string should be
    rotated to the right based on the index of letter X (counting from 0) as
    determined before this instruction does any rotations. Once the index is
    determined, rotate the string to the right one time, plus a number of times
    equal to that index, plus one additional time if the index was at least 4.
    """
    new_string = deque(string)
    pos = string.find(char)
    steps = 1 + pos if pos < 4 else 2 + pos
    new_string.rotate(steps)
    return ''.join(new_string)


def rotate_position_inverse(string, char):
    """
    Invert the 'rotate based on position of letter X' operation by rotating
    left and seeing if a forward rotate_position gets back to where we started.
    """
    for i in range(len(string)):
        test_string = rotate(string, -i)
        if rotate_position(test_string, char) == string:
            return test_string


def move(string, pos1, pos2):
    """
    move position X to position Y means that the letter which is at index X
    should be removed from the string, then inserted such that it ends up at
    index Y.
    """
    new_string = list(string)
    new_string.insert(pos2, new_string.pop(pos1))
    return ''.join(new_string)


def invert_instruction(f, args):
    """
    Transform a parsed instruction into its inverse
    """
    if f in (swap_position, swap_char, move):
        args.reverse()

    elif f == rotate:
        args[0] = -args[0]

    elif f == rotate_position:
        f = rotate_position_inverse

    return f, args


def scramble(instructions, string):
    """
    Part 1: apply the scrambling instructions verbatim
    """
    for instr in instructions:
        f, args = parse(instr)
        string = f(string, *args)
    return string


def unscramble_brutally(instructions, string):
    """
    Part 2: Brute force the unscrambled string by applying the
    instructions to every permutation of our possible characters.
    """
    for test_string in permutations('abcdefgh'):
        if scramble(instructions, test_string) == string:
            return ''.join(test_string)


def unscramble_elegantly(instructions, string):
    """
    Part 2: Unscramble the string by inverting the instructions
    and applying them in reverse order to find the starting string.
    """
    parsed = [invert_instruction(*parse(x)) for x in instructions]
    parsed.reverse()

    for f, args in parsed:
        string = f(string, *args)

    return string


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = f.read().splitlines()

        string = 'abcdefgh'
        print("Part 1:", scramble(instructions, string))

        string = 'fbgdceah'
        print("Part 2:", unscramble_elegantly(instructions, string))

        # Don't need to do this any more
        #print("Part 2:", unscramble_brutally(instructions, string))
