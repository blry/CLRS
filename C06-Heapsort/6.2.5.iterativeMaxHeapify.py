#!/usr/bin/env python
# coding=utf-8

def iterativeMaxHeapify(A, i):

    while True: 
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largest = i

        if leftChild < len(A) and A[leftChild] > A[largest]:
            largest = leftChild

        if rightChild < len(A) and A[rightChild] > A[largest]:
            largest = rightChild


        if largest != i:
            A[largest], A[i] = A[i], A[largest]
            i = largest
        else:
            break

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

iterativeMaxHeapify(A, 1)

print(A)