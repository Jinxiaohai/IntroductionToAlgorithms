#include <iostream>
#include "Head.h"

using namespace std;

int main(int argc, char *argv[])
{
  double A[5] = {1, 2, 3., 4., 5};
  quickSort(A, 0, 4);
  for (int i = 0; i != 5; ++i)
    {
      cout << A[i] << endl;
    }
  return 0;
}
