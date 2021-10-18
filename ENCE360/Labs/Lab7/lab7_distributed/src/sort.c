#include <mpi.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <unistd.h>
#include <time.h>
#include <assert.h>

// Utility timing function
float seconds(struct timespec start, struct timespec stop) {
    float diff = (stop.tv_sec - start.tv_sec) + (float)(stop.tv_nsec - start.tv_nsec) / (float)1e9;
    return diff;
}



//Allocate a square matrix
float *alloc_vec(int n) {
    float *res = (float*)malloc(sizeof(float) * n);
    memset(res, 0, sizeof(float) * n);

    return res;
}

// Fill a vector random values between 0 and 1
void random_vec(float *res, int n) {

    int i;
    for (i = 0; i < n; ++i) {
        res[i] = drand48();
    }
}



// Merge two arrays into one
void merge(float *a, int n1, float *b, int n2, float *arr) {
    int i = 0, j = 0, n = 0;

    // While there still exist elements in the source arrays
    while (i < n1 && j < n2) {
        // Add smallest element and increment
        if (a[i] < b[j]) {
            arr[n++] = a[i];
            i++;
        }
        else {
            arr[n++] = b[j];
            j++;
        }
    }

    // Merge uneven ends if there still exist values not merged
    while (i < n1) arr[n++] = a[i++];
    while (j < n2) arr[n++] = b[j++];
}

//Merge two arrays and allocate for the result
float *merge_alloc(float *a, int n1, float *b, int n2) {
    float *res = (float*)malloc(sizeof(float) * (n1 + n2));
    merge(a, n1, b, n2, res);
    return res;
}


// Comparator function for qsort
int compare(const void *a, const void *b) {
    float *x = (float *)a;
    float *y = (float *)b;

    if (*x < *y) return -1;
    else if (*x > *y) return 1;
    else return 0;
}



// Round to the next power of 2 up
int next_power2(int n) {
    int x = 1;

    while (x < n) {
        x = x << 1;
    }

    return x;
}


// Merge sorted arrays recursively
float *merge_tree(int *result_size, float *sub_vec, int n1, int step) {

    // Get the rank of the process/number of processes
    int rank, world_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    if (step > next_power2(world_size)) {
        // We are done
        *result_size = n1;
        return sub_vec;
    }


    if (rank % step == 0) {

        // We are even with respect to the step size
        // wait for another sub vector from the "odd" side

        int source = rank + step / 2;
        if (source >= world_size) {

            // No need to merge because we are at the edge (no pair)
            return merge_tree(result_size, sub_vec, n1, step * 2);
        }
        else {
            //TODO: Implement me
            // Recieve the length of the vector, allocate space for it and recieve it
            int n2 = 0;
            float *other_vec = NULL;


            // Merge the two sub vectors together
            float *merged = merge_alloc(sub_vec, n1, other_vec, n2);
            free(other_vec);

            // Recursively merge down
            return merge_tree(result_size, merged, n1 + n2, step * 2);
        }

    }
    else {

        // We are odd with respect to the step size
        // send our vector to the even side and finish

        //TODO: Implement me
        // Send the length of the vector, followed by the data
        int dest = rank - step / 2;
        dest = dest; // Unneccessary: remove compiler warning



        //Free memory no longer needed
        free(sub_vec);

        *result_size = 0;
        return NULL;
    }

}


// Test the result
int check_sorted(float *values, int n) {
    int i;
    for (i = 0; i < n - 1; ++i) {
        if (values[i] > values[i + 1]) {
            return 0;
        }
    }

    return 1;
}

int main(int argc, char** argv) {


    // Initialize the MPI environment
    MPI_Init(&argc, &argv);

    // Get the rank of the process/number of processes
    int world_rank, world_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    if (argc < 2) {
        if (world_rank == 0) {
            printf("usage:  ./run.sh        sort num_processes num_elements\n");
        }

        MPI_Finalize();
        exit(1);
    }

    int total_elems = atoi(argv[1]);


    int elems_proc = (total_elems + (world_size - 1)) / world_size; // round up

    float *rand_nums = NULL;

    int total_alloc = elems_proc * world_size;

    if (world_rank == 0) {
        srand48(0);

        // Allocate and initialize vector of random values
        rand_nums = alloc_vec(total_alloc);
        random_vec(rand_nums, total_elems);
    }


    // How many extra elements exist
    int extra = total_alloc - total_elems;

    // Trim the unused elements off the end of the last process
    int is_last = world_rank + 1 == world_size;
    int local_size = elems_proc - (is_last ? extra : 0);
    if (world_rank >= total_elems) {
        local_size = 0;  // In the very odd case which we have more processes than elements
    }

    printf("initialized: rank %d of %d\n", world_rank, world_size);

    //Start the clock
    struct timespec start, stop;
    clock_gettime(CLOCK_REALTIME, &start);

    // Create a buffer that will hold a subset of the random numbers
    float *sub_rand_nums = alloc_vec(elems_proc);

    // Scatter the random numbers to all processes
    //TODO: Implement me

    // Use quicksort to sort the vectors at the local nodes
    qsort(sub_rand_nums, local_size, sizeof(float), compare);

    // Finally use merge sort recursively to merge the vectors between processes
    int result_size;
    float *result = merge_tree(&result_size, sub_rand_nums, local_size, 2);

    //Stop the clock
    clock_gettime(CLOCK_REALTIME, &stop);

    if (world_rank == 0) {
        assert(result_size == total_elems);

        int correct = check_sorted(result, result_size);
        printf("time taken: %.4f result_size: %d, test: %s\n", seconds(start, stop), result_size, correct ? "pass" : "fail");

        free(rand_nums);
        free(result);
    }

    //   Don't need to free sub_rand_nums because merge_tree does so already

    // Cleanup
    MPI_Finalize();
    return 0;

}
