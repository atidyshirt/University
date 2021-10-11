#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

#include "matrix.h"


void benchmark_mul(int n, int repeats) {
 
  
  double *a = random_matrix(n);
  double *b = random_matrix(n); 
  
  double *res = alloc_matrix(n);
  
  struct timespec start, stop;
  int i;
  
  double basic = 0.0;
  
  if(n < 1200) {
    clock_gettime( CLOCK_REALTIME, &start);
    for(i = 0; i < repeats; ++i) {
      matrix_mul_basic(res, a, b, n);
    }
    
    clock_gettime( CLOCK_REALTIME, &stop);
    basic = seconds(start, stop)  / (double)repeats;
  }
  
  

  clock_gettime( CLOCK_REALTIME, &start);
  for(i = 0; i < repeats; ++i) {
    matrix_mul_transposed(res, a, b, n);
  }
  
  clock_gettime( CLOCK_REALTIME, &stop);
  double transposed = seconds(start, stop)  / (double)repeats;
  

  
  clock_gettime( CLOCK_REALTIME, &start);
  for(i = 0; i < repeats; ++i) {
    matrix_mul_blocked(res, a, b, n, 16);
  }
  
  clock_gettime( CLOCK_REALTIME, &stop);
  double blocked = seconds(start, stop) / (double)repeats;
  
  
  printf("%d basic: %.5lf, transposed: %.5lf, blocked: %.5lf\n", n, basic, transposed, blocked);
  
  free(a);
  free(b);
  free(res);
}

int main(int argc, char**argv) {
  
  if(argc < 2) {
    printf("usage: ./benchmark_mul size_increment\n");
    exit(1);
  }
  
  int size_inc = atoi(argv[1]);
  
  int i;
  int reps = 2;
  
  for(i = 1; i < 21; ++i) {
    benchmark_mul(i * size_inc, reps);
  }

  return 0;
}
