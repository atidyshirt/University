# Definitions

CFLAGS = -g -std=c99 -Wall -Werror
OBJECTS = coder.o confab.o

# Targets
coder: $(OBJECTS)
	$(CC) -o coder $(OBJECTS) -lm

coder.o confab.c: confab.h

coder.o : confab.c

Clean:
	rm -rf *.o coder



