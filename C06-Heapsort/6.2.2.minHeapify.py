#!/usr/bin/env python
# coding=utf-8

def minHeapify(A, i):
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    smallest = i

    if leftChild < len(A) and A[leftChild] < A[smallest]:
        smallest = leftChild

    if rightChild < len(A) and A[rightChild] < A[smallest]:
        smallest = rightChild


    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        minHeapify(A, smallest)


A = [10, 3, 5, 4, 6]

minHeapify(A, 0)

print(A)