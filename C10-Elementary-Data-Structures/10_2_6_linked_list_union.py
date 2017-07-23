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


    def union(self, L):
        self.tail.nextItem = L.head
        L.tail.nextItem = self.head


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

    L2 = LinkedList()

    L2.insert(Item(40, 400))
    L2.insert(Item(50, 500))
    L2.insert(Item(60, 600))

    L.union(L2)

    L.info()
    