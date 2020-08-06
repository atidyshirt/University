#include <stdio.h>
#include <ctype.h>

#define MAX_INPUT_MESSAGE_LENGTH 4096

int readInput(unsigned char input[], size_t inputMaxLength) 
{
    int out;
    out = scanf("%hhu", input);
    if (out > inputMaxLength) {
        return -1;
    } else {
        return out;
    }
}

int readUCharInt(unsigned char* input)
{
    int size;
    size = scanf("%hhu", input);
    return size;
}

int main(void)
{
    unsigned char input[MAX_INPUT_MESSAGE_LENGTH];
    int inputLength;
    
    inputLength = readInput(input, MAX_INPUT_MESSAGE_LENGTH);

    printf("Message (%s):", input);
    for (int i=0; i < inputLength; i++) printf(" %u", input[i]);
    printf("\n");
}
