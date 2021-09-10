
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

struct Node {
  /* Node structure
  * @Attribute int: data
  * @Attribute Node*: next
  */
  struct Node* next;
  void* data;
};

typedef struct QueueStruct {
  struct Node* head;
  struct Node* tail;
  int size;
  sem_t semaphore;
  pthread_mutex_t lock;
} Queue;


Queue *queue_alloc(int size) {
  Queue* queue = malloc(sizeof(struct QueueStruct));
  queue->size = size;
  sem_init(&queue->semaphore, 0, queue->size);
  pthread_mutex_init(&queue->lock, NULL);
  return queue;
}

void queue_free(Queue *queue) {
  free(queue);
}

void queue_put(Queue *queue, void *item) {
  sem_wait(&queue->semaphore);
  pthread_mutex_lock(&queue->lock);
  struct Node* node = (struct Node*)malloc(sizeof(struct Node));
  if (queue->size == 0) {
    node->data = item;
    queue->head = queue->tail = node;
  } else {
    queue->tail->next = node;
    queue->tail = queue->tail->next;
    queue->size++;
  }
  pthread_mutex_unlock(&queue->lock);
  sem_post(&queue->semaphore);
}



void *queue_get(Queue *queue) {
  // TODO: implement function
  /* sem_wait(&queue->semaphore); */
  /* pthread_mutex_lock(&queue->lock); */
}

