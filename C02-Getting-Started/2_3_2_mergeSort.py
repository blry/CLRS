#!/usr/bin/env python
# coding=utf-8

import math

class MergeSorter:
    def __init__(self, A):
        self.D = A
        self.B = [None] * len(A)

    def getData(self):
        return self.D

    def sort(self):
        self.__sort(0, len(self.D) - 1)
        return self.D

    def __sort(self, low, high):
        if(low < high):
            mid = (low + high) // 2
            self.__sort(low, mid)
            self.__sort(mid + 1, high)
            self.__merge(low, mid, high)

    def __merge(self, low, mid, high):
        self.B[low : mid + 1] = self.D[low : mid + 1]
        self.B[mid + 1] = math.inf
        mid += 1
        for i in range(low, high + 1):
            if(mid > high or self.B[low] <= self.D[mid]):
                self.D[i] = self.B[low]
                low += 1
            elif(self.B[low] > self.D[mid]):
                self.D[i] = self.D[mid]
                mid += 1


if __name__ == '__main__':
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 100, -100, 100, -100, -1000]

    MergeSorter(A).sort()

    print(A)