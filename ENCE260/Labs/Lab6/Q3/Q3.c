#include <stdio.h>
#include <stdlib.h>

int* ramp(size_t n)
{
    int* meme = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        meme[i] = i + 1;
    }
    return meme;
}

void fillRamp(int* data, size_t n)
{
    for (int i = 0; i < n; i++) {
        data[i] = i + 1;
    }
}

int main(void)
{
    int* data = malloc(4 * sizeof(int));
    fillRamp(data, 4);
    for (int i = 0; i < 4; i++) {
        printf("data[%d] = %d\n", i, data[i]);
    }
    free(data);
}
