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
            return None

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

        node = self.head
        
        while True: # 6
            while node:
                stack.push(node)
                node = node.leftChild

            if stack.head:
                node = stack.pop()
                print(node.data, end = " ")
                node = node.rightChild
            else:
                break


if __name__ == '__main__':
    # level 1
    T = Node(6)
    
    T.leftChild = Node(5)
    T.leftChild.leftChild = Node(2)
    T.leftChild.rightChild = Node(5)

    T.rightChild = Node(7)
    T.rightChild.rightChild = Node(8)


    L = BinaryTree(T)

    L.info()
    