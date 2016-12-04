#!/usr/bin/env python

"""
Solve day 4 of Advent of Code.

http://adventofcode.com/2016/day/4
"""

import re
from collections import Counter


def parse_room(room):
    match = re.match(r'(.+)-(\d+)\[(\w+)\]', room)
    name, sector_id, checksum = match.groups()
    name = name.replace('-', '')
    sector_id = int(sector_id)
    return (name, sector_id, checksum)


def make_checksum(name):
    checksum = ''.join([x[0] for x in
            sorted(Counter(name).most_common(),
                key=lambda x: (-x[1], x[0]))[:5]])
    return checksum


def is_real_room(name, checksum):
    return make_checksum(name) == checksum


def sum_of_sectors(rooms):
    sectors = []
    for room in rooms:
        name, sector, checksum = parse_room(room)
        if is_real_room(name, checksum):
            sectors.append(sector)
    return sum(sectors)


def decrypt_room_name(room):
    name, sector_id, checksum = parse_room(room)
    for i in range(sector_id):
        name = ''.join([
            chr(ord(x)+1) if x != 'z' else 'a'
            for x in name])
    return name


def find_decrypted_room_name(objective, rooms):
    objective = objective.lower().strip().replace(' ', '')

    for room in rooms:
        name, sector_id, checksum = parse_room(room)
        if not is_real_room(name, checksum):
            continue

        plaintext = decrypt_room_name(room)
        #print(name, plaintext)
        if objective in plaintext:
            #print(room, plaintext)
            return sector_id


if __name__ == '__main__':
    with open('input.txt') as f:
        rooms = f.readlines()
        print("Part 1:", sum_of_sectors(rooms))
        print("Part 2:", find_decrypted_room_name("North Pole", rooms))
