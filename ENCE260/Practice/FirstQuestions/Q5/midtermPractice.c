#include <stdio.h>

int add_sub(const int data[], int n)
{
    // when flag is 1 -> add, when flag is 0 minus
    int flag = 0;
    int i = 0;
    int total = 0;

    while (i < n) {
        if (flag == 1) {
            total -= data[i];
            flag = 0;
        } else {
            total += data[i];
            flag = 1;
        }
        i++;
    }
    return total;
}

int main(void)
{
    int data[4] = {1, 2, 3, 4};
    printf("%d\n", add_sub(data, 4));
}
