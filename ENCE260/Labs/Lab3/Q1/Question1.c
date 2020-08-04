#include <stdio.h>
#include <ctype.h>

double discriminant(double a, double b, double c)
{
    return ((b*b) - (4 * a * c));
}

int main(void)
{
    printf("%.2lf\n", discriminant(1.5, 1.5, 1.5));
    int c = 0;
    c = getchar();
    while ( c != EOF) {
        if (isdigit(c)) {
            printf("'%c': Digit %d\n", c, c - '0');
        } else if (isalpha(c)) {
            printf("'%c': Letter %d\n", c, toupper(c) - '@');
        } else if (c == 10) {
            printf("'\\n'\n");
        } else {
            printf("'%c': Non-alphanumeric\n", c);
        }
        c = getchar();
    }
}

