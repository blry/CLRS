#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, data = None):
        self.data = data
        self.leftChild = self.rightChild = self.parent = None


def maximum(node):
    if node.rightChild:
        return maximum(node.rightChild)
    return node


def predecessor(node):
    if node.leftChild:
        return maximum(node.leftChild)

    y = node.parent
    while y and node is y.leftChild:
        node = y
        y = y.parent

    return y


if __name__ == '__main__':
    T = Node(6)
    
    T.leftChild = Node(5)
    T.leftChild.parent = T
    
    T.leftChild.leftChild = Node(2)
    T.leftChild.leftChild.parent = T.leftChild

    T.leftChild.rightChild = Node(5)
    T.leftChild.rightChild.parent = T.leftChild

    T.rightChild = Node(7)
    T.rightChild.parent = T
    T.rightChild.rightChild = Node(8)
    T.rightChild.rightChild.parent = T.rightChild

    print(predecessor(T.rightChild).data)
    print(predecessor(T.rightChild.rightChild).data)
    print(predecessor(T.leftChild.leftChild))
