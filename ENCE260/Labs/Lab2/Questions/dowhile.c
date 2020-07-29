#include <stdio.h>

int main(void)
{
    int value;
    do {
        scanf("%i", &value);
        printf("%i\n", value);
    } while (value != 42);
}
