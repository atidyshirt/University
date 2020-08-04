#include <stdio.h>

// A function to read a small format (8-bit) number
int readUCharInt(unsigned char* input)
{
    int size;
    size = scanf("%hhu", input);
    return size;
}

int main()
{
    unsigned char input = 0;
    int result = 0;
    
    result = readUCharInt(&input);

    if (input == 0) {
        printf("No input");
    }
    else if (input >= 32 && input <= 127) {
        printf("Read number %d with ASCII symbol %c\n", input, input);
    } else {
        printf("Read number %d - non-printable character", input);
    }
}
