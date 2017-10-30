#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


def insertionSort(A):
    for j in range(len(A)):
        # 先把此值保存下来，以防止被覆盖掉
        curValue = A[j]
        pos = j
        while pos > 0 and A[pos-1] > curValue:
            A[pos] = A[pos-1]
            pos = pos - 1
        A[pos] = curValue
    return A


if __name__ == '__main__':
    # define a array
    Array = [6, 4, 2, 3, 1, 10, 9, 4]
    print(Array)
    Array = insertionSort(Array)
    print(Array)
