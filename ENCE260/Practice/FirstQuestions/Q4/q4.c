#include <stdio.h>

int main(void)
{
    int n = -1, flag = 0, total = 0;
    while (n != 0) {
        scanf("%d\n", &n);
        if (n != 13 && flag != 1) {
            total += n;
            flag = 1;
        } else {
            flag = 0;
        }
    }
    printf("%d", total);
}
