#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* alphaShiftLeft(char* s) 
{
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == 'A' || s[i] == 'a') {
            s[i] = s[i] + 25;
        } else if (s[i] == ' ') {
            s[i] = s[i];
        }  else if (!isalpha(s[i])) {
            s[i] = s[i];
        } else {
            s[i] = s[i] - 1;
        }
    }
    return s;
}

int main(void)
{
    char s[] = "';lkjhgfdsa";
    printf("%s\n", alphaShiftLeft(s));
    if (s != alphaShiftLeft(s)) {
        printf("Test feedback: Your function's return value is incorrect!\n");
    }
}
