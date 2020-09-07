#include <stdio.h>

typedef struct {
    int x;
    int y;
    int z;
} Vector3d;

Vector3d vector(int x, int y, int z)
{
    Vector3d v = {x, y, z};
    return v;
}

Vector3d vectorAdd(Vector3d a, Vector3d b)
{
    Vector3d v = {a.x + b.x, a.y + b.y, a.z + b.z};
    return v;
}

int main(void)
{
    Vector3d v1 = vector(1, 4, -1);
    Vector3d v2 = vector(2, 4, -1);
    Vector3d v3 = vectorAdd(v1, v2);
    printf("(%d, %d, %d)\n", v3.x, v3.y, v3.z);
}


