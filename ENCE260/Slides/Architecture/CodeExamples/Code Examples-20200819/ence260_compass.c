/* compass.c
 * Example for ENCE260 - use of pointers
 *    P.J. Bones  UCECE
 *    Last modified:  22.7.2017
 */
#include <stdio.h>

#define NORTH 1
#define EAST  2
#define SOUTH 3
#define WEST  4

char* pointStr (int point) {
    static char* name[] = {"", "North", "East", "South", "West"};

    if (point > 0 && point < 5)
        return name[point];
    else
        return name[0];
}

int main(void) {
    int index;
    char* northStr = pointStr (NORTH);

    printf ("In clockwise order the compass points are:\n");
    for (index = 1; index < 5; index++)
        printf ("%s ", pointStr (index));
    printf ("\n\n");

    return 0;
}