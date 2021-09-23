CC = gcc 
# CFLAGS =  -Wall -lrt -lm -O3 -funroll-loops
CFLAGS =  -Wall -lrt -lm -g --std=c99 -lpthread

.PHONY: default all clean

default: fork mutex semaphore thread
all: default



%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS) 

fork: fork.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

mutex: mutex.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

semaphore: semaphore.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

thread: thread.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)	
	

clean:
	-rm -f *.o 
	-rm -f fork mutex semaphore thread
