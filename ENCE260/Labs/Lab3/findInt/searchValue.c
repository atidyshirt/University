#include <stdio.h>

int countmatches(int n, int data[], int searchvalue)
{
    int counter = 0;
    for (int i = n; i >= 0; i--) {
        if (data[i] == searchvalue) {
            counter++;
        }
    }
    return counter;
}

int main(void)
{
    int nums[] = {1, 2, 3, 4, 1, 1, 5}; 
    printf("%d\n", countMatches(7, nums, 1));
}
