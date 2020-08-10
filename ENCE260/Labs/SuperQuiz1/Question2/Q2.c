#include <stdio.h>
#include <ctype.h>

#define MAX_INPUT_MESSAGE_LENGTH 4

int readUCharInt(unsigned char* input)
{
    int size;
    size = scanf("%hhu", input);
    return size;
}

int readInput(unsigned char input[], size_t inputMaxLength) 
{
    int i = 0;
    while (readUCharInt(&input[i]) != -1) {
        if (i >= inputMaxLength) {
            return -1;
        } i++;
    } return i;
}

int main(void)
{
    unsigned char input[MAX_INPUT_MESSAGE_LENGTH];
    int inputLength;

    inputLength = readInput(input, MAX_INPUT_MESSAGE_LENGTH);
    printf("Message (%d):", inputLength);
    for (int i=0; i < inputLength; i++) printf(" %u", input[i]);
    printf("\n");
}
