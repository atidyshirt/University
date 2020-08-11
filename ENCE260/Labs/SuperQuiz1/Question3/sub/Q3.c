#include <stdio.h>

#define MAX_INPUT_MESSAGE_LENGTH 4096
#define MAX_KEY_LENGTH 1024
#define MAX_PART_LENGTH 3

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
    int test = 2 + section;
    int j = 0;
    int i = 0;
    while (i < inputLength) {
        if (i > maxPartLength) {
            return -1;
        }
        if (input[i] == input[0]) {
            test -= 1;
        } else if (test == 1 && input[i] != input[0]) {
            part[j] = input[i];
            j += 1;
        }   
        i += 1; // i++ doesnt work sometimes?
    }     
    return j;
}


int main(void)
{
    /* unsigned char input[MAX_INPUT_MESSAGE_LENGTH] = {12, 22, 33, 44, 12, 2, 3, 4, 5}; */
    /* int inputLength = 9; */

    /* unsigned char part[MAX_TEXT_LENGTH]; */
    /* int section = 1; */
    /* int partLength; */

    /* partLength = splitInput(input, inputLength, section, part, MAX_TEXT_LENGTH); */
    /* printf("Section[%d] length (%d):", section, partLength); */
    /* for(int i; i < partLength; i++) printf(" %u", part[i]); */
    /* printf("\n"); */

    unsigned char input[MAX_INPUT_MESSAGE_LENGTH] = {12, 22, 33, 44, 12, 2, 3, 4, 5};
    int inputLength = 9;

    unsigned char part[MAX_PART_LENGTH];
    int section = 1;
    int partLength;

    partLength = splitInput(input, inputLength, section, part, MAX_PART_LENGTH);
    printf("Section[%d] length (%d):", section, partLength);
    for(int i; i < partLength; i++) printf(" %u", part[i]);
    printf("\n");
}
