#include <stdio.h>

int main(void) {
    int first, last, test;
    scanf("%i %i", &first, &last);

    for (int value = first; value <= last; value++) {
        for (int check = 2; check <= last; check++) {
            if (value % check != 0) {
                printf("Non prime");
            } else {
                test += 1;
            }
        } if (test == 1) {
            printf("%i\n", value);
            test = 0;
        }
    }
}
