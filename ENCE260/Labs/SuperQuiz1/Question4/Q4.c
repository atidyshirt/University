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
    int test = 2 + section;
    int j = 0;
    int i = 0;
    while (i < inputLength) {
        if (input[i] == input[0]) {
            test -= 1;
        }
        else if (test == 1 && input[i] != input[0]) {
            part[j] = input[i - 1];
            printf("%d\n", part[j]);
            j += 1;
        }   
    i += 1;
    }     
    return j;
}

void decryptMessage(unsigned char key[], size_t keyLength, unsigned char message[], size_t messageLength)
{
    int i = 0; 
    int r = 0;
    while (i < messageLength) {
        if (r >= keyLength) {
            r = r - keyLength;
        } else {
            message[i] = message[i] - key[r];
            r += 1;
            i += 1;
        }
    } 
}

int main(void)
{
    unsigned char key[MAX_KEY_LENGTH] = {23};
    unsigned char message[MAX_TEXT_LENGTH] = {67,20,127};
    int keyLength = 1;
    int messageLength = 3;

    decryptMessage(key, keyLength, message, messageLength);

    printf("Decrypt Message (%d):", messageLength);
    for(int i=0; i < messageLength+1; i++) printf(" %u", message[i]);
    printf("\n");
}
