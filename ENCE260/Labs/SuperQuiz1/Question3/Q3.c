#include <stdio.h>

#define MAX_INPUT_MESSAGE_LENGTH 4096
#define MAX_KEY_LENGTH 1024
#define MAX_TEXT_LENGTH 3072

int readUCharInt(unsigned char* input)
{
    int size;
    size = scanf("%hhu", input);
    return size;
}

int readInput(unsigned char input[], size_t inputMaxLength) 
{
    int i = 0;
    unsigned char tester;
    while ((readUCharInt(&tester)) != -1) {
        input[i] = tester;
        i++;
        if (i == inputMaxLength) {
            return -1;
        }
    } 
    return i;
}

int splitInput(unsigned char input[], size_t inputLength, int section, unsigned char part[], size_t maxPartLength)
{
    int i = 0;
    unsigned char c;
    unsigned char inside[MAX_INPUT_MESSAGE_LENGTH];
    unsigned char outside[MAX_INPUT_MESSAGE_LENGTH];
    int flag = 0;
    int counter = 0;
    int size = 0;
    unsigned char foo;
    while (readInput(input, MAX_INPUT_MESSAGE_LENGTH) != -1 && i < inputLength) {
        foo = input[0];
        if (flag == 0) {
            if (c != foo) {
                inside[i] = c;
                counter += 1;
            } else {
                flag = 1;
            }
        }
        if (flag == 1) {
            inside[(i - counter)] = foo;
        }
        size = i;
        i = 0;
        if (section == 1) {
             for(i = 0; i < size; i++) {
                input[i] = outside[i];
            }
        } else {
            for(i = 0; i < size; i++) {
                input[i] = inside[i];
            }
        } 
        i += 1;
    } return flag;
}


int main(void)
{
    unsigned char input[MAX_INPUT_MESSAGE_LENGTH] = {12, 22, 33, 44, 12, 2, 3, 4, 5};
    int inputLength = 9;

    unsigned char part[MAX_KEY_LENGTH];
    int section = 0;
    int partLength;

    partLength = splitInput(input, inputLength, section, part, MAX_KEY_LENGTH);
    printf("Section[%d] length (%d):", section, partLength);
    for(int i=0; i < partLength; i++) printf(" %u", part[i]);
    printf("\n");
}
