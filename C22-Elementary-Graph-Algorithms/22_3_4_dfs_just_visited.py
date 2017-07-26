#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.parent = None

    def __str__(self):
        return self.key


def DFS(Adj, U):
    U.visited = True

    print(U, end = " ")

    for V in Adj[U]:
        if V.visited == False:
            DFS(Adj, V)


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
