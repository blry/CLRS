#!/usr/bin/env python
# coding=utf-8

def selectionSort(A):
    for i in range(0, len(A) - 2):
        m = i
        for j in range(i + 1, len(A)):
            if(A[j] < A[m]):
                m = j
        A[i], A[m] = A[m], A[i]

A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 100, -100, 100, -100, -1000]

selectionSort(A)

print(A)