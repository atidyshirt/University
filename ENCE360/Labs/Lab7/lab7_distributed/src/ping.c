#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>



int main(int argc, char** argv) {
    // Initialize the MPI environment
    MPI_Init(NULL, NULL);

    // Get the number of processes
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // Get the rank of the process
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    if (world_size % 2) {
        fprintf(stderr, "error: please use an even number of processes\n");
        fprintf(stderr, "usage: ./run.sh ./ping <number of processes>\n");

        MPI_Finalize();
        exit(1);
    }

    int value = 0;
    while (value < 10) {

        if (world_rank % 2 == 1) {
            // Wait for a value back from the client
            MPI_Recv(&value, 1, MPI_INT, world_rank - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("%d: sending pong %d to %d \n", world_rank, value, world_rank - 1);

            value++;
            // Send the value to the client
            MPI_Send(&value, 1, MPI_INT, world_rank - 1, 0, MPI_COMM_WORLD);
        }
        else {
            // Send the value to the client
            MPI_Send(&value, 1, MPI_INT, world_rank + 1, 0, MPI_COMM_WORLD);
            printf("%d: sending ping %d to %d \n", world_rank, value, world_rank + 1);

            // Wait for a value back from the client
            MPI_Recv(&value, 1, MPI_INT, world_rank + 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        }
    }


    // Cleanup
    MPI_Finalize();
    return 0;
}