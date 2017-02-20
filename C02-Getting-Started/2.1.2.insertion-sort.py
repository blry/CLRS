#!/usr/bin/env python
# coding=utf-8

def insertionSort(A):
    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while(j >= 0 and A[j] > k):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = k

A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 100, -100, 100, -100, -1000]

insertionSort(A)

print(A)