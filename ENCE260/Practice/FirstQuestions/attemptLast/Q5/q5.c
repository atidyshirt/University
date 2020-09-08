#include <stdio.h>

int add_even_sub_odd(const int data[], int n);

int main(void)
{
    int data[4] = {1, 2, 3, 4};
    printf("%d\n", add_even_sub_odd(data, 4));
}

int add_even_sub_odd(const int data[], int n)
{
    int total = 0;
    for (int i = 0; i < n; i++) {
        if (data[i] % 2 == 0) {
            total += data[i];
        } else {
            total -= data[i];
        }
    }
    return total;
}
