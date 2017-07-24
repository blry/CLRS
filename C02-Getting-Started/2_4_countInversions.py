#!/usr/bin/env python
# coding=utf-8

import math


class InversionsCounter:
    def __init__(self, A):
        self.D = A
        self.B = [None] * len(A)


    def getData(self):
        return self.D


    def count(self):
        return self.__sort(0, len(self.D) - 1)


    def __sort(self, low, high):
        if(low < high):
            mid = (low + high) // 2
            inversions = self.__sort(low, mid)
            inversions += self.__sort(mid + 1, high)
            inversions += self.__merge(low, mid, high)
            return inversions
        return 0


    def __merge(self, low, mid, high):
        self.B[low : mid + 1] = self.D[low : mid + 1]
        self.B[mid + 1] = math.inf

        mid += 1
        inversions = 0
        
        for i in range(low, high + 1):
            if(mid > high or self.B[low] <= self.D[mid]):
                self.D[i] = self.B[low]
                low += 1
            elif(self.B[low] > self.D[mid]):
                self.D[i] = self.D[mid]
                mid += 1
                inversions += mid - i - 1
        return inversions


if __name__ == '__main__':
    print(InversionsCounter([2, 3, 8, 6, 1]).count()) # 5
