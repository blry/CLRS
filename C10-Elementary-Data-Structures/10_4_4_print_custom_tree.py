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
        self.leftChild = self.rightSibling = None


class CustomTree():
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
            if node.rightSibling:
                stack.push(node.rightSibling)



if __name__ == '__main__':
    # level 1
    T = Node(1)

    # level 2
    T.leftChild = Node(2)
    T.leftChild.rightSibling = Node(3) 

    # level 3
    T.leftChild.leftChild = Node(4)
    T.leftChild.leftChild.rightSibling = Node(5)
    T.leftChild.leftChild.rightSibling.rightSibling = Node(6)
    T.leftChild.leftChild.rightSibling.rightSibling.rightSibling = Node(7)

    L = CustomTree(T)

    L.info()
    