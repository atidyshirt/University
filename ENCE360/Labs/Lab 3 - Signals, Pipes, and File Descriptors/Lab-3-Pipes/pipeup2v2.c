/* Title: pipedup2v2.c
* Description: ENCE360 Question One Quiz Server
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define INP 1
#define OUTP 0

int main(void) {
  int fd[2];
  pid_t childpid;

  pipe(fd);
  if ((childpid = fork()) == 0) { /* Child code: Runs input */
    dup2(fd[INP], STDOUT_FILENO);
    close(fd[OUTP]);
    close(fd[INP]);
    execl("/usr/bin/sort", "sort", NULL);
    perror("Cannot sort");
  }

  else { /* Parent code: Runs sort */
    dup2(fd[OUTP], STDIN_FILENO);
    close(fd[OUTP]);
    close(fd[INP]);
    execl("/usr/bin/head", "head", "-2", NULL);
    perror("exec failed");
  }

  exit(0);
}
