#!/usr/bin/env python
# coding=utf-8


def fibonacci(n):
    k = [1] * (n + 1)

    for i in range(3, n + 1):
        k[i] = k[i - 1] + k[i - 2]

    return k[n]


if __name__ == '__main__':
    n = 1000

    print(fibonacci(n))