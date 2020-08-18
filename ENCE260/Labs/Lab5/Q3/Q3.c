#include <stdio.h>
#include <stdlib.h>

typedef struct vector2d_s Vector2d;

struct vector2d_s {
    int x;
    int y;
};

Vector2d vector(int x, int y)
{
    Vector2d result = {x, y};
    return result;
}

Vector2d vectorSum(const Vector2d v1, const Vector2d v2)
{
    int sumX;
    int sumY;
    sumX = v1.x + v2.x;
    sumY = v1.y + v2.y;
    Vector2d result = {sumX, sumY};
    return result;
}

int main(void)
{
    Vector2d v1 = vector(100, -97);
    Vector2d v2 = vector(11, 1);
    Vector2d v3 = vectorSum(v1, v2);
    printf("(%d, %d) + (%d, %d) = (%d, %d)\n",
        v1.x, v1.y, v2.x, v2.y, v3.x, v3.y);
}
