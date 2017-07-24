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
                return None

        prev.nextNode = node.nextNode

        if node is self.tail:
            self.tail = prev


    def search(self, k):
        if not self.head:
            return None

        buf = self.head.key

        if buf == k:
            return self.head

        self.head.key = k
        node = self.head.nextNode

        while node.key != k:
            node = node.nextNode

        self.head.key = buf

        if node is self.head:
            return None

        return node


    def info(self):
        if self.head:
            print(self.head.key, end = " ")
            node = self.head.nextNode
            while node is not self.head:
                print(node.key, end = " ")
                node = node.nextNode
        else:
            print("No Items", end = " ")


def insert(node):
    global array
    array[h(node.key)].insert(node)


def delete(node):
    global array
    array[h(node.key)].delete(node)


def search(k):
    global array
    return array[h(k)].search(k)


def h(k):
    return k % 9


if __name__ == '__main__':
    array = [LinkedList() for _ in range(10)]

    insert(Node(5, 100))
    insert(Node(28, 200))
    insert(Node(19, 100))
    insert(Node(15, 200))
    insert(Node(20, 100))
    insert(Node(33, 200))
    insert(Node(12, 100))
    insert(Node(17, 200))
    insert(Node(10, 100))

    for i in range(10):
        print(i, end = ": ")
        array[i].info()
        print()
