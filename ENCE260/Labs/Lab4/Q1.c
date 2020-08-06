#include <stdio.h>

int main(void)
{
    int num = 20;
    int* ptr = NULL;
    ptr = &num;
    printf("%d, %p, %p, %p, %d\n", *ptr, &ptr, ptr, &num, num);

}
