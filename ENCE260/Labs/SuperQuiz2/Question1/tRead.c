#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>

// Common declarations
#define MAX_TEXTFILE_SIZE 4096
#define MAX_FILENAME_LENGTH 80


size_t readText(FILE* file, char text[], size_t maxTextSize)
{
    char* line = fgets(text, maxTextSize, file);
    size_t len = strlen(text);
    while(line != NULL && len != maxTextSize - 1) {
        line = fgets(text+len, maxTextSize-len, file);
        len = strlen(text);
    }
    return len;
}

size_t readCipherBook(FILE* file, char text[], size_t maxTextSize)
{
    char narr[maxTextSize];
    int textLength = readText(file, text, maxTextSize);
    int i = 0;
    int j = 0;
    int p = 0;
    while(i < textLength) {
        if(isspace(text[i])) {
            p += 1;
            i += 1;
        } else {
            narr[i-p] = text[i];
            j += 1;
            i += 1;
        }
    }
    memset(text, 0, maxTextSize); 
    strcpy(text, narr);
    return j;
}

int main(void)
{
    char filename[MAX_FILENAME_LENGTH] = "";
    char text[MAX_TEXTFILE_SIZE] = "";
    FILE* file = NULL;
    size_t textLength = 0;
    
    scanf("%80s", filename);
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found... program will fail with segmentation fault\n");
    }
    textLength = readCipherBook(file, text, MAX_TEXTFILE_SIZE);
    fclose(file);
    
    printf("%s\n", text);
    printf("Size of cipherfile is %zu\n", textLength);
    return 0;
}
