#!/usr/bin/env python

"""
Solve day 23 of Advent of Code.

http://adventofcode.com/2016/day/23
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
                pc += registers.get(args[1]) or args[1]
                continue

        elif instr == 'tgl':
            offset = registers.get(args[0]) or args[0]
            addr = pc + offset
            if addr < 0 or addr >= len(code):
                pc += 1
                continue

            other_line = code[addr]

            if other_line.startswith('cpy'):
                code[addr] = other_line.replace('cpy', 'jnz')
            elif other_line.startswith('jnz'):
                code[addr] = other_line.replace('jnz', 'cpy')
            elif other_line.startswith('inc'):
                code[addr] = other_line.replace('inc', 'dec')
            elif other_line.startswith('dec'):
                code[addr] = other_line.replace('dec', 'inc')
            elif other_line.startswith('tgl'):
                code[addr] = other_line.replace('tgl', 'inc')

        pc += 1

    return registers


if __name__ == '__main__':
    with open('input.txt') as f:
        code = f.read().splitlines()
        registers = run_code(code, init={'a': 7})
        print("Part 1:", registers)

#        registers = run_code(code, init={'a': 12})
#        print("Part 2:", registers)
