#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 1000;
    double* numbers = malloc(n);
    printf("%p\n", numbers);
    printf("%lf", *numbers);
}
