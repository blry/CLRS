#!/usr/bin/env python
# coding=utf-8


class Node():
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data


class LinkedList():
    def __init__(self):
        self.nil = Node()
        self.nil.prevNode = self.nil
        self.nil.nextNode = self.nil


    def insert(self, node):
        node.nextNode = self.nil.nextNode
        self.nil.nextNode.prevNode = node
        self.nil.nextNode = node
        node.prevNode = self.nil

    def delete(self, node):
        node.prevNode.nextNode = node.nextNode
        node.nextNode.prevNode = node.prevNode


    def search(self, k):
        node = self.nil.nextNode

        self.nil.key = k

        while node.key != k:
            node = node.nextNode

        self.nil.key = None

        if node is self.nil:
            raise Exception("Not Found")

        return node


if __name__ == '__main__':
    L = LinkedList()

    L.insert(Node(10, 100))
    L.insert(Node(11, 111))
    L.insert(Node(12, 111))
    print(L.search(12).nextNode.key)
    L.delete(L.search(12))

    try:
        print(L.search(12).data)
    except Exception:
        print("Exception handled")
