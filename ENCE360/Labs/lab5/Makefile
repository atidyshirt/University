LIBS = -lpthread
CC = gcc -Iinclude -std=gnu99
CFLAGS = -g -Wall -O2

.PHONY: default all clean

default: mmap read_write realloc fread_fwrite
all: default

DEPS =
MMAP_OBJ = mmap.o
READ_OBJ = read_write.o
FREAD_OBJ = fread_fwrite.o
REALLOC_OBJ = realloc.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

mmap: $(MMAP_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

read_write: $(READ_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

fread_fwrite: $(FREAD_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

realloc: $(REALLOC_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)


clean:
	-rm -f *.o
	-rm -f mmap read_write fread_fwrite realloc mmap
