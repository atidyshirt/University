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

    pipe(fd);
    if ((childpid = fork()) == 0) { /* Child code: Runs ls */
        dup2(fd[INP], STDOUT_FILENO);
        close(fd[OUTP]);
        close(fd[INP]);
        execl("/bin/ls", "ls", "-l", NULL);
        perror("The exec of ls failed");
    }

    else { /* Parent code: Runs sort */
        dup2(fd[OUTP], STDIN_FILENO);
        close(fd[OUTP]);
        close(fd[INP]);
        execl("/usr/bin/sort", "sort", "-k", "+8", NULL);
        /* Note: The location of sort depends on your distribution.
         * Use 'which sort' to find the correct location */
        perror("The exec of sort failed");
    }

    exit(0);
}
