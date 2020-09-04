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

void removeChar(char *str, unsigned int index) {
    char *src;
    for (src = str+index; *src != '\0'; *src = *(src+1),++src) ;
    *src = '\0';
}

size_t readCipherBook(FILE* file, char text[], size_t maxTextSize)
{
    int i = 0;
    size_t length = readText(file, text, maxTextSize);
    while (text[i] != '\0') {
        if (text[i] == ' ' || text[i] == '\n' || text[i] == '\t' || text[i] == '\r' || text[i] == '\f') {
            removeChar(text, i);
            length-= 1;
        }
        i++;
    }
    return length;
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
