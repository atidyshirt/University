#include <stdio.h>

int main(void)
{
  int i = 1;
  int j = 10;
  int k = 100;
  i = j = k = 1;
  printf("%d, %d, %d,\n", i, j, k);
  i = 1;
  j = 10;
  k = 100;
  i = j++ + k++;
  printf("%d, %d, %d,\n", i, j, k);
  i = 1;
  j = 10;
  k = 100;  
  i = ++j + ++k;
  printf("%d, %d, %d,\n", i, j, k);
  i = 1;
  j = 10;
  k = 100;  
  i = j = k;
  printf("%d, %d, %d,\n", i, j, k);
    i = 1;
  j = 10;
  k = 100;
  j = k = i;
  printf("%d, %d, %d,\n", i, j, k);
  i = 1;
  j = 10;
  k = 100;
  i = ++j + k--;
  printf("%d, %d, %d,\n", i, j, k);
  i = 1;
  j = 10;
  k = 100;
  i = ++j + --k;
  printf("%d, %d, %d,\n", i, j, k);
}
