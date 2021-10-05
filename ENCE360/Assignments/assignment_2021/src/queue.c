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

/* Queue structure
* @Attribute pthread_mutex_t lock
* @Attribute sem_t enqueue
* @Attribute sem_t dequeue
* @Attribute int head    -- head of queue
* @Attribute int tail    -- tail of queue
* @Attribute size_t size -- size of the queue
*/
typedef struct QueueStruct {
  pthread_mutex_t lock;
  sem_t enqueue;
  sem_t dequeue;
  int head;
  int tail;
  void** queue;
  size_t size;
} Queue;


/* initilizes a new queue of a given size
* @param int size -- size of the initilized queue
*/
Queue *queue_alloc(int size) {
  Queue* queue = malloc(sizeof(Queue));
  queue->queue = malloc(sizeof(void *) * size);
  queue->size = size;
  queue->head = queue->tail = 0;
  pthread_mutex_init(&queue->lock, NULL);
  sem_init(&queue->enqueue, 0, size);
  sem_init(&queue->dequeue, 0, 0);
  return queue;
}

/* frees all locks, semaphores and the queue itself
* @param Queue* queue -- queue to free
*/
void queue_free(Queue *queue) {

  int sem_value;
  sem_getvalue(&queue->dequeue, &sem_value);
  pthread_mutex_destroy(&queue->lock);
  sem_destroy(&queue->enqueue);
  sem_destroy(&queue->dequeue);
  free(queue->queue);
  free(queue);
}

/* enqueues a node to the queue
* @param Queue* queue -- queue to append to
* @param void* data   -- data to enqueue
*/
void queue_put(Queue *queue, void *item) {
  sem_wait(&queue->enqueue);
  pthread_mutex_lock(&queue->lock);

  queue->tail++;
  queue->queue[queue->tail] = item;
  queue->tail = queue->tail % queue->size;

  pthread_mutex_unlock(&queue->lock);
  sem_post(&queue->dequeue);
}

/* pops the head of the queue and returns value if the queue is empty
* it will return 0
* @param Queue* queue -- queue to pop from
* @return void* data  -- data from queue
*/
void* queue_get(Queue *queue) {
  sem_wait(&queue->dequeue);
  pthread_mutex_lock(&queue->lock);

  queue->head++;
  void* data = queue->queue[queue->head];
  queue->head = queue->head % queue->size;

  pthread_mutex_unlock(&queue->lock);
  sem_post(&queue->enqueue);
  return data;
}
