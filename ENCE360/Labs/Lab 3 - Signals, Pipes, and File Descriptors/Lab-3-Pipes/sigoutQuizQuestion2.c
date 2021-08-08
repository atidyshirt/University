#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

void install_handler(void);
void quit_recieved();

int callCount;

int main(int argc, char * argv[]) {
  install_handler();
  while (1) {;};
}

void install_handler(void) {
  signal(SIGQUIT, (void *) quit_recieved);
}

void quit_recieved (void) {
  signal(SIGQUIT, (void *) quit_recieved);
  write(1, "SIGQUIT\n", 8);
  if (callCount == 1) { exit(0); }
  callCount++;
}
