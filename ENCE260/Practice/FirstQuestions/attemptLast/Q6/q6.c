#include <stdio.h>

void swap3(int* x, int* y, int* z);

int main(void)
{
    int a = 10;
    int b = 0;
    int c = 7;
    swap3(&a, &b, &c);
    printf("%d <= %d <= %d\n", c, b, a);
}

void swap(int *a, int *b)
{
   int t;
   t  = *b;
   *b = *a;
   *a = t;
}

void swap3(int* x, int* y, int* z)
{
    if (*x < *y) swap(x, y);
    if (*y < *z) swap(y, z);
    if (*x < *y) swap(x, y);
}
