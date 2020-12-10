#include <stdio.h>

int* pairSumSearch(int* data, int numEls, int pairSum)
{
    int i = 0, j = 1;
    for (i = 0; i < numEls; i++) {
        if ((data[i] + data[j]) == pairSum) {
            return &(data[i]);
        }
        j++;
    }
    return NULL;
}

int main(void)
{
    int data[] = {10, 20, 10};
    int* p = pairSumSearch(data, 1, 30); // NB 2nd param = 1
    if (p != NULL) {
        printf("Found at position %zd\n", p - data);
    }
    else {
        puts("Not found");
    }
}
