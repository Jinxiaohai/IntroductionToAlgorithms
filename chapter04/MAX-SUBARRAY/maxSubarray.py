#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


def FindMaxCrossingSubarray(A, low, high):
    """
    寻找到跨越中点的最大子数组和边界点，其中两个边界点都是要的。
    """
    # 中点
    middle = (low+high) // 2

    # 左边的最大子数组
    left_sum = float('-inf')
    sum = 0
    for i in range(middle, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    # 右边的最大子数组
    right_sum = float('-inf')
    sum = 0
    for j in range(middle+1, high+1, 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum+right_sum)


def findMaximumSubarray(A, low, high):
    """
    最大子数组的递归式处理
    """

    # 递归的终止条件
    if low == high:
        return (low, high, A[low])

    else:
        # 中点
        mid = (high+low) // 2

        # 最大子数组在左边
        (leftLow, leftHigh, leftSum) = findMaximumSubarray(A, low, mid)
        # 最大子数组在右边
        (rightLow, rightHigh, rightSum) = findMaximumSubarray(A, mid+1, high)
        # 横跨中点
        (crossLow, crossHigh, crossSum) = FindMaxCrossingSubarray(A, low, high)

        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)


if __name__ == '__main__':
    A = [-4，12，6，]
    (left, right, sumValue) = findMaximumSubarray(A, 0, len(A)-1)
    print("left is : {0}, right is : {1}, Sum is : {2}".
          format(left, right, sumValue))
