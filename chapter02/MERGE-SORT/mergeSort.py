#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


def merge(left, right):
    """
    归并排序的辅助函数
    """
    array = []
    left_cursor, right_cursor = 0, 0

    """
    开始收集两个子‘数组’中的元素
    """
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            array.append(left[left_cursor])
            left_cursor += 1
        else:
            array.append(right[right_cursor])
            right_cursor += 1

    """
    收集两个'数组'之中仍有残存元素的那个数组
    """
    for i in range(left_cursor, len(left)):
        array.append(left[i])
    for i in range(right_cursor, len(right)):
        array.append(right[i])

    """
    返回收集的两个子数组
    """
    return array


def mergeSort(arr):
    """
    归并排序，实施递归调用进行解决
    """
    # 处理不用排序的情况即给出递归截止的条件
    if len(arr) <= 1:
        return arr

    # 进行二分的处理
    middle = int(len(arr)/2)

    """
    进行递归的调用
    """
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    return merge(left, right)


if __name__ == '__main__':
    import random

    arr = []
    for i in range(20):
        arr.append(random.randrange(100))

    print(arr)
    arr = mergeSort(arr)
    print(arr)
