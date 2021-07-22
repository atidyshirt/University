/* Title: waiting.c
 * Description: ENCE360 Example code - Signals.
 */

#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>  /* defines pid_t */
#include <unistd.h>     /* defines fork() */
#include <sys/wait.h>   /* defines the wait() system call. */
#include <signal.h>

 /* Function prototypes */
void sighup(); /* routines child will call upon sigtrap */
void sigint();
void sigquit();

int main(int argc, const char * argv[]) {
    /* storage place for the pid of the child process, and its exit status. */
    pid_t child_pid = 0;
    int child_status = 0;

    /* signal(SIGCHLD, &waitChild); */ /*Register the signal handler - syntax */

    /* fork a child process... */
    child_pid = fork();

    printf("child_pid is %i\n", child_pid);

    if (child_pid < 0) { /* fork() and check if there were errors */
        perror("fork"); /* print a system-defined error message */
        exit(EXIT_FAILURE);
    }

    else if (child_pid == 0) { /* Child code */
        signal(SIGHUP, sighup); /* set function calls */
        signal(SIGINT, sigint);
        signal(SIGQUIT, sigquit);
        for (; ; sleep(1)); /*loop forever*/
    }

    else { /* Parent code */
        printf("Parent processing starts\n");

        /* child_pid holds id of child */
        printf("\nPARENT: sending SIGHUP\n\n");
        sleep(1); /* Give the child some time to set up its signal handlers */
        kill(child_pid, SIGHUP);
        sleep(3); /* pause for 3 secs */
        
        printf("\nPARENT: sending SIGINT\n\n");
        kill(child_pid, SIGINT);
        sleep(3); /* pause for 3 secs */
        
        printf("\nPARENT: sending SIGQUIT\n\n");
        kill(child_pid, SIGQUIT);
        wait(&child_status);
        
        printf("\nPARENT: doing something\n\n");
        sleep(3);
    }

    return EXIT_SUCCESS;
}

void sighup() {
    signal(SIGHUP, sighup); /* reset signal */
    printf("CHILD: I have received a SIGHUP\n");
}

void sigint() {
    signal(SIGINT, sigint); /* reset signal */
    printf("CHILD: I have received a SIGINT\n");
}

void sigquit() {
    printf("CHILD: My DADDY has Killed me!!!\n");
    printf("CHILD: cleaning up...\n");
    sleep(2);
    exit(0);
}

