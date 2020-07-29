/* Print a geometric progression, with the start value, multiplier,
 * and number of elements read from standard input.
 * Written by Richard Lobb, June 2012/July 2019, for ENCE 260.
 */
#include <stdio.h>

int main(void)
{
    int value;
    while (value != 42) {
        scanf("%i", &value);
        printf("%d\n", value);
    }
}
