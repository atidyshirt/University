#include <stdio.h>

float ratio(int num1, int num2)
{
    return ((double)num1 / (double)num2);
}

void step()
{
    int start;
    int step;
    scanf("%d %d", &start, &step);
    for (int i = 0; i < 6; i++) {
        printf("%d\n", (start + i*step));
    }
}

int sum() {
}

int main(void)
{
    step();
}
