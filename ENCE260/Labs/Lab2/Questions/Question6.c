#include <stdio.h>

int main(void)
{
    int input_int = 0;

    scanf("%i", &input_int);

    if (input_int == 0){
        printf("Zero");
    }
    else if (input_int % 2 == 0){
        printf("Even");
    } 
    else {
        printf("Odd");
    }
}
