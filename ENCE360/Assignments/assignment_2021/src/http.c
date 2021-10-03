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

Buffer* initilize_buffer(int size) {
  /* initilizes a new buffer of length 0
  * @return Buffer* -- new buffer
  */
  Buffer* buffer = (Buffer *)malloc(sizeof(Buffer));
  buffer->data = (char *)malloc((sizeof(char)) * size);
  buffer->length = size;
  return buffer;
}

Buffer* append_buffer(Buffer* source, Buffer* extend) {
  source->length += extend->length;
  source->data = realloc(source->data, source->length);
  source->data = strncat(source->data, extend->data, source->length);
  return source; // this is just for if we do want to return the buffer
}

void free_buffer(Buffer* buffer) {
  /* free memory associated with a given buffer
  * @param Buffer* -- buffer to free
  */
  free(buffer->data);
  free(buffer);
}

int initilize_socket(char* host, int port) {
  /* Initilizes new TCP socket
  * @param char* -- hostname to connect to
  * @param int -- port to connect on
  * @return int -- file descriptor of new socket
  */

  int rc;
  int their_sockfd = socket(AF_INET, SOCK_STREAM, 0);

  // set address information
  struct addrinfo their_addrinfo;
  struct addrinfo *our_addrinfo = NULL;
  memset(&their_addrinfo, 0, sizeof(their_addrinfo));
  their_addrinfo.ai_family = AF_INET;
  their_addrinfo.ai_socktype = SOCK_STREAM;
  getaddrinfo(host, NULL, &their_addrinfo, &our_addrinfo);

  // connect to socket and error check
  rc = connect(their_sockfd, our_addrinfo->ai_addr, our_addrinfo->ai_addrlen);
  if (rc == -1) {
    perror("Failed to connect"); exit(1);
    freeaddrinfo(our_addrinfo); // free address info
  }

  return their_sockfd;
}

Buffer* http_query(char *host, char *page, int port) {
  /* makes an http 1.0 query to a given website and returns response string
  * @param char* -- hostname of website
  * @param char* -- page to request
  * @param int   -- port to connect on
  * @return Buffer* -- request response in buffer
  */

  int stream_length = 0;
  char recieve_line[BUF_SIZE + 1], send_line[BUF_SIZE + 1];
  int fd = initilize_socket(host, port);
  Buffer* buffer = initilize_buffer(0);

  snprintf(send_line, BUF_SIZE,
    "GET %s HTTP/1.0\r\n"
    "Host: %s\r\n"
    "User-Agent: getter\r\n\r\n", page, host
  );

  if (write(fd, send_line, strlen(send_line)) >= 0) {
    while ((stream_length = read(fd, recieve_line, BUF_SIZE)) > 0) {
      recieve_line[stream_length] = '\0';
      Buffer* stream_buffer = initilize_buffer(stream_length);
      stream_buffer->data = recieve_line;
      append_buffer(buffer, stream_buffer);
      free_buffer(stream_buffer);
    }
  }
  return buffer;
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

