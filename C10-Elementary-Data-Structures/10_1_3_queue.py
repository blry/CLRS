#!/usr/bin/env python
# coding=utf-8

class Queue(list):
    def __init__(self, n):
        self.tail = self.head = 0
        self.last = n - 1
        self.extend([None] * n)


    def enqueue(self, val):
        self[self.tail] = val

        if self.tail == self.last:
            self.tail = 0
        else:
            self.tail += 1


    def dequeue(self):
        val = self[self.head]

        if self.head == self.last:
            self.head = 0
        else:
            self.head += 1

        return val


if __name__ == '__main__':
    A = Queue(10)

    A.enqueue(0)
    A.enqueue(1)
    A.enqueue(2)
    A.enqueue(3)
    A.enqueue(4)
    A.enqueue(5)
    A.enqueue(6)
    A.enqueue(7)
    A.enqueue(8)
    A.enqueue(9)


    for i in range(10, 101):
        print(A.dequeue(), end = " ")
        A.enqueue(i)

    for i in range(10):
        print(A.dequeue(), end = " ")
