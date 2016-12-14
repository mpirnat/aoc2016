#!/usr/bin/env python

"""
Solve day 14 of Advent of Code.

http://adventofcode.com/2016/day/14
"""

import re
from collections import deque
from hashlib import md5

triple = re.compile(r'(\w)\1\1')


def make_hash(salt, index):
    return md5((salt+str(index)).encode('utf8')).hexdigest()


def hash_at(hashes, salt, index):
    try:
        my_hash = hashes[index]
    except IndexError:
        my_hash = make_hash(salt, index)
        hashes.append(my_hash)
    return my_hash


def find_keys(salt, max_keys=1):
    hashes = []
    keys = []
    i = 0

    considering_key = False

    while len(keys) < max_keys:
        # Pull a hash from the queue; if we don't have one, make one
        # Check if it contains a triple
        # If it does, look for a 5-le in the next 1000 hashes
        # If we find one, put it in the keys list
        # Regardless, rewind hash queue to i+1 and keep looking

        # Pull a hash or make a new one
        this_hash = hash_at(hashes, salt, i)

        # Does this hash have a triple in it?
        match = triple.search(this_hash)
        if match:
            char = match.groups()[0]

            # Look for 5-le in the next 1000 hashes
            for j in range(i+1, i+1000):
                new_hash = hash_at(hashes, salt, j)

                if char * 5 in new_hash:
                    keys.append((i, this_hash, char))
                    break

        # Don't actually forget this, it's important (derp)
        i += 1

    return keys


if __name__ == '__main__':
    salt = 'ngcjuoqr'
    keys = find_keys(salt, max_keys=64)
    print("Part 1:", keys[-1][0])
