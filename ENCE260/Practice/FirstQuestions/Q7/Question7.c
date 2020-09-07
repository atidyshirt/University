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
    int i = 0;
    while (i <= strlen(s)) {
        s[i] = s[i-1];
        i++;
    }
    return s;
}

int main(void)
{
    char s[] = "B hr mns rn azc zesdq zkk";
    printf("%s\n", alphaShiftRight(s));
}
