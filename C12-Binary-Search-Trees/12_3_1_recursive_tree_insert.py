#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, key = None):
        self.key = key
        self.leftChild = self.rightChild = self.parent = None


def insert(node, z, p = None):
    if node:
        if z.key < node.key:
            insert(node.leftChild, z, node if not node.leftChild else None)
        else:
            insert(node.rightChild, z, node if not node.rightChild else None)
    else:
        z.parent = p

        if z.key < p.key:
            p.leftChild = z
        else:
            p.rightChild = z


if __name__ == '__main__':
    T = Node(6)
    
    insert(T, Node(2))
    insert(T, Node(3))
    insert(T, Node(4))
    insert(T, Node(7))
    insert(T, Node(6))
    insert(T, Node(5))

    print(T.leftChild.rightChild.rightChild.rightChild.key)
