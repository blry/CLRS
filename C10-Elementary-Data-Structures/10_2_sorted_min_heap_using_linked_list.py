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


class SortedMinHeap():
    def __init__(self):
        self.head = self.tail = None


    def minimum(self):
        return self.head


    def extractMinimum(self):
        node = self.head

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.tail.nextNode = self.head.nextNode

        return node


    def insert(self, node):
        if self.head is None:
            self.head = self.tail = node
            node.nextNode = node
            return
        elif node < self.head:
            node.nextNode = self.head
            self.head = self.tail.nextNode = node
            return

        k = self.tail.key
        self.tail.key = node.key + 1
            
        prev = self.head

        while prev.nextNode < node:
            prev = prev.nextNode

        self.tail.key = k

        if (prev.nextNode is self.tail) and (k <= node.key):            
            self.tail.nextNode = node
            self.tail = node
            node.nextNode = self.head
        else:
            node.nextNode = prev.nextNode
            prev.nextNode = node


    def union(self, sortedMinHeap):
        if self.head is None:
            self.head = sortedMinHeap.head
            self.tail = sortedMinHeap.tail
            return

        node = sortedMinHeap.head

        if node < self.head:
            buf = node.nextNode
            node.nextNode = self.head
            self.head = self.tail.nextNode = node
            node = buf

            if node is sortedMinHeap.head:
                return

        prev = self.head

        while prev.nextNode is not self.head:
            if node < prev.nextNode:
                buf = node.nextNode
                node.nextNode = prev.nextNode
                prev.nextNode = node
                node = buf

                if node is sortedMinHeap.head:
                    return

            prev = prev.nextNode

        if prev.nextNode is self.head:
            prev.nextNode = node
            self.tail = sortedMinHeap.tail
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

    heap2 = SortedMinHeap()

    for h in range(10):
        heap = SortedMinHeap()
        for i in range(3):
            heap.insert(Node(randrange(0, 10, 3)))
        heap2.union(heap)

    heap2.info()
