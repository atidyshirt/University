#include <stdio.h>

int* pairSumSearch(int* data, int numEls, int pairSum)
{

}

int main(void)
{
    int data[] = {1, 10, 3, 20, 1, 3, 7};
    int* p = pairSumSearch(data, 7, 23);
    if (p != NULL) {
        printf("Found at position %zd\n", p - data);
    }
    else {
        puts("Not found");
    }
}
