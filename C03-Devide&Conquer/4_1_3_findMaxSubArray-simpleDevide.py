#!/usr/bin/env python
# coding=utf-8

def findMaxSubArray(A, low, high):  # 30nlog20n;
    if low >= high:
        return A[high], low, high
    else:
        mid = (high + low) // 2
        
        leftSum, leftLow, leftHigh = findMaxSubArray(A, low, mid)
        rightSum, rightLow, rightHigh = findMaxSubArray(A, mid + 1, high)
        crossSum, crossLow, crossHigh = findMaxCrossMidSubArray(A, low, mid, high)

        if (leftSum >= rightSum) and (leftSum >= crossSum):
            return leftSum, leftLow, leftHigh
        elif (rightSum >= leftSum) and (rightSum >= crossSum):
            return rightSum, rightLow, rightHigh
        else:
            return crossSum, crossLow, crossHigh

def findMaxCrossMidSubArray(A, low, mid, high):
    maxLeftSum = current = A[mid]
    leftLow = mid

    for i in range(mid - 1, low - 1, -1):
        current += A[i]
        if current > maxLeftSum:
            maxLeftSum = current
            leftLow = i
        
    maxRightSum = current = A[mid + 1]
    rightHigh = mid + 1

    for i in range(mid + 2, high):
        current += A[i]
        if current > maxRightSum:
            maxRightSum = current
            rightHigh = i

    return maxRightSum + maxLeftSum, leftLow, rightHigh


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    b, i, j = findMaxSubArray(A, 0, len(A) - 1)
    print(b, [i, j], A[i:j + 1])
