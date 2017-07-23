#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, data = None):
        self.data = data
        self.leftChild = self.rightChild = None


class BinaryTree():
    def __init__(self, head):
        self.head = head


    def info(self, node):
        print(node.data, end = " ")

        if node.rightChild:
            self._info(node.rightChild)
        if node.leftChild:
            self._info(node.leftChild)


if __name__ == '__main__':
    T = Node(1)
    T.leftChild = Node(2)
    T.rightChild = Node(3)
    T.leftChild.leftChild = Node(4)
    T.leftChild.rightChild = Node(5)
    T.rightChild.leftChild = Node(6)
    T.rightChild.rightChild = Node(7)

    L = BinaryTree(T)

    L.info()
