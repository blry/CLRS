#!/usr/bin/env python
# coding=utf-8

class Item():
    def __init__(self, val, key):
        self.val = val
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return str((self.key))


def __maxHeapify(heap, i, d):
    global heapSize

    while True: 
        largest = i

        firstChild = (i * d) + 1
        lastChild = (i + 1) * d
        
        for j in range(firstChild, lastChild + 1):

            if j < heapSize and heap[j] > heap[largest]:
                largest = j

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            i = largest
        else:
            break


def __buildMaxHeap(heap, d):
    for i in range(len(heap) // d - 1, -1, -1):
        __maxHeapify(heap, i, d)


def heapSort(heap, d):
    global heapSize
    heapSize = len(heap)

    __buildMaxHeap(heap, d)

    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapSize -= 1
        __maxHeapify(heap, 0, d)

def maxHeapExtractMaximum(heap, d):
    global heapSize
 
    m = heap[0]
    heap[0] = heap[-1]
    heapSize -= 1
    del heap[-1]
    __maxHeapify(heap, 0, d)

    return m

def maxHeapIncreaseKey(heap, d, index, newKey):
    if heap[index].key <= newKey:
        heap[index].key = newKey
        while True:
            parent = (index + 1) // d - 1
            if index > 0 and heap[parent] < heap[index]:
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent
            else:
                break

if __name__ == '__main__':
    heap = [Item(4, 4), Item(1, 1), Item(3, 3), Item(2, 2), Item(16, 16), Item(9, 9), Item(10, 10), Item(14, 14)]

    heapSize = len(heap)

    __buildMaxHeap(heap, 2)

    maxHeapIncreaseKey(heap, 2, 2, 1000)

    for item in heap:
        print(item.key, end = " ")

    print("\nMax: " + str(maxHeapExtractMaximum(heap, 2)) + "\nLeft: ", end="")

    for item in heap:
        print(item.key, end = " ")