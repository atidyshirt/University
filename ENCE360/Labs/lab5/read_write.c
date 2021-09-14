#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>


#define handle_error(msg) \
        do { perror(msg); exit(EXIT_FAILURE); } while (0)

size_t file_size(int fd) {
  struct stat sb;  
  if (fstat(fd, &sb) == -1) handle_error("fstat");
  
  return  sb.st_size;
}


int main(int argc, char *argv[])
{
  if(argc < 3) {
    fprintf(stderr, "usage: read_write <repeats>\n");
    exit(EXIT_FAILURE);
  }
  
  size_t repeats = atoi(argv[1]);
  size_t chunk_size = atoi(argv[2]);
  
  for(int i = 0; i < repeats; ++i) {
  
    int src = open("test.dat", O_RDONLY);
    if (src == -1) handle_error("fstat");

    int dst = open("output.dat", O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if (dst == -1) handle_error("open");
    
    
    char *buffer = malloc(chunk_size);
    

    /*
     * TODO: copy the file using read/write
     * 
     */
    
    close(src);
    close(dst);
    
    free(buffer);
  }
  
  exit(EXIT_SUCCESS);
}