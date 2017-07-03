#!/usr/bin/env python
# coding=utf-8

class Item():
    def __init__(self, val, key):
        self.val = val
        self.key = key

    def __eq__(self, other):
        return self.key == other.year

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return str((self.val, self.key))


def __minHeapify(heap, i):
    global heapSize

    while True: 
        leftChild = (i << 1) + 1
        rightChild = (i + 1) << 1
        largest = i

        if leftChild < heapSize and heap[leftChild] < heap[largest]:
            largest = leftChild

        if rightChild < heapSize and heap[rightChild] < heap[largest]:
            largest = rightChild

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            i = largest
        else:
            break


def __buildMinHeap(heap):
    for i in range(len(heap) // 2 - 1, -1, -1):
        __minHeapify(heap, i)


def minHeapMinimum(heap):
    return heap[0]


def minHeapExtractMinimum(heap):
    global heapSize
 
    m = heap[0]
    heap[0] = heap[-1]
    heapSize -= 1
    del heap[-1]
    __minHeapify(heap, 0)

    return m


def minHeapDecreaseKey(heap, index, newKey):
    if heap[index].key >= newKey:
        heap[index].key = newKey
        while True:
            parent = (index + 1) // 2 - 1
            if index > 0 and heap[parent] > heap[index]:
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent
            else:
                break


def minHeapInsert(heap, item):
    global heapSize

    heapSize += 1
    heap.append(item)
    minHeapDecreaseKey(heap, len(heap) - 1, item.key)


if __name__ == '__main__':
    heap = [Item('test4', 4), Item('test1', 1), Item('test3', 3), Item('test16', 16)]

    heapSize = len(heap)

    __buildMinHeap(heap)

    minHeapInsert(heap, Item('test0', 0))
    minHeapInsert(heap, Item('test20', 20))

    for i in range(0, len(heap)):
        print(minHeapExtractMinimum(heap).key, end = " ")

