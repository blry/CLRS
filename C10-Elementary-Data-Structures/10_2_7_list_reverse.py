#!/usr/bin/env python
# coding=utf-8


class Item():
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data
        self.nextItem = None


class LinkedList():
    def __init__(self):
        self.head = self.tail = None


    def insert(self, item):
        if self.head is None:
            self.head = self.tail = item
            item.nextItem = item
        else:
            item.nextItem = self.head
            self.head = item
            self.tail.nextItem = self.head


    def reverse(self):
        prevItem = self.tail = self.head
        buf = self.head.nextItem
        # 3 -> 2 -> 1 -> 3; p3; b2;

        while buf is not self.head:
            nextItem = buf.nextItem
            buf.nextItem = prevItem
            prevItem = buf
            buf = nextItem
            # n1; 2 -> 3; p2; b1;
            # n3; 1 -> 2; p1; b3;

        self.head = self.tail.nextItem = prevItem


    def info(self):
        if self.head:
            print(self.head.key, end = " ")
            a = self.head.nextItem
            while a is not self.head:
                print(a.key, end = " ")
                a = a.nextItem
        else:
            print("No Items")


if __name__ == '__main__':
    L = LinkedList()

    L.insert(Item(10, 100))
    L.insert(Item(20, 200))
    L.insert(Item(30, 300))

    L.info()
    print()
    L.reverse()

    L.info()
    