#include <stdio.h>

int main(void)
{
    int i = -1, total = 0;
    while (i != 0) {
        scanf("%d", &i);
        if (i % 2 != 0) {
            total -= i;
        } else {
            total += i;
        }
    } 
    printf("%d", total);
}
