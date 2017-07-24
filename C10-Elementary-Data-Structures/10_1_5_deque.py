#!/usr/bin/env python
# coding=utf-8


class Deque(list):
    def __init__(self, n):
        self.tail = 0
        self.head = None
        self.last = n - 1
        self.extend([None] * n)


    def append(self, val):
        if self.head == self.tail:
            raise Exception("Queue overflow")

        self[self.tail] = val

        if self.head is None:
            self.head = self.tail

        if self.tail == self.last:
            self.tail = 0
        else:
            self.tail += 1


    def appendLeft(self, val):
        if self.head == self.tail:
            raise Exception("Queue overflow")

        if self.head is None:
            self.head = self.tail

        if self.head == 0:
            self.head = self.last
        else:
            self.head -= 1

        self[self.head] = val


    def popLeft(self):
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


    def pop(self):
        if self.head is None:
            raise Exception("Queue underflow")

        if self.tail == 0:
            self.tail = self.last
        else:
            self.tail -= 1

        val = self[self.tail]

        if self.head == self.tail:
            self.head = None

        return val


if __name__ == '__main__':
    A = Deque(10)

    for i in range(6):
        try:
            A.append(i)
            A.appendLeft(9 - i)
        except Exception:
            print("Overflow catched")
            break

    for i in range(11):
        try:
            print(A.popLeft(), end = " ")
        except Exception:
            print()
            print("Underflow catched")
            break
