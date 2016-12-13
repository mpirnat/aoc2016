#!/usr/bin/env python

"""
Solve day 12 of Advent of Code.

http://adventofcode.com/2016/day/12
"""

from collections import defaultdict


def run_code(code, init=None):
    pc = 0
    code_len = len(code)

    registers = defaultdict(int)
    if init:
        registers.update(init)

    while pc < code_len:
        instr, *args = code[pc].split()
        args = [int(x) if not x.isalpha() else x for x in args]

        if instr == 'cpy':
            registers[args[1]] = registers.get(args[0]) or args[0]

        elif instr == 'inc':
            registers[args[0]] += 1

        elif instr == 'dec':
            registers[args[0]] -= 1

        elif instr == 'jnz':
            if registers.get(args[0]) or (isinstance(args[0], int) and args[0]):
                pc += args[1]
                continue
        pc += 1

    return registers


if __name__ == '__main__':
    with open('input.txt') as f:
        code = f.read().splitlines()
        registers = run_code(code)
        print("Part 1:", registers)

        registers = run_code(code, init={'c': 1})
        print("Part 2:", registers)
