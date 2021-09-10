#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <netdb.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>

#include "http.h"

#define BUF_SIZE 1024

int init_stream_socket(void) {
  /* Initilise a new TCP/STREAM socket */
  int s = socket(AF_INET, SOCK_STREAM, 0);
  if (s != -1) return s; else perror("Error creating socket"); exit(1);
}

Buffer* http_query(char *host, char *page, int port) {
  // TODO: Implement http query
  int sock = init_stream_socket();

}

// split http content from the response string
char* http_get_content(Buffer *response) {

  char* header_end = strstr(response->data, "\r\n\r\n");

  if (header_end) {
    return header_end + 4;
  }
  else {
    return response->data;
  }
}


Buffer *http_url(const char *url) {
  char host[BUF_SIZE];
  strncpy(host, url, BUF_SIZE);

  char *page = strstr(host, "/");
  if (page) {
    page[0] = '\0';

    ++page;
    return http_query(host, page, 80);
  }
  else {

    fprintf(stderr, "could not split url into host/page %s\n", url);
    return NULL;
  }
}

