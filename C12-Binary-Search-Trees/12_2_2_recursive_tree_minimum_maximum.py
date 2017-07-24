#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, data = None):
        self.data = data
        self.leftChild = self.rightChild = None


def minimum(node):
    if node.leftChild:
        return minimum(node.leftChild)
    return node


def maximum(node):
    if node.rightChild:
        return maximum(node.rightChild)
    return node


if __name__ == '__main__':
    # level 1
    T = Node(6)
    
    T.leftChild = Node(5)
    T.leftChild.leftChild = Node(2)
    T.leftChild.rightChild = Node(5)

    T.rightChild = Node(7)
    T.rightChild.rightChild = Node(8)

    print("Minimum:  " + str(minimum(T).data))
    print("Maximum:  " + str(maximum(T).data))
