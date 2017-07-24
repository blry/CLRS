#!/usr/bin/env python
# coding=utf-8

from random import randint, shuffle


def randomSearch(A, value):
    P = []
    while True:
        k = randint(0, len(A) - 1)
        if A[k] == value:
            return k
        else:
            if k not in P:
                P.append(k)
                if len(P) == len(A):
                    return None


def determenisticSearch(A, value):
    for i in range(0, len(A)):
        if A[i] == value:
            return i

    return None


def scrambleSearch(A, value):
    shuffle(A)
    return determenisticSearch(A, value)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7] 

    print(scrambleSearch(A, -3))
