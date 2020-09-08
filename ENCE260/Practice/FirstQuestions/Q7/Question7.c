#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* alphaShiftRight(char* s)
{
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == 'z' || s[i] == 'Z') {
            s[i] = s[i] - 25;
        }
        else if (s[i] != ' ' && isalpha(s[i])) {
            s[i] = s[i] + 1;
        }
    }
    return s;
}

char* rotateLeft(char* s)
{
    if (strlen(s) < 2) {
        return NULL;
    }
    char tmp;
    for (int i=0; i < strlen(s)-1; i++) {
        tmp = s[i];
        s[i] = s[i + 1];
        s[i + 1] = tmp;
    }
    return s;
}

int main(void)
{
    char s[] = "Hello World!";
    printf("%s\n", rotateLeft(s));
}
