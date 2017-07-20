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



if __name__ == '__main__':
    heap = [Item(4, 4), Item(1, 1), Item(3, 3), Item(2, 2), Item(16, 16), Item(9, 9), Item(10, 10), Item(14, 14)]

    heapSize = len(heap)

    __buildMaxHeap(heap)

    maxHeapInsert(heap, Item(0, 0))
    maxHeapInsert(heap, Item(20, 20))

    for i in range(0, heapSize):
        print(maxHeapExtractMaximum(heap).key, end = " ")