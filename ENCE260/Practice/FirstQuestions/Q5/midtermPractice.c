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

int add_even_sub_odd(const int data[], int n)
{
    int flag = 0, total = 0, i = 0;
    while (i < n) {
        if (flag == 0) {
            total -= data[i];
            flag = 1;
        } else {
            total += data[i];
            flag = 0;
        }
        i++;
    }
    return total;
}

int main(void)
{
    int data[6] = {5, -9, -3, 0, 8, -1};
    printf("%d\n", add_even_sub_odd(data, 6));
}
