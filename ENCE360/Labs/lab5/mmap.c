#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>


#define handle_error(msg) do { perror(msg); exit(EXIT_FAILURE); } while (0)

size_t file_size(int fd) {
  struct stat sb;
  if (fstat(fd, &sb) == -1) handle_error("fstat");
  return  sb.st_size;
}

int main(int argc, char *argv[])
{
  if(argc < 2) {
    fprintf(stderr, "usage: read_write <repeats>\n");
    exit(EXIT_FAILURE);
  }
  size_t repeats = atoi(argv[1]);
  for(int i = 0; i < repeats; ++i) {
    int src = open("test.dat", O_RDONLY);
    if (src == -1) handle_error("fstat");
    int dst = open("output.dat", O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if (dst == -1) handle_error("open");
    size_t size = file_size(src);
    if(ftruncate(dst, size)) handle_error("ftruncate");
    char* src_map = mmap(NULL, size, PROT_READ, MAP_PRIVATE, src, 0);
    char* dst_map = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, dst, 0);
    memcpy(dst_map, src_map, size);
    munmap(src_map, size);
    munmap(dst_map, size);
    close(src);
    close(dst);
  }

  exit(EXIT_SUCCESS);
}
