#include "types.h"
#include "stat.h"
#include "user.h"

#define NULL 0


int main(void)
{
    int p[2];


    pipe(p);
    int pid = fork();

    if (pid == 0) {

        // Redirect stdin
        close(0);
        dup(p[0]);

        close(p[0]);
        close(p[1]);

        char *argv[] = {"wc", NULL};
        exec("wc", argv);

    } else {

        write(p[1], "hello world\n", 12);

        close(p[0]);
        close(p[1]);

        wait();
    }

    exit();
}
