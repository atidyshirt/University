#include <stdio.h>
#include <string.h>

char* alphaShiftRight(char* s)
{
    for (int i = 0; i < strlen(s) - 1; i++) {
        if (s[i] != ' ') {
            s[i] = s[i] + 1;
        }
    }
    return s;
}

char* rotateLeft(char* s)
{
    int i = 0;
    while (i <= strlen(s)) {
        s[i] = s[i-1];
        i++;
    }
    return s;
}

int main(void)
{
    char s[] = "Hello World!";
    printf("%s\n", alphaShiftRight(s));
    printf("%s\n", rotateLeft(s));
}
