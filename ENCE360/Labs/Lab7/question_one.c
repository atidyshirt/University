 #include <stdio.h>
 #include <mpi.h>

int main(int argc, char** argv) {
  MPI_Init(NULL, NULL);
  int x;

  MPI_Comm_size(MPI_COMM_WORLD, &x);

  printf("%d\n", x);

}
