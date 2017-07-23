#!/usr/bin/env python
# coding=utf-8

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


class Node():
    def __init__(self, data = None):
        self.data = data
        self.parent = self.leftChild = self.rightChild = None


class BinaryTree():
    def __init__(self, head):
        self.head = head


    def info(self):
        node = self.head
        prev = None

        while node:
            if prev is node.parent:
                print(node.data, end = " ")
                prev = node
                node = node.leftChild or node.rightChild or node.parent
            elif prev is node.leftChild and node.rightChild:
                prev = node
                node = node.rightChild
            else:
                prev = node
                node = node.parent


if __name__ == '__main__':
    T = Node(1)

    T.leftChild = Node(2)
    T.leftChild.parent = T

    T.rightChild = Node(3)
    T.rightChild.parent = T

    T.leftChild.leftChild = Node(4)
    T.leftChild.leftChild.parent = T.leftChild

    T.leftChild.rightChild = Node(5)
    T.leftChild.rightChild.parent = T.leftChild

    T.rightChild.leftChild = Node(6)
    T.rightChild.leftChild.parent = T.rightChild

    T.rightChild.rightChild = Node(7)
    T.rightChild.rightChild.parent = T.rightChild

    L = BinaryTree(T)

    L.info()
    