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
        self.leftChild = self.rightChild = None


class BinaryTree():
    def __init__(self, head):
        self.head = head


    def info(self):
        stack = Stack()
        stack.push(self.head)
        
        while stack.head:
            node = stack.pop()
                
            print(node.data, end = " ")
                
            if node.leftChild:
                stack.push(node.leftChild)
            if node.rightChild:
                stack.push(node.rightChild)



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
    