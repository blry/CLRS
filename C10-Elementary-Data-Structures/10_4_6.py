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
        self.lastSibling = False # if it is lastSibling then pointer points to his parent
        self.leftChild = self.pointer = None


class CustomTree():
    def __init__(self, head):
        self.head = head


    def info(self):
        stack = Stack()
        stack.push(self.head)
        
        while stack.head:
            node = stack.pop()
                
            print(str(node.data) + "[" + (str(self.parent(node).data) if node.pointer else '') + "]", end = " ")
                
            if node.leftChild:
                stack.push(node.leftChild)
            if node.pointer and not node.lastSibling:
                stack.push(node.pointer)

    def parent(self, node):
        while node.lastSibling == False:
            node = node.pointer

        return node.pointer

    def children(self, node):
        children = []
        if node.leftChild:
            node = node.leftChild
            children.append(node)
            while node.lastSibling == False:
                node = node.pointer
                children.append(node)

        return children





if __name__ == '__main__':
    # level 1
    T = Node(1)
    T.lastSibling = True

    # level 2
    T.leftChild = Node(2)
    T.leftChild.pointer = Node(3)
    T.leftChild.pointer.lastSibling = True
    T.leftChild.pointer.pointer = T
    
    # level 3
    T.leftChild.leftChild = Node(4)
    T.leftChild.leftChild.pointer = Node(5)
    T.leftChild.leftChild.pointer.lastSibling = True
    T.leftChild.leftChild.pointer.pointer = T.leftChild

    T.leftChild.pointer.leftChild = Node(6)
    T.leftChild.pointer.leftChild.pointer = Node(7)
    T.leftChild.pointer.leftChild.pointer.lastSibling = True
    T.leftChild.pointer.leftChild.pointer.pointer = T.leftChild.pointer


    L = CustomTree(T)

    L.info()
    print()
    
    for node in L.children(T):
        print(node.data, end = " ")
    print()

    for node in L.children(T.leftChild):
        print(node.data, end = " ")
    print()

    for node in L.children(T.leftChild.pointer):
        print(node.data, end = " ")
    print()