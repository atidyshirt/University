#include <stdio.h>
void printViaPtr(const int* intPtr)
{
    printf("%d\n", *intPtr);
}

void print2Ints(int number1, int number2)
{
    printViaPtr(&number1);
    printViaPtr(&number2);
}

void swap(int* address1, int* address2)
{
    address1 = address1 + address2;
    address2 = address2 - address1;
    printf("%d %d", address1, address2);
}

int main(void)
{
    print2Ints(21, 12);
}
