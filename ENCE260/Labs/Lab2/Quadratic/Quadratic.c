#include <stdio.h>
#include <math.h>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int main(void)
{
    float a = 0;
    float b = 0;
    float c = 0;
    scanf("%f %f %f", &a, &b, &c);
    float ans_1 = (-b + sqrt(b*b - 4 * a * c)) / 2 * a;
    float ans_2 = (-b - sqrt(b*b - 4 * a * c)) / 2 * a; 
    if (b*b - 4 * a * c < 0) {
        printf("Complex roots");
    } else if (a == 0) {
        printf("Not a quadratic");
    } else {
        printf("Roots are %.4f and %.4f", MIN(ans_1, ans_2), MAX(ans_1, ans_2));
    }
}
