#!/usr/bin/env python
# coding=utf-8

def findMaxSubArray(A):
    maxSum = low = high = 0
    for l in range(0, len(A)):
        current = 0
        for r in range(l, len(A)):
            current += A[r]
            if current > maxSum:
                maxSum = current
                low = l
                high = r
    return maxSum, low, high


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7] 

b, i, j = findMaxSubArray(A)
print(b, [i, j], A[i:j + 1])