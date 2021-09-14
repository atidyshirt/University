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
    fprintf(stderr, "usage: fread_fwrite <repeats>\n");
    exit(EXIT_FAILURE);
  }
  
  size_t repeats = atoi(argv[1]);
  size_t chunk_size = atoi(argv[2]);
  
  for(int i = 0; i < repeats; ++i) {
  
    FILE *src = fopen("test.dat", "r");
    if (src == NULL) {
      fprintf(stderr, "error opening test.dat");
      exit(EXIT_FAILURE);
    }

    FILE *dst = fopen("output.dat", "w");
    if (dst == NULL) {
      fprintf(stderr, "error opening output.dat");
      exit(EXIT_FAILURE);
    }
    
    
    char *buffer = malloc(chunk_size);
    
    /*
     * TODO: copy the file using fread/fwrite
     * 
     */

    
    fclose(src);
    fclose(dst);
    
    free(buffer);
  }
  
  exit(EXIT_SUCCESS);
}