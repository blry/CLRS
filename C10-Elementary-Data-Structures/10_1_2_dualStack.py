#!/usr/bin/env python
# coding=utf-8

class dualStack(list):
    def __init__(self, n):
        self.top1 = -1
        self.top2 = self.n = n
        self.extend([None] * n)

    def push1(self, val):
        if (self.top1 + 1) == self.top2:
            raise Exception("Stack overflow")

        self.top1 += 1
        self[self.top1] = val

    def pop1(self):
        if self.top1 == -1:
            raise Exception("Stack1 underflow")

        self.top1 -= 1
        return self[self.top1 + 1]
        

    def push2(self, val):
        if self.top1 == (self.top2 - 1):
            raise Exception("Stack overflow")

        self.top2 -= 1
        self[self.top2] = val


    def pop2(self):
        if self.top2 == self.n:
            raise Exception("Stack2 underflow")

        self.top2 += 1
        return self[self.top2 - 1]

if __name__ == '__main__':
    A = dualStack(10)

    A.push1(1)
    A.push1(1)
    A.push1(1)
    A.push2(2)
    A.push1(1)
    A.push2(2)
    A.push1(1)

    while True:
        try:
            A.push2(2)
        except Exception:
            print("Stack2 overflow exception handled")
            break

    while True:
        try:
            A.push1(1)
        except Exception:
            print("Stack1 overflow exception handled")
            break

    while True:
        try:
            print(A.pop1(), end = ", ")
        except Exception:
            print("Stack1 underflow exception handled")
            break

    while True:
        try:
            print(A.pop2(), end = ", ")
        except Exception:
            print("Stack2 underflow exception handled")
            break
