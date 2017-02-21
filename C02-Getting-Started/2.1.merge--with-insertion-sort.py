#!/usr/bin/env python
# coding=utf-8

import math

class MergeWithInsertionSorter:
    def __init__(self, A, k):
        self.D = A
        self.B = [None] * len(A)
        self.k = k

    def getData(self):
        return self.D

    def sort(self):
        self.__sort(0, len(self.D) - 1)
        return self.D

    def __sort(self, low, high):
        if(low < high):
            if((high - low) <= self.k):
                self.D[low : high + 1] = self.__insertionSort(self.D[low : high + 1])
            else:
                mid = (low + high) // 2
                self.__sort(low, mid)
                self.__sort(mid + 1, high)
                self.__merge(low, mid, high)

    def __insertionSort(self, A):
        for i in range(1, len(A)):
            k = A[i]
            j = i - 1
            while(j >= 0 and A[j] > k):
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = k

        return A

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

A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 100, -100, 100, -100, -1000]

MergeWithInsertionSorter(A, 32).sort()