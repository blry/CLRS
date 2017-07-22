#!/usr/bin/env python
# coding=utf-8

class Stack(list):
    def __init__(self, n):
        self.top = -1
        self.n = n
        self.extend([None] * n)


    def push(self, val):
        if (self.top + 1) == self.n:
            raise Exception("Stack overflow")

        self.top += 1
        self[self.top] = val


    def pop(self):
        if self.top == -1:
            raise Exception("Stack underflow")

        self.top -= 1
        return self[self.top + 1]


class Queue():
    def __init__(self, n):
        self.tail = 0
        self.head = None
        self.last = n - 1
        self.st1 = Stack(n)
        self.st2 = Stack(n)


    def enqueue(self, val):
        if self.head == self.tail:
            raise Exception("Queue overflow")

        self.st2.push(val)

        if self.head is None:
            self.head = self.tail

        if self.tail == self.last:
            self.tail = 0
        else:
            self.tail += 1


    def dequeue(self):
        if self.head is None:
            raise Exception("Queue underflow")

        try:
            val = self.st1.pop()
        except Exception:
            for i in range(self.st2.top + 1):
                self.st1.push(self.st2.pop())

            val = self.st1.pop()

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
