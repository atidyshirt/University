#include <stdio.h>

int* pairSumSearch(int* data, int numEls, int pairSum)
{
    for (int i = 0; i <numEls - 1; i++) {
        if (pairSum == data[i] + data[i+1]) {
            return &data[i];
        }
    }
    return NULL;
}
