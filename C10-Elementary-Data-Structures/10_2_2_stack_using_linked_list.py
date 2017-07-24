#!/usr/bin/env python
# coding=utf-8


class Item():
    def __init__(self, key = None):
        self.key = key
        self.nextItem = None


class Stack():
    def __init__(self):
        self.head = None


    def push(self, item):
        if self.head is None:
            item.nextItem = None
            self.head = item
        else:
            item.nextItem = self.head
            self.head = item


    def pop(self):
        if self.head is None:
            raise Exception("Stack underflow")

        item = self.head
        self.head = item.nextItem

        return item


if __name__ == '__main__':
    A = Stack()
    for i in range(10):
        A.push(Item(i))

    for i in range(11):
        try:
            print(A.pop().key, end = " ")
        except Exception:
            print("\nStack underflow exception handled")
