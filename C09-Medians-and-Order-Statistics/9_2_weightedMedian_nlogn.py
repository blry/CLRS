#!/usr/bin/env python
# coding=utf-8

from random import randrange, shuffle, uniform
import time


class Item():
    def __init__(self, val, key):
        self.val = val
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return str((self.val, self.key))


def __maxHeapify(heap, i):
    global heapSize

    while True: 
        leftChild = (i << 1) + 1
        rightChild = (i + 1) << 1
        largest = i

        if leftChild < heapSize and heap[leftChild] > heap[largest]:
            largest = leftChild

        if rightChild < heapSize and heap[rightChild] > heap[largest]:
            largest = rightChild

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            i = largest
        else:
            break


def __buildMaxHeap(heap):
    for i in range(len(heap) // 2 - 1, -1, -1):
        __maxHeapify(heap, i)


def heapSort(heap):
    global heapSize
    heapSize = len(heap)

    __buildMaxHeap(heap)
    
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapSize -= 1
        __maxHeapify(heap, 0)



if __name__ == '__main__':
    
    A = [Item(0.1, 0.1), Item(0.35, 0.35), Item(0.05, 0.05), Item(0.1, 0.1), Item(0.15, 0.15), Item(0.05, 0.05), Item(0.2, 0.2)]

    w = 0
    
    heapSort(A)

    for i in range(0, len(A)):
        w += A[i].val
        if(w >= 0.5):
            break

    print(A[i].key)