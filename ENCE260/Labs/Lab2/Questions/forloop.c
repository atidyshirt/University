#include <stdio.h>

int main(void)
{
    int inp;
    int out;

    scanf("%d", &inp);

    for(int i = 1; i <= inp; i++) {
        out = i * i;
        printf("%d\n", out);
    }
}
