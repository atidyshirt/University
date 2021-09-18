#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <assert.h>

#define NUM_THREADS 10

typedef struct {

	// Read and write semaphores for our channel
	sem_t read;
	sem_t write;

	// Global shared data
	int global_data;

} Channel;

void read_data();
void set_data();
void init_channel();

int main()
{
	pthread_t threads[NUM_THREADS];
	Channel channel;
	int i;

	srand(2018);
	init_channel(&channel);

	for(i = 0; i < NUM_THREADS; i += 2) {
		pthread_create(&threads[i], NULL, (void*)&set_data, &channel);
		pthread_create(&threads[i+1], NULL, (void*)&read_data, &channel);
	}

	// wait for threads to finish before continuing
	// place your code between the lines of //
	///////////////////////////////////////////////
	for(i = 0; i < NUM_THREADS; i += 1) {
    pthread_join(threads[i], NULL);
  }
	///////////////////////////////////////////////

	printf("exiting\n");
	exit(0);
}

/* child thread
*
*/
void set_data(Channel *channel)
{
	// place your code between the lines of //
	///////////////////////////////////////////////
  sem_wait(&channel->write);
	///////////////////////////////////////////////
	assert(channel->global_data == 0);

	printf("Setting data\t");
	channel->global_data = rand();

	// place your code between the lines of //
	///////////////////////////////////////////////
  sem_post(&channel->read);
	///////////////////////////////////////////////
}

void read_data(Channel *channel)
{
	int data;

	// place your code between the lines of //
	///////////////////////////////////////////////
  sem_wait(&channel->read);
	///////////////////////////////////////////////

	data = channel->global_data;
	channel->global_data = 0;
	printf("Data: %d\n", data);

	// place your code between the lines of //
	///////////////////////////////////////////////
  sem_post(&channel->write);
	///////////////////////////////////////////////
}

void init_channel(Channel *channel)
{

	// Initialise count of the read semaphore to 0 (there's nothing to read yet)
	// place your code between the lines of //
	///////////////////////////////////////////////
  sem_init(&channel->read, 0, 0);
	///////////////////////////////////////////////

	// Note the write semaphore is initialised to 1
	//(channel is empty, free for writing)
	// place your code between the lines of //
	///////////////////////////////////////////////
  sem_init(&channel->write, 0, 1);
	///////////////////////////////////////////////
	channel->global_data = 0;

}
