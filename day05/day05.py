#!/usr/bin/env python

"""
Solve day 5 of Advent of Code.

http://adventofcode.com/2016/day/5
"""

import hashlib

def find_password(door):
    password = ''
    index = 0

    while len(password) < 8:
        # For my personal sanity...
        if index % 10000 == 0:
            print(index)

        to_hash = door + str(index)
        hashed = hashlib.md5(to_hash.encode('utf8')).hexdigest()
        if hashed.startswith('00000'):
            password += hashed[5]
            # It's nice to have occasional glimmers of hope...
            print("Found one!", password)

        index += 1

    return password


def find_password2(door):
    password = [None] * 8

    while None in password:
        # For my personal sanity...
        if index % 10000 == 0:
            print(index)

        to_hash = door + str(index)
        hashed = hashlib.md5(to_hash.encode('utf8')).hexdigest()
        if hashed.startswith('00000') and hashed[5].isdigit():
            pw_index = int(hashed[5])
            if pw_index < 8 and not password[pw_index]:
                password[pw_index] = hashed[6]
                # It's nice to have occasional glimmers of hope...
                print("Found one!", password)

        index += 1

    return ''.join(password)


if __name__ == '__main__':
    door = 'ojvtpuvg'
    print("Part 1:", find_password(door))
    print("Part 2:", find_password2(door))
