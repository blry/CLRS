#!/usr/bin/env python
# coding=utf-8

from random import randrange, uniform

class L(list):
    def __init__(self, A):
        self.extend(A)
        self.len = len(A)
        self.optimalSize = self.optimalSize()
        self.cache = {}
        


    def optimalSize(self):
        optimal, k = 0, 0

        for i in range(1, self.len):
            if (self[i] / i) > k:
                k = self[i] / i
                optimal = i

        return optimal


    def getSizesOptimized(self, n):
        left = [0, []]

        while n >= self.len:
            left[0] += self[self.optimalSize]
            left[1] += [self.optimalSize]
            n -= self.optimalSize

        remains = self.getSizes(n)

        return left[0] + remains[0], left[1] + remains[1]


    def getSizes(self, n):
        if n in self.cache:
            return self.cache[n]

        maxPrice = 0
        parts = []

        for size in range(n, 0, -1):
            maxOfRemainsPart = self.getSizes(n - size)

            currentPrice = maxOfRemainsPart[0]

            if size < self.len:
                currentPrice += self[size]

            if currentPrice > maxPrice:
                maxPrice, parts = currentPrice, [size] + maxOfRemainsPart[1]

        self.cache[n] = maxPrice, parts

        return self.cache[n]


if __name__ == '__main__':
    for i in range(100, 120):
        prices = [0, 1]
        k = uniform(3, 4)
        for j in range(1, randrange(7, 14)):
            prices.append(int(k * j))
            k = abs(uniform(k - 3, k + 3))

        T = L(prices)

        k1 = T.getSizes(i)
        k2 = T.getSizesOptimized(i)

        if k1[0] != k2[0]:
            print("Size:", i, " Prices: ", prices)
            print("Full:     ", k1)
            print("Optimized:", k2)
            print()
