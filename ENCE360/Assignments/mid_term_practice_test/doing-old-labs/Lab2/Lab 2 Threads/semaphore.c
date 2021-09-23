#define _GNU_SOURCE

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <stdlib.h>
#include "assert.h"

#define NUM_THREADS 4

typedef struct {
    sem_t read;
    sem_t write;

    char *message;

} Chan;


void write_channel(Chan *channel, void *message) {
    sem_wait(&channel->write);
    assert(channel->message == NULL && "channel should be empty!");
    channel->message = message;
    sem_post(&channel->read);
}


void *read_channel(Chan *channel) {
    void *message = NULL;
    sem_wait(&channel->read);
    message = channel->message;
    channel->message = NULL;
    sem_post(&channel->write);
    return message;
}


void init_channel(Chan *channel) {
    sem_init(&channel->read, 0, 0);
    sem_init(&channel->write, 0, 1);
    channel->message = NULL;
}



// Producer thread sending messages to main
void *producer(void *arg)
{
    char message[128];
    Chan *channel = (Chan*)arg;
    for (int k = 0; k < 10; ++k) {
        sprintf(message, "Hello %d from thread %x", k, (unsigned int)pthread_self());
        // Send message to main
        write_channel(channel, message);
        sleep(1);
    }
    // Signal to the main thread that we have finished!
    write_channel(channel, NULL);
    pthread_exit(0);
}


int main(int argc, char **argv) {
    Chan channel;
    pthread_t thread[NUM_THREADS];
    // Initialise the Chan structure
    init_channel(&channel);
    // Create a bunch of threads running out producer
    for (int i = 0; i < NUM_THREADS; ++i) {
        pthread_create(&thread[i], NULL, producer, &channel);
    }
    int finished = 0;
    while (finished < NUM_THREADS) {
        // Consumer of the pi calculation
        char *message = read_channel(&channel);
        if (message) {
            printf("recieved: %s\n", message);
        }
        else {
            // Another worker has finished
            finished++;
        }
    }
    // Wait for all the threads we created
    for (int i = 0; i < NUM_THREADS; ++i) {
        // Wait for ith thread to finish
        pthread_join(thread[i], NULL);
    }
    return 0;
}


