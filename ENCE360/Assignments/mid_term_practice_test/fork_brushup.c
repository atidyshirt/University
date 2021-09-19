#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define CHILD(ID) ID == 0 ? 1 : 0
#define PARENT(ID) ID != 0 ? 1 : 0

int main (int argc, char* argv[]) {
  int id = fork();
  if (PARENT(id)) {
    // NOTE: to get three processes we must do this, so that the parent process does not fork again
    id = fork();
  }
  if (CHILD(id)) {
    printf("Hello from child process %d\n", id);
  } else {
    printf("Hello from parent process %d\n", id);
  }
  return 0;
}
