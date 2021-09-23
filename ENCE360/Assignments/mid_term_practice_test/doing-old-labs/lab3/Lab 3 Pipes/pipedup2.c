/* Title: pipedup2.c
 * Description: ENCE360 Example code - dup2.
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
    int fd2[2];
    pid_t childpid2;

    pipe(fd2);
    if ((childpid2 = fork() == 0)) {
      pipe(fd);
      if ((childpid = fork()) == 0) { /* Child of Child code: Runs ls */
          dup2(fd[INP], STDOUT_FILENO);
          close(fd[OUTP]);
          close(fd[INP]);
          execl("/bin/ls", "ls", "-l", NULL);
          perror("The exec of ls failed");
      }
      else { /* Child code: Runs sort */
          dup2(fd[OUTP], STDIN_FILENO);
          close(fd[OUTP]);
          close(fd[INP]);
          dup2(fd2[OUTP], STDIN_FILENO);
          close(fd2[OUTP]);
          close(fd2[INP]);
          execl("/usr/bin/sort", "sort", "-k", "+8", NULL);
          /* Note: The location of sort depends on your distribution.
           * Use 'which sort' to find the correct location */
          perror("The exec of sort failed");
      }
  } else { /* Parent code: Runs head */
    dup2(fd[OUTP], STDIN_FILENO);
    close(fd[OUTP]);
    close(fd[INP]);
    execl("/usr/bin/head", "head", "-5", NULL);
    perror("The exec of head failed");
  }
    exit(0);
}
