#!/usr/bin/env python
# coding=utf-8

def maxHeapify(A, i):
    global heapSize

    while True: 
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largest = i

        if leftChild < heapSize and A[leftChild] > A[largest]:
            largest = leftChild

        if rightChild < heapSize and A[rightChild] > A[largest]:
            largest = rightChild

        if largest != i:
            A[largest], A[i] = A[i], A[largest]
            i = largest
        else:
            break

def buildMaxHeap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        maxHeapify(A, i)

def heapSort(A):
    global heapSize
    heapSize = len(A)

    buildMaxHeap(A)
    
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapSize -= 1
        maxHeapify(A, 0)


A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

heapSort(A)

print(A)