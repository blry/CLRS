#!/usr/bin/env python
# coding=utf-8


class Item():
    def __init__(self, key = None):
        self.key = key


class Queue():
    def __init__(self):
        self.head = self.tail = None


    def enqueue(self, item):
        item.nextItem = None

        if self.head is None:
            self.head = self.tail = item
        else:
            self.tail.nextItem = item
            self.tail = item


    def dequeue(self):
        if self.head is None:
            raise Exception("Queue underflow")

        item = self.head
        self.head = item.nextItem

        return item


if __name__ == '__main__':
    A = Queue()

    for i in range(10):
        A.enqueue(Item(i))
        A.dequeue()
        A.enqueue(Item(i))

    for i in range(11):
        try:
            print(A.dequeue().key, end = " ")
        except Exception:
            print()
            print("Underflow catched")
            break
