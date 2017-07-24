#!/usr/bin/env python
# coding=utf-8


class Queue(list):
    def __init__(self, n):
        self.tail = 0
        self.head = None
        self.last = n - 1
        self.extend([None] * n)


    def enqueue(self, val):
        if self.head == self.tail:
            raise Exception("Queue overflow")

        self[self.tail] = val

        if self.head is None:
            self.head = self.tail

        if self.tail == self.last:
            self.tail = 0
        else:
            self.tail += 1


    def dequeue(self):
        if self.head is None:
            raise Exception("Queue underflow")

        val = self[self.head]

        if self.head == self.last:
            self.head = 0
        else:
            self.head += 1

        if self.head == self.tail:
            self.head = None

        return val


if __name__ == '__main__':
    A = Queue(10)

    for i in range(11):
        try:
            A.enqueue(i)
        except Exception:
            print("Overflow catched")
            break

    for i in range(11):
        try:
            print(A.dequeue(), end = " ")
            A.enqueue(i)
            print(A.dequeue(), end = " ")
        except Exception:
            print()
            print("Underflow catched")
            break
