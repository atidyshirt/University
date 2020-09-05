#include <stdio.h>
#include <string.h>

char* mystrstr(char* haystack, char* needle)
{
    size_t needle_len = strlen(needle);

    haystack = strchr (haystack, needle[0]);
    if (haystack == NULL) {
        return (char *) haystack;
    }

    if (memcmp (haystack, needle, needle_len) == 0) {
        return (char *) haystack;
    }
    return NULL;
}

int mystrnlen(const char* s, int maxlen)
{
    int i = 0;
    while (i < maxlen && s[i] != '\0') {
        i++;
    }
    return i;
}

int main(void)
{
    printf("%d\n", mystrnlen("ENCE260", 20));
}
