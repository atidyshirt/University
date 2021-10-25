#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"

char buf[512];


int main(int argc, char *argv[])
{
    int src_fd;
    int dest_fd;

    if (argc != 3){
        printf(1, "usage: cp src_file dest_file\n");
        exit();
    }

    // TODO:
    //----------------Remove this----------------
    src_fd = 0;
    dest_fd = 0;
    src_fd = src_fd;
    dest_fd = dest_fd;
    //----Only here to stop compiler warnings----


    exit();
}
