#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.parent = None


    def __str__(self):
        return self.key


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


def BFS(Adj, U): # в ширину
    queue = Queue()
    U.visited = True
    queue.enqueue(U)

    while queue.head:
        U = queue.dequeue()

        print(U, end = " ")

        for V in Adj[U]:
            if V.visited == False:
                V.visited = True
                queue.enqueue(V)


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

    BFS(Adj, a)
