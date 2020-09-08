#include <stdio.h>
#include <string.h>

int countChars(const char* s, const char* charsOfInterest)
{
    int counter = 0;
    for (int i = 0; i < strlen(s); i++) {
        for (int j = 0; j < strlen(charsOfInterest); j++) {
            if (s[i] == charsOfInterest[j]) {
                counter++;
            }
        }
    }
    return counter;
}
