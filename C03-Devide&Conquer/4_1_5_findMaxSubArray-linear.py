#!/usr/bin/env python
# coding=utf-8
# 1..j, отслеживая макс подмассив
# потом для 1..j+1 -это либо 1..j, либо i..j+1


def findMaxSubArray(A):
    right = left = 0
    maxSum = A[0]

    temp_sum = 0
    temp_left = 0
    for i in range(0, len(A)):
        temp_sum = max(A[i], temp_sum + A[i])
        if temp_sum > maxSum:
            maxSum = temp_sum
            right = i
            left = temp_left
        if temp_sum == A[i]:
            temp_left = i
    return maxSum, left, right


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    b, i, j = findMaxSubArray(A)
    print(b, [i, j], A[i:j + 1])
