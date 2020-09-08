#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    signed char num = 0;  // Remember, this is (or can be) a 1-byte int
    
    num = 127;
    num += 1;
    printf("%d", num);
    return EXIT_SUCCESS;
}
