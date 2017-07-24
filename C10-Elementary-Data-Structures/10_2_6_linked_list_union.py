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


    def union(self, L):
        self.tail.nextNode = L.head
        L.tail.nextNode = self.head


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

    L2 = LinkedList()

    L2.insert(Node(40, 400))
    L2.insert(Node(50, 500))
    L2.insert(Node(60, 600))

    L.union(L2)

    L.info()
