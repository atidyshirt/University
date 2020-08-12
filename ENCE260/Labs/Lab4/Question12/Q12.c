#include <stdio.h>
#include <stdlib.h>
char data[100];
char thing1 = 2;

int isInData(char* address)
{
    int flag = 0;
    for (int i; i < 100; i++) {
        if (*address == data[i]) {
            flag = 1;
        }
    } 
    return flag;
}

int main(void)
{
    // Expect 1, 1, 1, 0
    printf("%d\n", isInData(&data[0]));
    printf("%d\n", isInData(&data[17]));
    printf("%d\n", isInData(&data[99]));
    printf("%d\n", isInData(&thing1));
}
