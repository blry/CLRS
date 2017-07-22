#!/usr/bin/env python
# coding=utf-8

from random import randrange, shuffle
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


def maxHeapMaximum(heap):
    return heap[0]


def maxHeapExtractMaximum(heap):
    global heapSize
 
    m = heap[0]
    heap[0] = heap[-1]
    heapSize -= 1
    del heap[-1]
    __maxHeapify(heap, 0)

    return m


def maxHeapIncreaseKey(heap, index, newKey):
    if heap[index].key <= newKey:
        heap[index].key = newKey
        while True:
            parent = (index + 1) // 2 - 1
            if index > 0 and heap[parent] < heap[index]:
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent
            else:
                break


def maxHeapInsert(heap, item):
    global heapSize

    heapSize += 1
    heap.append(item)
    maxHeapIncreaseKey(heap, len(heap) - 1, item.key)


def randomizedSelectTop(A, begin, end, ist):
    if begin == end:
        return A[begin:]

    randIndex = randrange(begin, end + 1)
    A[end], A[randIndex] = A[randIndex], A[end]

    pivot = begin

    for i in range(begin + 1, end + 1):
        if A[i].key <= A[begin].key:
            pivot += 1
            A[i], A[pivot] = A[pivot], A[i]

    A[pivot], A[begin] = A[begin], A[pivot]

    k = pivot - begin + 1

    if ist == k:
        return A[pivot:]
    elif ist < k:
        return randomizedSelectTop(A, begin, pivot - 1, ist)
    else:
        return randomizedSelectTop(A, pivot + 1, end, ist - k)



if __name__ == '__main__':
    i = 10
    n = 20000

    A = [Item('a', randrange(n)) for j in range(n)]

    # A (sorting)               i + n * lg n 
    heap = A[:]

    t = time.time()

    heapSort(heap)

    for item in heap[:-i - 1:-1]:
        print(item.key, end = " ")

    print(time.time() - t)
    
    # B (max-priority queue)    n + i * lg n
    heap = []
    heapSize = 0

    t = time.time()

    for item in A:
        maxHeapInsert(heap, item)

    for j in range(0, i):
        print(maxHeapExtractMaximum(heap).key, end = " ")

    print(time.time() - t)
    
    # C (partition and sort)    n + i * lg i
    heap = A[:]

    t = time.time()

    heap = randomizedSelectTop(heap, 0, len(heap) - 1, len(heap) - i + 1)
    heapSort(heap)

    for item in heap[::-1]:
        print(item.key, end = " ")
    
    print(time.time() - t)

    # Python sort
    
    t = time.time()
    
    A.sort()
    
    for item in A[: -i - 1: -1]:
        print(item.key, end = " ")

    print(time.time() - t)