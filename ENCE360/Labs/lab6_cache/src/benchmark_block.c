
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

#include "matrix.h"


void benchmark_blocks(int n, int repeats) {
 
  
  double *a = random_matrix(n);
  double *b = random_matrix(n); 
  
  double *res = alloc_matrix(n);
  
  struct timespec start, stop;
  int i;
  
  int blocks = 4;
  
  for (blocks = 4; blocks <= 1024; blocks *= 2) {
    clock_gettime( CLOCK_REALTIME, &start);
    for(i = 0; i < repeats; ++i) {
      matrix_mul_blocked(res, a, b, n, blocks);
    }
    
    clock_gettime( CLOCK_REALTIME, &stop);
    double blocked = seconds(start, stop);
    

    printf("%d, blocks: %d, blocked: %.4lf\n", n, blocks, blocked);
  }
  
  free(a);
  free(b);
  free(res);
}



int main(int argc, char**argv) {
  


  benchmark_blocks(1024, 1);

  return 0;
}