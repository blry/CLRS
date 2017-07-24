#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, data = None):
        self.data = data
        self.leftChild = self.rightChild = None


def preorder(node):
    if node:
        print(node.data, end = " ")
        preorder(node.leftChild)
        preorder(node.rightChild)


def inorder(node):
    if node:
        inorder(node.leftChild)
        print(node.data, end = " ")
        inorder(node.rightChild)
        

def postorder(node):
    if node:
        postorder(node.leftChild)
        postorder(node.rightChild)
        print(node.data, end = " ")


if __name__ == '__main__':
    # level 1
    T = Node(6)
    
    T.leftChild = Node(5)
    T.leftChild.leftChild = Node(2)
    T.leftChild.rightChild = Node(5)

    T.rightChild = Node(7)
    T.rightChild.rightChild = Node(8)

    print("Preorder:  ", end = " ")
    preorder(T)
    print("\nInorder:   ", end = " ")
    inorder(T)
    print("\nPostorder: ", end = " ")
    postorder(T)
