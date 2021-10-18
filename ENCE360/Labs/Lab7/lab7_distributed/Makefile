CC = mpicc.openmpi -Iinclude -I./src
# CFLAGS =  -Wall -lrt -lm -O3 -funroll-loops
CFLAGS =  -Wall -lrt -lm -g

.PHONY: default all clean

default: hello_world pass_the_parcel ping vector_len sort permissions
all: default



%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS) 

hello_world: src/hello_world.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

pass_the_parcel: src/pass_the_parcel.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

ping: src/ping.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

vector_len: src/vector_len.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)	
	
sort: src/sort.c $(TEST_OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

permissions:
	chmod +x ./run.sh && chmod +x run_remote.sh


clean:
	-rm -f src/*.o test/*.o
	-rm -f hello_world pass_the_parcel ping vector_len sort
