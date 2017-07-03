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
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    smallest = i

    if leftChild < len(heap) and heap[leftChild] < heap[smallest]:
        smallest = leftChild

    if rightChild < len(heap) and heap[rightChild] < heap[smallest]:
        smallest = rightChild


    if smallest != i:
        heap[smallest], heap[i] = heap[i], heap[smallest]
        __minHeapify(heap, smallest)


if __name__ == '__main__':
    heap = [Item('test10', 10), Item('test3', 3), Item('test5', 5), Item('test4', 4), Item('test6', 6)]

    __minHeapify(heap, 0)

    for item in heap:
        print(item.key, end = " ")