#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.parent = None

    def __str__(self):
        return self.key


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


def DFS(Adj, U):
    stack = Stack()
    U.visited = True
    stack.push(U)

    while stack.head:
        U = stack.pop()

        print(U, end = " ")

        for V in Adj[U][::-1]:
            if V.visited == False:
                V.visited = True
                stack.push(V)


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    m = Node('m')
    k = Node('k')

    Adj = {
        a: (b, d, e, c), 
        b: (a, d, e), 
        c: (a, f, g),
        d: (a, b, e), 
        e: (a, b, d), 
        f: (c, g), 
        g: (c, f, m), 
        m: (g, k), 
        k: (m, )
    }

    DFS(Adj, a)
