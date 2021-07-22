#define _GNU_SOURCE

//
// semaphore.c - Use semaphores to send messages between threads
// The threads communicate with the main thread using a semaphore based channel
// Your task is to implement the operations.
//
// First, observe the producer() function, and the main() function
// and understand how the Chan is being used to communicate. Then try to
// implement the operations.
//
// At any one point in time the channel is either empty, or full. (queue of length 1)
//
// If the channel is empty - the read semaphore has a value of 0 (must wait to read)
//                         - the write semaphore has a value of 1  (allowed to write immediately)
//
// If the channel is full - the read semaphore has a value of 1 (allowed to read immediately)
//                        - the write semaphre has a value of 0 (must wait to read)
//
// The read and write operations are therefore symettrical and proceed like this:
// 1) Acquire access to read or write via sem_wait
// 2) Perform read or write activity
// 3) Signal to opposite read or write that they can now proceed
//
// compile with: gcc semamphore.c -o semaphore --std=c99 -lpthread
//

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

    // Read and write semaphores for our channel 
    sem_t read;
    sem_t write;

    char *message; // Value stored in the channel

} Chan;


void write_channel(Chan *channel, void *message) {

    // _wait_ until the channel becomes empty, then write new contents 
    // signal any consumers waiting to read the channel
    //
    // You will need sem_post, sem_wait
    //
    // TODO: wait for our chance to access the variable

  //   assert(channel->message == NULL && "channel should be empty!");

    //write to the message  
    channel->message = message;

    // TODO: signal to any readers that there's an update


    // Channel is now occupied
}


void *read_channel(Chan *channel) {

    // TODO:
    // _wait_ until the channel becomes full, then read from the channel and take the contents 
    // signal any producers waiting to write to the channel
    //
    // You will need sem_post, sem_wait
    //
    void *message = NULL;
    // wait for an update from one of the threads

    // read the variable
    message = channel->message;
    channel->message = NULL;

    // signal to any threads waiting that they can send another update

    return message;

    // Channel is now empty
}


void init_channel(Chan *channel) {

    // TODO:
    // Initialize channel to an empty state ready for writing (and not reading)
    // You will need: sem_init
    //


    // TODO: Initialise count of the read semaphore to 0 (there's nothing to read yet)

    // TODO: Initialise the write semaphore is initialised to 1 (channel is empty, free for writing)

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


