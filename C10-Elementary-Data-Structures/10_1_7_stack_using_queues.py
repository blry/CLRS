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


class Stack():
    def __init__(self, n):
        self.top = -1
        self.n = n
        self.q1 = Queue(n)
        self.q2 = Queue(n)


    def push(self, val):
        if (self.top + 1) == self.n:
            raise Exception("Stack overflow")

        self.top += 1
        self.q2.enqueue(val)


    def pop(self):
        if self.top == -1:
            raise Exception("Stack underflow")

        self.top -= 1
        try:
            val = self.q1.dequeue(val)
        except Exception:
            for i in range(self.q2.last + self.q2.tail - self.q2.head):
                self.q1.enqueue(self.q2.dequeue())
            val = self.q1.dequeue()

        return val


if __name__ == '__main__':
    A = Stack(10)
    A.push(1)
    A.push(1)
    A.push(1)
    A.push(2)
    A.push(1)
    A.push(2)
    A.push(1)

    while True:
        try:
            A.push(2)
        except Exception:
            print("Stack overflow exception handled")
            break

    while True:
        try:
            print(A.pop(), end = " ")
        except Exception:
            print("\nStack underflow exception handled")
            break
