#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <assert.h>


#define handle_error(msg) \
        do { perror(msg); exit(EXIT_FAILURE); } while (0)

typedef struct {
  char *data;
  size_t length;
  size_t reserved;
} Buffer;


/*
* Create a new buffer, reserving an initial amount of memory
* length starts at zero.
*/
Buffer *new_buffer(size_t reserved) {
  Buffer* buffer = malloc(sizeof(Buffer));
  buffer->reserved = reserved;
  buffer->length = 0;
  buffer->data = malloc(reserved); // create room for the null terminator
  return buffer;
}


void free_buffer(Buffer *buffer) {
  free(buffer->data);
  free(buffer);
}

/*
* Append data to a buffer.
* If the reserved amount is not enough to fit the buffer,
* double the reserved amount and try again (until it fits).
* Finally, append the data to the end of the buffer and increase it's length.
*/
void append_buffer(Buffer *buffer, char *data, size_t length) {
  if ((buffer->length + length) > buffer->reserved) {
    while (buffer->length + length > buffer->reserved) {
      buffer->reserved *= 2;
    }
    buffer->data = (char*)realloc(buffer->data, buffer->reserved);
    memset((buffer->data+buffer->length), '\0', buffer->reserved-buffer->length);
  }
  for (int i=0; i < length; i++) {
    // NOTE: Find out why we need this as a pointer
    *(buffer->data + buffer->length + i) = *(data + i);
  }
  buffer->length = buffer->length + length;
}




int main(int argc, char *argv[])
{
  if(argc < 2) {
    fprintf(stderr, "usage: realloc <repeats>\n");
    exit(EXIT_FAILURE);
  }

  size_t repeats = atoi(argv[1]);
  size_t chunk_size = 30;

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


    char *data = malloc(chunk_size);
    Buffer *buffer = new_buffer(chunk_size);

    size_t bytes = 0;
    while((bytes = fread(data, 1, chunk_size, src)) > 0) {
      append_buffer(buffer, data, bytes);
    }

    printf("%s", buffer->data);
    fwrite(buffer->data, buffer->length, 1, dst);

    fclose(src);
    fclose(dst);

    free(data);
    free_buffer(buffer);
  }

  exit(EXIT_SUCCESS);
}
