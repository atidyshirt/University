#include <pthread.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <assert.h>

int has_run[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

void runMe(int *arg) {
  int value = (*arg);
  assert(value >= 0 && value < 5 && "Bad argument passed to 'runMe()!'");
  has_run[value] = 1;
  int *ret = (int*)malloc(sizeof(int));
  *ret = value * value;
  pthread_exit((void*)ret);
}

int run_threads(int n) {
  pthread_t workers[n];
  int load[n];
  int* val;
  int total = 0;
  for (int i=0; i < n; i++) {
    load[i] = i;
    pthread_create(&workers[i], NULL, (void *) runMe, &load[i]);
    pthread_join(workers[i], (void*) &val);
    total += *val;
  }
  return total;
}

int main (int argc, char **argv) {
  int sum = run_threads(5);
  int correct = 0;
  for(int i = 0; i < 5; ++i) {
    if(has_run[i]) correct++;
  }
  printf("%d %d", correct, sum);
  return 0;
}
