#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int myIndex(int data[], int* element)
{
    int i = 0;
    while (&data[i] != element) {
        i += 1;
    }
    return i;
}

int main(void)
{
    int data[30];
    int* p = &data[17];
    printf("Index is %d\n", myIndex(data, p));
}
