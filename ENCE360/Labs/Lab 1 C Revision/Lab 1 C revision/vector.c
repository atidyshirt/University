
/*
 * vector.c - an exercise in memory allocation and pointers.
 *
 *  compile with: gcc vector.c -o vector -std=c99
 *  run with ./vector
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

struct Vector {
    double *data;
    int size;
};


//
// Initialize a new vector of size n
// Allocate memory and use memset to set the data to zero
//
// Functions you'll likely need (check these with the man pages):
// malloc
// memset, sizeof
//
struct Vector *new_vector(int n) {
  double *data;
  data = (double *)malloc(n * sizeof(double));
  memset(data, 0, n);
  struct Vector* vector = (struct Vector*)malloc(sizeof(struct Vector));
  vector->data = data;
  vector->size = n;
  return vector;
}


//
// Allocate a vector and copy the data from a pointer
//
struct Vector *new_from(double *data, int n) {
  struct Vector *v = new_vector(n);
  for (int i = 0; i < n; ++i) {
    v->data[i] = data[i];
  }

  return v;
}

//
// Take two vectors as input, add their contents and return a new vector with the added data
// it is an error if the sizes of the input vectors have different sizes
//
struct Vector *add_vectors(struct Vector *v1, struct Vector *v2) {
  assert(v1->size == v2->size);
  double *data;
  data = (double *)malloc(v1->size * sizeof(double));
  for (int i = 0; i < v1->size; i++) {
    data[i] = v1->data[i] + v2->data[i];
  }
  struct Vector* vector = (struct Vector*)malloc(sizeof(struct Vector));
  vector->data = data;
  vector->size = v1->size;
  return vector;
}



/*
 * Print out the contents of a vector
 */
void print_vector(struct Vector *v) {

    printf("<");
    for (int i = 0; i < v->size; ++i) {
        printf("%.2f", v->data[i]);

        if (i + 1 < v->size) {
            printf(", ");
        }
    }
    printf(">\n");
}



int main() {
    double values_x[] = { 1.43,2.0,3.5,4.0 };
    double values_y[] = { 7.0,-2.7,4.0,0.0 };

    struct Vector *x = new_from(values_x, 4);
    struct Vector *y = new_from(values_y, 4);

    print_vector(x);
    print_vector(y);

    struct Vector *r = add_vectors(x, y);
    print_vector(r);

      /* Expected output: */
      /* <1.43, 2.00, 3.50, 4.00> */
      /* <7.00, -2.70, 4.00, 0.00> */
      /* <8.43, -0.70, 7.50, 4.00> */

      // Experiment with different inputs

    return 0;
}



