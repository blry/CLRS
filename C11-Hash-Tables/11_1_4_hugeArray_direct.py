#!/usr/bin/env python
# coding=utf-8

import random

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def insert(x):
    global huge_array
    global additional_array
    huge_array[x.key] = len(additional_array)
    additional_array.append((x.key, x))


def delete(x):
    global huge_array
    huge_array[x.key] = -1


def search(k):
    global huge_array
    global additional_array
    idx = huge_array[k]
    if 0 <= idx < len(additional_array):
        if additional_array[idx][0] == k:
            return additional_array[idx][1]
    return None


if __name__ == '__main__':
    huge_array = [random.randint(0, 10000) for _ in range(10007)]
    additional_array = []

    insert(Item(10, 100))
    insert(Item(20, 200))
    print(search(20).value)