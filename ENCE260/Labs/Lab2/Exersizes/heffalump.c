#include <stdio.h>

int heffalump(float screeHeight, float rushHeight, float slideBack, int counter) {
    if (screeHeight == 0) {
        return 0;
    } else if (rushHeight <= 0) {
        return counter;
    } else if (rushHeight >= screeHeight) {
        return counter + 1;
    } else {
        return heffalump(screeHeight-rushHeight+slideBack, rushHeight, slideBack, counter+1);
    }
}

int main(void)
{
    int counter = 0;
    int result;
    float scree, step, slide;
    scanf("%f %f %f", &scree, &step, &slide);

    result = heffalump(scree, step, slide, counter);

    printf("%i", result);
}
