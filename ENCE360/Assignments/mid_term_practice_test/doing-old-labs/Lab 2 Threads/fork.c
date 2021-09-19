/* Title: fork.c
 * Description: ENCE360 Example code - Use of the fork() system call.
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

int global = 5;

int main() {
    pid_t  childPid;
    int    local = 10;

    printf("[Start with] global: %d  local: %d\n", global, local);

    childPid = fork(); /* Create a child process */

    if (childPid < 0) { /* Error handling */
        perror("fork");
        exit(1);
    }
    else if (childPid == 0) { /* Child code */
        global++;
        local++;
        printf("[Child]  childPid: 0x%x\n", getpid());
        printf("[Child]  global: %d  local: %d\n", global, local);
        sleep(4); /* Wait 4 seconds */
    }
    else { /* Parent code */
        global--;
        local--;
        /* waitpid(childPid, NULL, 0); */
        printf("[Parent] childPid: 0x%x  parent: 0x%x\n", childPid, getpid());
        printf("[Parent] global: %d  local: %d\n", global, local);
        sleep(2); /* Wait 2 seconds */
    }

    printf("[At end (0x%x)] global: %d  local: %d\n", getpid(), global, local);

    return EXIT_SUCCESS;
}

