#include <stdio.h>

void swap3(int* x, int* y, int* z)
{
    int flagMiddle = 0;
    int flagLast = 0;
    int flagSmallest = 0;
    if (*x < *y && *x < *z) {
        flagSmallest = *x;
        if (*y < *z) {
            flagMiddle = *y;
            flagLast = *z;
        } else {
            flagMiddle = *z;
            flagLast = *y;
        }
    }
    else if (*y < *x && *y < *z) {
        flagSmallest = *y;
        if (*x < *z) {
            flagMiddle = *x;
            flagLast = *z;
        } else {
            flagMiddle = *z;
            flagLast = *x;
        }
    }
    else if (*z < *y && *z < *x) {
        flagSmallest = *z;
        if (*x < *y) {
            flagMiddle = *x;
            flagLast = *y;
        } else {
            flagMiddle = *y;
            flagLast = *x;
        }
    }
    *z = flagSmallest;
    *y = flagMiddle;
    *x = flagLast;
}

int main(void)
{
    int a = 10;
    int b = 0;
    int c = 7;
    swap3(&a, &b, &c);
    printf("%d <= %d <= %d\n", c, b, a);
}
