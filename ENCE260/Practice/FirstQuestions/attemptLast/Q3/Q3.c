#include <stdio.h>

int main(void)
{
    int n = 0;
    int start = 0, step = 0;
    scanf("%d %d", &start, &step);
    while (n < 6) {
        printf("%d\n", (start + n * step));
        n++;
    }
}
