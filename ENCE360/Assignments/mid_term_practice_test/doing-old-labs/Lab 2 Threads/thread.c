/* Title: thread.c
 * Description: ENCE360 Example code - Creation of a thread
 */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>

int global = 5;

void* child(void* arg) {
    int local = 10;

    global++;
    local++;
    printf("[Child]  child thread id: 0x%x\n", (unsigned int)pthread_self());
    printf("[Child]  global: %d  local: %d\n", global, local);

    pthread_exit(NULL);
}

int main() {
    pthread_t  childPid;
    int       local = 10;

    printf("[At start]  global: %d  local: %d\n", global, local);

    /* create a child thread */
    if (pthread_create(&childPid, NULL, child, NULL) != 0)
    {
        perror("create");
        exit(1);
    }
    else { /* parent code */
        global++;
        local--;
        printf("[Parent] parent main thread id : 0x%x\n", (unsigned int)pthread_self());
        printf("[Parent] global: %d  local: %d\n", global, local);
        sleep(1);
    }
    printf("[At end] global: %d  local: %d\n", global, local);
    exit(0);
}
