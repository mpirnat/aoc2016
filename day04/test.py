#!/usr/bin/env python

import unittest
from day04 import parse_room, make_checksum, is_real_room, sum_of_sectors
from day04 import decrypt_room_name, find_decrypted_room_name


class TestIdentifiesRealRooms(unittest.TestCase):
    """
aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a
(5), b (3), and then a tie between x, y, and z, which are listed alphabetically.

a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
tied (1 of each), the first five are listed alphabetically.

not-a-real-room-404[oarel] is a real room.

totally-real-room-200[decoy] is not.
    """

    cases = (
        ('aaaaa-bbb-z-y-x-123[abxyz]', ('aaaaabbbzyx', 123, 'abxyz'), 'abxyz', True),
        ('a-b-c-d-e-f-g-h-987[abcde]', ('abcdefgh', 987, 'abcde'), 'abcde', True),
        ('not-a-real-room-404[oarel]', ('notarealroom', 404, 'oarel'), 'oarel', True),
        ('totally-real-room-200[decoy]', ('totallyrealroom', 200, 'decoy'),
                'loart', False),
    )

    def test_parses_rooms(self):
        for room, parsed, *_ in self.cases:
            self.assertEqual(parse_room(room), parsed)

    def test_calculates_checksums(self):
        for room, parsed, checksum, _ in self.cases:
            name, sector, _ = parse_room(room)
            self.assertEqual(make_checksum(name), checksum)

    def test_identifies_real_rooms(self):
        for room, *_, is_real in self.cases:
            name, sector, checksum = parse_room(room)
            self.assertEqual(is_real_room(name, checksum), is_real)

    def test_sums_valid_sectors(self):
        rooms = [x[0] for x in self.cases]
        self.assertEqual(sum_of_sectors(rooms), 1514)


class TestDecryptingRoomNames(unittest.TestCase):

    cases = (
        ('qzmt-zixmtkozy-ivhz-343[zimth]', 'veryencryptedname'),
    )

    def test_decrypts_room_names(self):
        for room, expected_plaintext in self.cases:
            self.assertEqual(decrypt_room_name(room), expected_plaintext)

    def test_finds_decrypted_room_names(self):
        rooms = ['garbage-nope-123[lol]', 'haystack-57[wtf]'] + \
                [x[0] for x in self.cases]
        self.assertEqual(find_decrypted_room_name('Very Encrypted', rooms), 343)


if __name__ == '__main__':
    unittest.main()
