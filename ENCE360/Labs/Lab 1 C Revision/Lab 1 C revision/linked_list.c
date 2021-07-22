/*
* linked_list.c - an exercise in function pointers and lists.
*
*  compile with: gcc linked_list.c -o linked_list -std=c99
*  run with ./linked_list
*
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


struct Link {
  struct Link *next;
  int value;
};

//
// Print all the values in a linked list structure
//
void print_list(struct Link *list) {
  for (struct Link *l = list; l != NULL; l = l->next) {
    printf("%d", l->value);

    if (l->next) {
      printf(", ");
    }
  }

  printf("\n");
}



//
// Append a value to the front of a linked list
// the returned list now looks like:  head->rest of list
//
struct Link *append(int x, struct Link *head) {
  struct Link *head_ = (struct Link*)malloc(sizeof(struct Link));
  head_->next = head;
  head_->value = x;

  return head_;
}





//
// Reverse a linked list in place (modifies original list)
//
struct Link *reverse_list(struct Link* list) {
  struct Link *head = NULL;

  for (struct Link *l = list; l != NULL;) {
    struct Link *next = l->next;
    l->next = head;
    head = l;

    l = next;
  }

  return head;
}

//
// Iteratively compute the fibonacci sequence and store the results
// in a Linked list structure. Note the first 'head' of a list should be a NULL pointer.
//
// fib (0) = 1
// fib (1) = 1
// fib (n) = fib(n - 1) + fib(n - 2)
//
// fib = 1, 1, 3, 5, 8, 13...
//

struct Link *fibonacci(int n) {

  struct Link *head = NULL;
  int prev = 1;
  int latest = 1;

  if (n > 0) {
    head = append(1, head);
  }

  if (n > 1) {
    head = append(1, head);
  }

  for (int i = 2; i < n; ++i) {
    head = append(latest + prev, head);

    prev = latest;
    latest = head->value;
  }


  return reverse_list(head);
}




//
// Write a function called "map_list" which takes a linked list,
// and a function pointer, and return a new list with values transformed using the function given.
//
// If unfamiliar, a good guide to the subject of function pointers is here:
// http://denniskubes.com/2013/03/22/basics-of-function-pointers-in-c/
//
// There's a question on the Quiz about this - so do this first!
//

struct Link *map_list(struct Link* list, int (*square)()) {
  struct Link *head = NULL;
  while (list != NULL) {
    head = append((*square)(list->value), head);
    list = list->next;
  }
  return reverse_list(head);
}



//
// Free the linked list structure for this you'll need to
// traverse the list.
//
//
void free_list(struct Link *list) {
  free(list);
}



// Our function to transform the elements of a list
int square(int x) {
  return x * x;
}



int main() {

  struct Link *fib = fibonacci(10);
  struct Link *fib_sq = map_list(fib, square);

  // print out our list of fibonacci^2 (in reverse)
  // 1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025
  print_list(fib);
  print_list(fib_sq);

  free_list(fib);
  free_list(fib_sq);

  return 0;
}
