#!/usr/bin/env python
# coding=utf-8


def insertionRecSort(A, n):
    if(n > 1):
        insertionRecSort(A, n - 1)
        for i in range(0, n):
            if A[i] > A[n]:
                A[i], A[n] = A[n], A[i]


if __name__ == '__main__':
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 100, -100, 100, -100, -1000]

    insertionRecSort(A, len(A) - 1)

    print(A)
