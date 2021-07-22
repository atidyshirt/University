
/*
* buffer.c - an exercise in memory allocation and pointers.
*
*  compile with: gcc buffer.c -o buffer -std=c99
*  run with ./buffer
*
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>
#include <strings.h>

//
// Structure to hold a buffer of binary data
// Note that we expect that it could hold null(0) characters,
// so we can't rely on strlen to tell us the size or strcpy to copy the data
//

typedef struct BufferStruct {
  char *data;
  int size;
} Buffer;


//
// Write a function to allocate a new buffer,
// then copy the contents from the buffer passed as a parameter
// into the new buffer and return it.
//
Buffer *copy_buffer(Buffer *buffer) {
    Buffer *new_buffer = malloc(sizeof (Buffer));
    new_buffer->data = malloc(buffer->size * sizeof (char));
    memset(new_buffer->data, 0, buffer->size);
    for (int i = 0; i < buffer->size; i++) {
        new_buffer->data[i] = buffer->data[i];
    }
    new_buffer->size = buffer->size;
    return new_buffer;
}

// Example buffer with normal strings
Buffer *example1() {
  Buffer *buffer = (Buffer*)malloc(sizeof(Buffer));
  buffer->data = "hello world\nthis is a string";
  buffer->size = strlen(buffer->data);

  return buffer;
}

// Example buffer storing 3 totally different strings in the same buffer (note the '\0')
Buffer *example2() {
  Buffer *buffer = (Buffer*)malloc(sizeof(Buffer));
  buffer->data = "this string has null\0characters\0 in the middle, beware!";
  buffer->size = 55;
  return buffer;
}

//
// Use fopen to create a file for writing
// Then fwrite to write the buffer to a file
//

void write_buffer(const char *filename, Buffer *buffer) {
  FILE *file = fopen(filename, "w");
  fwrite(buffer->data, 1, buffer->size, file);
  fclose(file);
}



int main() {

  Buffer *example = example2();
  Buffer *copied = copy_buffer(example);

  write_buffer("example1.bin", copied);
  // Check the contents of the file is as you expect using the utility 'strings'
  // i.e. strings example1.bin

  return 0;
}
