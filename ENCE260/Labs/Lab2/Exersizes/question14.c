#include <stdio.h>

int main(void) {
    int first = 0, last = 0, i = 0, j = 0, flag = 0;

    scanf(" %i %i", &first, &last);
    for (i = first; i <= last; i++) {
        flag = 0;
        for (j = 2; j <= i / 2; j++) {
            if ((i % j) == 0) {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            printf("%d\n", i);
        }
    }
}

