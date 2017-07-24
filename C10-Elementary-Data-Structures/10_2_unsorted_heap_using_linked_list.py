#!/usr/bin/env python
# coding=utf-8

from random import randrange

class Node():
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return str(self.key)


class Heap():
    def __init__(self):
        self.head = self.tail = None


    def minimum(self):
        node = buf = self.head

        while node.nextNode is not self.head:
            if node.nextNode < buf:
                buf = node.nextNode
            node = node.nextNode

        return buf


    def extractMinimum(self):
        node = buf = self.head

        if self.head is self.tail:
            self.head = self.tail = None
            return buf

        while node.nextNode is not self.head:
            if node.nextNode < buf:
                buf = node.nextNode
                prev = node
            node = node.nextNode

        if buf is self.tail:
            self.tail = prev

        if buf is self.head:
            self.head = self.head.nextNode
            self.tail.nextNode = self.head
        else:
            prev.nextNode = buf.nextNode

        return buf


    def insert(self, node):
        if self.head is None:
            self.head = self.tail = node
            node.nextNode = node
            return

        node.nextNode = self.head
        self.head = self.tail.nextNode = node
        


    def union(self, minHeap):
        if self.head is None:
            self.head = minHeap.head
            self.tail = minHeap.tail
            minHeap.tail.nextNode = self.head
        else:
            self.tail.nextNode = minHeap.head
            self.tail = minHeap.tail
            self.tail.nextNode = self.head



    def info(self):
        if self.head:
            print(self.head.key, end = " ")
            node = self.head.nextNode
            while node is not self.head:
                print(node.key, end = " ")
                node = node.nextNode
        else:
            print("No Items")


if __name__ == '__main__':

    heap2 = Heap()

    for h in range(3):
        heap = Heap()
        for i in range(3):
            heap.insert(Node(randrange(0, 10, 1)))
        heap2.union(heap)

    heap2.info()
    print()
    print(heap2.extractMinimum(), heap2.extractMinimum(), heap2.extractMinimum(), heap2.extractMinimum())
    heap2.info()
