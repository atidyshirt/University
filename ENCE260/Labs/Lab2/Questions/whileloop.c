/* Print a geometric progression, with the start value, multiplier,
 * and number of elements read from standard input.
 * Written by Richard Lobb, June 2012/July 2019, for ENCE 260.
 */
#include <stdio.h>
int main(void)
{
    int numTerms = 0;
    int value = 1;
    int multiplier = 1;
    int i = 0; // Number of terms printed so far
    printf("Enter value, multiplier and number of terms to print: ");
    scanf("%d %d %d", &value, &multiplier, &numTerms);
    while (i < numTerms) {
        printf("%d\n", value);
        value *= multiplier;
        i++;
    }
    return 0;
}
