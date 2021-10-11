#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

#include "matrix.h"


void test_matrix(int n) {
 double *a = random_matrix(n);
 double *b = random_matrix(n);

 double *x = alloc_matrix(n);
 double *y = alloc_matrix(n);



 matrix_mul_basic(x, a, b, n);
 matrix_mul_transposed(y, a, b, n);

 printf("matrix_mul_transposed: %s\n", compare_matrix(x, y, n) ? "pass" : "fail");

 matrix_mul_blocked(y, a, b, n, 16);
 printf("matrix_mul_blocked: %s\n", compare_matrix(x, y, n) ? "pass" : "fail");


 free(a);
 free(b);

 free(x);
 free(y);

}

int main(int argc, char**argv) {

  test_matrix(100);

  return 0;
}
