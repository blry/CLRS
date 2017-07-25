#!/usr/bin/env python
# coding=utf-8


def fibonacci(n):
    k = [1, 1]

    for i in range(3, n + 1):
        k = [k[1], k[0] + k[1]]

    return k[1]


if __name__ == '__main__':
    n = 1000

    print(fibonacci(n))
