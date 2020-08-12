#include <stdio.h>

char* mystrrchr(char* s, int c)
{
    int i = 0;
    char* out;

    while (*s != '\0') {
        if (*s == c) {
            out = s;
        }
        i++;
        s++;
    }
    return out;
}

int tokenCopy(char* dest, const char* src, int destSize)
{

}

int main(void)
{
    char buff[5];
    int n = tokenCopy(buff, "This is a string", 5);
    printf("%d '%s'\n", n, buff);
}
