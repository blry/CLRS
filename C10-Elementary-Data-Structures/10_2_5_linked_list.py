#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data
        self.nextNode = None


class LinkedList():
    def __init__(self):
        self.head = self.tail = None


    def insert(self, node):
        if self.head is None:
            self.head = self.tail = node
            node.nextNode = node
        else:
            node.nextNode = self.head
            self.head = node
            self.tail.nextNode = self.head


    def delete(self, node):
        if self.head is node:
            if self.tail is node:
                self.head = self.tail = None
            else:
                self.head = self.tail.nextNode = self.head.nextNode
            return

        prev = self.head

        while prev.nextNode is not node:
            prev = prev.nextNode
            if prev is self.head:
                raise Exception("Node not found")

        prev.nextNode = node.nextNode

        if node is self.tail:
            self.tail = prev


    def search(self, k):
        if not self.head:
            raise Exception("List is empty")

        buf = self.head.key

        if buf == k:
            return self.head

        self.head.key = k
        node = self.head.nextNode

        while node.key != k:
            node = node.nextNode

        self.head.key = buf

        if node is self.head:
            raise Exception("Node not found")

        return node


    def info(self):
        if self.head:
            print(self.head.key, end = " ")
            a = self.head.nextNode
            while a is not self.head:
                print(a.key, end = " ")
                a = a.nextNode
        else:
            print("No Nodes")


if __name__ == '__main__':
    L = LinkedList()

    L.insert(Node(10, 100))
    L.insert(Node(20, 200))
    L.insert(Node(30, 300))

    L.info()
    print()
    a = L.search(20)
    L.delete(a)
    L.info()

    try:
        L.delete(a)
    except Exception:
        print("\nException handled")

    try:
        L.search(20)
    except Exception:
        print("Exception handled")

    L.delete(L.search(10))
    L.delete(L.search(30))
    L.info()
