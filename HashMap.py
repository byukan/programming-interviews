#!/usr/bin/python
# -*- coding: utf-8 -*-


def _get_hash(key):
    """
    hash function, modded sum of the ascii values of chars in string
    :param: key gets mapped to an integer value
    :return: hash key in the range of self.map's size
"""

    ascii_sum = 0
    for char in key:
        ascii_sum += ord(char)
    return ascii_sum


class Hashmap:
    """
    member functions: init, _get_hash, add, value, delete, print
    """

    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    def add(self, key, value):
        """
        add key value pair to hashmap
        """

    # declare key_hash, key_value

        key_hash = _get_hash(key)
        key_value = [key, value]

        # add to self.map

        if self.map[key_hash] is None:
            self.map[key_hash] = key_value
            return True
        else:

            # handle collisions

            for pair in self.map[key_hash]:

                # update value if key is already in inner list

                if pair[0] == key:
                    pair[1] = value
                    return True

            # append new key if not found in inner list

            self.map[key_hash].append(key_value)
            return True

    def value(self, key):
        key_hash = _get_hash(key)
        if self.map[key_hash] is None:
            raise Exception('KeyError')
        else:

            # get the right key by looping through self.map[key_hash]

            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
                    return True
            raise Exception('KeyError')

    def delete(self, key):
        key_hash = _get_hash(key)
        if self.map[key_hash] is None:
            raise Exception('KeyError')
        else:

            # get the right key by looping through self.map[key_hash]

            for (i, pair) in enumerate(self.map[key_hash]):
                if pair[0] == key:
                    self.map[key_hash].pop(i)
                    return True
            raise Exception('KeyError')

    def print_hashmap(self):
        for x in self.map:
            if x is not None:
                print
                str(x)
