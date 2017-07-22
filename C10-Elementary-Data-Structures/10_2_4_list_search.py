#!/usr/bin/env python
# coding=utf-8

class Item():
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data

class LinkedList():
    def __init__(self):
        self.nil = Item()
        self.nil.prevItem = self.nil
        self.nil.nextItem = self.nil


    def insert(self, item):
        item.nextItem = self.nil.nextItem
        self.nil.nextItem.prevItem = item
        self.nil.nextItem = item
        item.prevItem = self.nil

    def delete(self, item):
        item.prevItem.nextItem = item.nextItem
        item.nextItem.prevItem = item.prevItem


    def search(self, k):
        item = self.nil.nextItem

        self.nil.key = k

        while item.key != k:
            item = item.nextItem

        self.nil.key = None

        if item is self.nil:
            raise Exception("Not Found")

        return item


if __name__ == '__main__':
    L = LinkedList()

    L.insert(Item(10, 100))
    L.insert(Item(11, 111))
    L.insert(Item(12, 111))
    print(L.search(12).nextItem.key)
    L.delete(L.search(12))

    try:
        print(L.search(12).data)
    except Exception:
        print("Exception handled")