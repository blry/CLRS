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
    while True: 
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largest = i

        if leftChild < len(heap) and heap[leftChild] > heap[largest]:
            largest = leftChild

        if rightChild < len(heap) and heap[rightChild] > heap[largest]:
            largest = rightChild


        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            i = largest
        else:
            break


if __name__ == '__main__':
    heap = [Item('test0', 0), Item('test1', 1), Item('test3', 3), Item('test16', 16)]

    __maxHeapify(heap, 0)

    for item in heap:
        print(item.key, end = " ")