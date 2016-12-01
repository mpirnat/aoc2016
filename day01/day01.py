#!/usr/bin/env python

"""
Solve day 1 of Advent of Code.

http://adventofcode.com/2016/day/1
"""


def position_from_instructions(instructions, path=None):
    """
    Find out what position we're at after following a set of instructions.
    """
    x = y = 0
    heading = 0 # 0 = N, 1 = E, 2 = S, 3 = W

    instructions = instructions.split(', ')

    for instruction in instructions:
        turn = instruction[:1]
        distance = int(instruction[1:])

        if turn == 'R':
            heading = (heading + 1) % 4
        elif turn == 'L':
            heading = (heading - 1) % 4

        #print("turn {turn}, heading {heading}, go {distance}".format(**locals()))

        for i in range(distance):
            if heading == 0:
                y += 1
            elif heading == 1:
                x += 1
            elif heading == 2:
                y -= 1
            elif heading == 3:
                x -= 1
            if path is not None:
                path.append((x, y))

    #print((x,y))
    return (x, y)


def distance_from_origin(position):
    """
    Get the 'taxicab geometry' distance of a position from the origin (0, 0).
    """
    return sum([abs(x) for x in position])


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = f.read()

        path = [(0, 0)]
        position = position_from_instructions(instructions, path)
        distance = distance_from_origin(position)
        print("Part 1:", distance)

        positions_seen = {}
        for pos in path:
            if pos in positions_seen:
                distance = distance_from_origin(pos)
                print("Part 2:", distance)
                break
            else:
                positions_seen[pos] = True
