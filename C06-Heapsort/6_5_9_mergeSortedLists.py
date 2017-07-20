#!/usr/bin/env python
# coding=utf-8

'''
Give an O(nlgk)-time algorithm to merge k sorted lists into one sorted list, 
where n is the total number of elements in all the input lists. 
(Hint: Use a min-heap for k-way merging).
'''

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
    l1 = [Item('test1', 1), Item('test3', 3), Item('test16', 16), Item('test40', 40)]
    l2 = [Item('test2', 2), Item('test10', 10), Item('test30', 30), Item('test40', 40), Item('test160', 160)]

    lists = [l1, l2]
    heap = []
    heapSize = 0;

    for i in range(0, len(lists)):
        lists[i][0].listNo = i;
        minHeapInsert(heap, lists[i][0])
        del lists[i][0]

    sortedList = []

    while heapSize > 0:
        o = minHeapExtractMinimum(heap)
        sortedList.append(o)
        if lists[o.listNo]:
            lists[o.listNo][0].listNo = o.listNo
            minHeapInsert(heap, lists[o.listNo][0])
            del lists[o.listNo][0]


    for i in range(0, len(sortedList)):
        print(sortedList[i].key, end = " ")