#!/usr/bin/env python
# coding=utf-8


def modifiedQuickSort(A, no, begin, end):
    if begin >= end:
        return

    pivot = begin

    for i in range(begin+1, end+1):
        if A[i][no] <= A[begin][no]:
            pivot += 1
            A[i], A[pivot] = A[pivot], A[i]

    A[pivot], A[begin] = A[begin], A[pivot]

    modifiedQuickSort(A, no, begin, pivot-1)
    modifiedQuickSort(A, no, pivot+1, end)

    return A


def radixSort(A, d):
    for i in range(d - 1, -1, -1):
        A = modifiedQuickSort(A, i, 0, len(A) - 1)


if __name__ == '__main__':
    A = ['AAA', 'COW', 'DOG', 'SEA', 'RUG', 'ROW', 'MOB', 'BOX', 'TAB', 'BAR', 'EAR', 'TAR', 'DIG', 'BIG', 'TEA', 'NOW', 'FOX', 'AAA']

    radixSort(A, len(A[0]))

    print(A)
