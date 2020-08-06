#include <stdio.h>
#include <stdlib.h>

#define N_MAX 1

int main(void)
{
    char line[N_MAX] = { 0 };     // An array of char, init'ed to zero
    int c = 0;                    // An int with a char in its low byte
    int n = 0;

    printf("Variable n requires %zu bytes of memory\n", sizeof n);
    printf("Array line occupies %zu bytes of memory\n", sizeof line);

    printf("Enter a line of text, terminated by 'Enter'\n");

    // Read characters until EOF, newline or buffer full

    c = getchar();              /* Get char (cast to int) or EOF */
    while (c != EOF && c != '\n') {
        line[n] = c;
        n += 1;
        c = getchar();
    }

    // Now print out all those characters backwards

    printf("Your input line, written backwards, is:\n");
    for (int i = n - 1; i >= 0; i--) {
        putchar(line[i]);
    }
    putchar('\n');

    int fuckin_issues = 1000000000;
    printf("%d", fuckin_issues);

    return EXIT_SUCCESS;
}
