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

def binSearch(A, x):
    start, end = 0, len(A) - 1

    while(start <= end):
        mid = (start + end) // 2

        if(A[mid] < x):
            start = mid + 1
        elif(A[mid] > x):
            end = mid - 1
        else:
            return mid

    return None

def sumCanBe(S, x):
    MergeSorter(S).sort()

    for i in range(0, len(S) - 1):
        t = S.pop(i)
        if binSearch(S, x - t) is not None:
            S.insert(i, t)
            return True
        S.insert(i, t)

    return False


if __name__ == '__main__':
    S = [1, 2, 3, 6, 7, 8]

    print(sumCanBe(S, 3)) #True
    print(sumCanBe(S, 2)) #False
