#!/usr/bin/env python
# coding=utf-8


def binSearch(A, x):
    start, end = 0, len(A) - 1

    while(start <= end):
        mid = (start + end) // 2

        if(A[mid] < x):
            start = mid + 1
        elif(A[mid] > x):
            end = mid - 1
        else:
            return mid

    return None


if __name__ == '__main__':
    A = [-1, 0, 4, 100, 123, 124, 151, 162]

    print(binSearch(A, 123))
