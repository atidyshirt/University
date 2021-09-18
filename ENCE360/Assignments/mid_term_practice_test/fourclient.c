#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <unistd.h>

#define MAXDATASIZE 1024


int main(int argc, char *argv[])
{
  if (argc != 3) {
    fprintf(stderr,"usage: fourClient hostname port-number\n");
    exit(1);
  }

  // place your code between the lines of //
  ///////////////////////////////////////////////////////

  int server_sockfd = socket(AF_INET, SOCK_STREAM, 0);

  ///////////////////////////////////////////////////////

  struct addrinfo their_addrinfo; // server address info
  struct addrinfo *their_addr = NULL; // connector's address information
  memset(&their_addrinfo, 0, sizeof(struct addrinfo));
  their_addrinfo.ai_family = AF_INET; /* communicate using internet address */
  their_addrinfo.ai_socktype = SOCK_STREAM;  /* use TCP rather than datagram */
  /* get IP address info for the hostname (argv[1]) and port (argv[2]) */
  getaddrinfo(argv[1], argv[2], &their_addrinfo, &their_addr);

  // place your code between the lines of //
  ///////////////////////////////////////////////////////

  connect(server_sockfd, their_addr->ai_addr, their_addr->ai_addrlen);

  ///////////////////////////////////////////////////////

  char buffer[MAXDATASIZE]; //buffer contains data from/to server
  int numbytes; // number of bytes of data read from socket
  // get data from the server:
  // place your code between the lines of //
  ///////////////////////////////////////////////////////

  numbytes = read(server_sockfd, buffer, MAXDATASIZE);

  ///////////////////////////////////////////////////////

  while (numbytes > 0)
  {
    buffer[numbytes-1] = '\0';
    printf("%s\n", buffer); //print out what you received

    // send data to the server and then get data back from the server:
    // place your code between the lines of //
    ///////////////////////////////////////////////////////

    write(server_sockfd, buffer, strlen(buffer));
    numbytes = read(server_sockfd, buffer, MAXDATASIZE - 1);

    ///////////////////////////////////////////////////////
  }
  // place your code between the lines of //
  ///////////////////////////////////////////////////////

  close(server_sockfd);

  ///////////////////////////////////////////////////////

  return 0;
}
