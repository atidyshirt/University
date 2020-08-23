#include <stdio.h>
#include <math.h>
#include <string.h>
#include "confab.h"
#define MAX_LINE_SIZE 1000


int main(void)
{
    char line[MAX_LINE_SIZE] = {0};
    char codedLine[MAX_LINE_SIZE] = {0};
    int rows = 0;
    
    fgets(line, MAX_LINE_SIZE, stdin);  // Read a line from stdin
    line[strlen(line) - 1] = '\0';      // Replace the newline terminator with a null byte
    scanf("%d", &rows);                 // Read a mysterious number
    confab(line, rows, codedLine);      // Encode the input line
    printf("%s\n", codedLine);          // Print the encoded string
}
