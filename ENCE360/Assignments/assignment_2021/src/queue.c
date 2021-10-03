
#include "queue.h"

#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <assert.h>

#define handle_error_en(en, msg) \
        do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)

#define handle_error(msg) \
        do { perror(msg); exit(EXIT_FAILURE); } while (0)

typedef struct QueueStruct {


} Queue;


Queue *queue_alloc(int size) {
    assert(0 && "not implemented yet!");

}

void queue_free(Queue *queue) {

    assert(0 && "not implemented yet!");
}

void queue_put(Queue *queue, void *item) {

    assert(0 && "not implemented yet!");

}



void *queue_get(Queue *queue) {

    assert(0 && "not implemented yet!");

}

