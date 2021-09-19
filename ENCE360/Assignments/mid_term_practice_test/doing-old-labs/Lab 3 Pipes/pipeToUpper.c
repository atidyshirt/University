/* Title: pipe.c
* Description: ENCE360 Example code - Pipes
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

int parent_to_child[2];
int child_to_parent[2];
static char message[BUFSIZ];
int child_status, size;

#define PIPE_IN 1
#define PIPE_OUT 0

int main(int argc, char *argv[]) {

  int i = 0;

  if (argc != 2) {
    fprintf(stderr, "Usage: %s message\n", argv[0]);
    exit(1);
  }

  /* Create pipes */
  if (pipe(parent_to_child) == -1) {
    perror("Pipe from");
    exit(2);
  }
  if (pipe(child_to_parent) == -1) {
    perror("Pipe - to");
    exit(2);
  }

  switch (fork()) { /* Fork a new process */

    case -1: /* Error forking */
      perror("Fork");
      exit(3);

    case 0: /* Child code */
      close(parent_to_child[PIPE_IN]);
      close(child_to_parent[PIPE_OUT]);

      /* Read from parent */
      if (read(parent_to_child[PIPE_OUT], message, BUFSIZ) != -1) {
        printf("CHILD: Recieved %s\n", message);
      }
      else {
        perror("Read");
        exit(4);
      }

      for(i = 0; i < BUFSIZ && message[i] != '\0'; i++) {
          message[i] = toupper(message[i]);
      }
      write(child_to_parent[1], message, i);

      /* Close pipes */
      close(parent_to_child[PIPE_OUT]);
      close(child_to_parent[PIPE_IN]);
      break;

    default: /* Parent code */
      close(parent_to_child[PIPE_OUT]);
      close(child_to_parent[PIPE_IN]);

      if (write(parent_to_child[PIPE_IN], argv[1], strlen(argv[1])) != -1) {
        printf("PARENT: Sent %s\n", argv[1]);
      }
      else {
        perror("Write");
        exit(5);
      }

      // To see the result
      if (read(child_to_parent[PIPE_OUT], message, BUFSIZ) != -1) {
        printf("PARENT: Recieved %s\n", message);
      }
      else {
        perror("Read");
        exit(4);
      }

      wait(&child_status);

      /* Close pipes */
      close(parent_to_child[PIPE_IN]);
      close(child_to_parent[PIPE_OUT]);
  }

  return EXIT_SUCCESS;
}
