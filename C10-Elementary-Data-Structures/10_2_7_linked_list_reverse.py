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


    def reverse(self):
        prevNode = self.tail = self.head
        buf = self.head.nextNode
        # 3 -> 2 -> 1 -> 3; p3; b2;

        while buf is not self.head:
            nextNode = buf.nextNode
            buf.nextNode = prevNode
            prevNode = buf
            buf = nextNode
            # n1; 2 -> 3; p2; b1;
            # n3; 1 -> 2; p1; b3;

        self.head = self.tail.nextNode = prevNode


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
    L.reverse()

    L.info()
