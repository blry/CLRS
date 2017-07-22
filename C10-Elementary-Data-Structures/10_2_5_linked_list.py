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


    def delete(self, item):
        if self.head is item:
            if self.tail is item:
                self.head = self.tail = None
            else:
                self.head = self.tail.nextItem = self.head.nextItem

            return

        prev = self.head

        while prev.nextItem is not item:
            prev = prev.nextItem
            if prev is self.head:
                raise Exception("Item not found")

        prev.nextItem = item.nextItem

        if item is self.tail:
            self.tail = prev


    def search(self, k):
        if not self.head:
            raise Exception("List is empty")

        buf = self.head.key

        if buf == k:
            return self.head

        self.head.key = k
        item = self.head.nextItem

        while item.key != k:
            item = item.nextItem

        self.head.key = buf

        if item is self.head:
            raise Exception("Item not found")

        return item

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