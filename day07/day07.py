#!/usr/bin/env python

"""
Solve day 7 of Advent of Code.

http://adventofcode.com/2016/day/7
"""

import re


def count_tls_addresses(data):
    return sum(supports_tls(x) for x in data)


def supports_tls(text):
    return any(has_abba(x) for x in get_abba_allowed_strings(text)) \
            and not any(has_abba(x) for x in get_abba_disallowed_strings(text))


def count_ssl_addresses(data):
    return sum(supports_ssl(x) for x in data)


def supports_ssl(text):
    strings1 = get_abba_allowed_strings(text)
    strings2 = get_abba_disallowed_strings(text)

    abas = [find_abas(x) for x in strings1]
    abas = [y for x in abas for y in x]
    babs = [bab_from_aba(x) for x in abas]

    return any(bab in x for bab in babs for x in strings2)


def find_abas(text):
    abas = set()

    for i in range(len(text)):
        try:
            if text[i] != text[i+1] \
                    and text [i] == text[i+2]:
                abas.add(text[i:i+3])
        except IndexError:
            break

    return sorted(list(abas))


def bab_from_aba(aba):
    return aba[1] + aba[0] + aba[1]


def get_abba_allowed_strings(text):
    return re.split(r'\[\w+\]', text)


def get_abba_disallowed_strings(text):
    return [x.replace('[', '').replace(']', '')
            for x in re.findall(r'\[\w+\]', text)]


def has_abba(text):
    for i in range(len(text)):
        try:
            if text[i] != text[i+1] \
                    and text[i] == text[i+3] \
                    and text[i+1] == text[i+2]:
                return True
        except IndexError:
            break
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        print("Part 1:", count_tls_addresses(f))

    with open('input.txt') as f:
        print("Part 2:", count_ssl_addresses(f))
