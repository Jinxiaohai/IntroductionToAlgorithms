////////////////////////////////////////////////////////////////////////
/// COPYRIGHT NOTICE
/// COPYRIGHT (c) 2017, 金小海
/// All rights reserved.
///
/// @file    quickSort.cpp
/// @version 1.0
/// @author  xiaohai <xiaohaijin@outlook.com>
/// @date    Thu Nov 16 20:31:02 2017
///
/// @brief   该文件实现快度排序。
///
/// 修订说明:最初版本
////////////////////////////////////////////////////////////////////////
#ifndef HEAD_H
#define HEAD_H

template <typename T>
void quickSort(T *A, int first, int last);
template <typename T>
int partition(T *A, int first, int last);

/**
 * @param A : 待排序数组
 * @param first : 起始
 * @param last : 终止
 */
template <typename T>
void quickSort(T *A, int first, int last)
{
  if (first < last)
    {
      int pivotElement = partition(A, first, last);
      quickSort(A, first, pivotElement-1);
      quickSort(A, pivotElement+1, last);
    }
} ///< template

/**
 * 实现函数的部分有序化
 *
 * @param A : 待排数组
 * @param first : 起始
 * @param last : 终止
 *
 * @return : 主元的位置
 */
template <typename T>
int partition(T *A, int first, int last)
{
  T x = A[last];
  int i = first - 1;

  for (int j = first; j != last-1; ++j)
    {
      if (A[j] <= x)
	{
	  ++i;
	  T temp;
	  temp = A[i];
	  A[i] = A[j];
	  A[j] = temp;
	}
    }
  T tempVaule;
  tempVaule = A[last];
  A[last] = A[i+1];
  A[i+1] = tempVaule;
  return i+1;
} ///< template


#endif /* HEAD_H */
