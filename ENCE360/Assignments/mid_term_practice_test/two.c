#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>


void translator(int input_pipe[], int output_pipe[])
{
  int c;
  char ch;
  int rc;

  /* first, close unnecessary file descriptors */
  // place your code between the lines of //
  ///////////////////////////////////////////////
  close(input_pipe[1]);
  close(output_pipe[0]);
  ///////////////////////////////////////////////

  /* enter a loop of reading from the user_handler's pipe, translating */
  /* the character, and writing back to the user handler.              */
  while (read(input_pipe[0], &ch, 1) > 0) {
    c = ch;
    if (isascii(c) && isupper(c))
    c = tolower(c);
    ch = c;

    /* write translated character back to user_handler. */
    // place your code between the lines of //
    ///////////////////////////////////////////////
    write(output_pipe[1], &ch, sizeof(char));
    ///////////////////////////////////////////////

    if (rc == -1) {
      perror("translator: write");
      close(input_pipe[0]);
      close(output_pipe[1]);
      exit(1);
    }
  }

  close(input_pipe[0]);
  close(output_pipe[1]);
  exit(0);
}



void user_handler(int input_pipe[], int output_pipe[])
{
  int c;    /* user input - must be 'int', to recognize EOF (= -1). */
  char ch;  /* the same - as a char. */
  int rc;   /* return values of functions. */

  /* first, close unnecessary file descriptors */
  ///////////////////////////////////////////////
  // place your code between the lines of //
  close(input_pipe[1]);
  close(output_pipe[0]);
  ///////////////////////////////////////////////

  printf("Enter text to translate:\n");
  /* loop: read input from user, send via one pipe to the translator, */
  /* read via other pipe what the translator returned, and write to   */
  /* stdout. exit on EOF from user.                                   */
  while ((c = getchar()) > 0) {
    ch = (char)c;

    /* write to translator */
    ///////////////////////////////////////////////
    // place your code between the lines of //

    write(output_pipe[1], &ch, sizeof(char));

    ///////////////////////////////////////////////

    if (rc == -1) { /* write failed - notify the user and exit. */
      perror("user_handler: write");
      close(input_pipe[0]);
      close(output_pipe[1]);
      exit(1);
    }

    /* read back from translator */
    ///////////////////////////////////////////////
    // place your code between the lines of //

    rc = read(input_pipe[0], &ch, sizeof(char));

    ///////////////////////////////////////////////

      c = (int)ch;
      if (rc <= 0) {
        perror("user_handler: read");
        close(input_pipe[0]);
        close(output_pipe[1]);
        exit(1);
      }

      putchar(c);
      if (c=='\n' || c==EOF) break;
    }

    close(input_pipe[0]);
    close(output_pipe[1]);
    exit(0);
  }


  int main(int argc, char* argv[])
  {
    int user_to_translator[2];
    int translator_to_user[2];
    int pid;
    int rc;

    rc = pipe(user_to_translator);
    if (rc == -1) {
      perror("main: pipe user_to_translator");
      exit(1);
    }

    rc = pipe(translator_to_user);
    if (rc == -1) {
      perror("main: pipe translator_to_user");
      exit(1);
    }

    pid = fork();

    switch (pid) {
      case -1:
        perror("main: fork");
        exit(1);
      case 0:
        translator(user_to_translator, translator_to_user); /* line 'A' */
        exit(0);
      default:
        user_handler(translator_to_user, user_to_translator); /* line 'B' */
    }

    return 0;
}
